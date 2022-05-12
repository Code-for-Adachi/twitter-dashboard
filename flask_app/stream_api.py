# coding: utf-8
import os
import json
from dotenv import load_dotenv
import tweepy
import datetime
from textblob import TextBlob
from tweet_store import TweetStore


load_dotenv(override=True)
store = TweetStore()
client = tweepy.Client(bearer_token=os.getenv('TWITTER_API_BEARER_TOKEN'))

class TweetPrinterV2(tweepy.StreamingClient):
    def on_tweet(self, status):

        user_field = client.get_tweet(id=status.id, user_fields=['id', 'name', 'username', 'profile_image_url'])
        print(user_field.data)

        if ('RT @' not in status.text):
            blob = TextBlob(status.text)
            sent = blob.sentiment
            polarity = sent.polarity
            subjectivity = sent.subjectivity

            tweet_item = {
                'id_str': user_field.data['id'],
                'text': status.text,
                'polarity': polarity,
                'subjectivity': subjectivity,
                'username': user_field.data['username'],
                'name': user_field.data['name'],
                'profile_image_url': user_field.data['profile_image_url'],
                'received_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            store.push(tweet_item)
            print("Pushed to redis:", tweet_item)

    def on_error(self, status_code):
        if status_code == 420:
            return False

printer = TweetPrinterV2(os.getenv('TWITTER_API_BEARER_TOKEN'))
rule = tweepy.StreamRule(value='足立区')
printer.add_rules(rule)
printer.filter()