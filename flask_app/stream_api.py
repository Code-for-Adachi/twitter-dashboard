# coding: utf-8
import os
import tweepy
import datetime
from textblob import TextBlob
from tweet_store import TweetStore

store = TweetStore()
client = tweepy.Client(bearer_token=os.getenv('TWITTER_API_BEARER_TOKEN'))

class TweetPrinterV2(tweepy.StreamingClient):
    def on_tweet(self, status):
        tw = client.get_tweet(id=int(status.id), expansions=["author_id"], user_fields=['id', 'name', 'username', 'profile_image_url'])
        blob = TextBlob(status.text)
        sent = blob.sentiment
        polarity = sent.polarity
        subjectivity = sent.subjectivity

        tweet_item = {
            'id_str': tw.includes["users"][0].id,
            'text': status.text,
            'polarity': polarity,
            'subjectivity': subjectivity,
            'username': tw.includes["users"][0].username,
            'name': tw.includes["users"][0].name,
            'profile_image_url': tw.includes["users"][0].profile_image_url,
            'received_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        store.push(tweet_item)
        print("Pushed to redis:", tweet_item)

    def on_error(self, status_code):
        if status_code == 420:
            return False

printer = TweetPrinterV2(bearer_token=os.getenv('TWITTER_API_BEARER_TOKEN'))
rule = tweepy.StreamRule(value=os.getenv('SEARCH_STRINGS'))
printer.add_rules(rule)
printer.filter()
