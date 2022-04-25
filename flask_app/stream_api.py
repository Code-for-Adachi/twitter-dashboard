# coding: utf-8
import os
from dotenv import load_dotenv
import tweepy
from datetime import timedelta

load_dotenv(override=True)
api = tweepy.Client(os.getenv('TWITTER_API_BEARER_TOKEN'))

class TweetPrinterV2(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        #print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print(api.get_tweet(id=tweet.id, expansions=["author_id"], user_fields=["username"]))
        tw = api.get_tweet(id=tweet.id, expansions=["author_id"], user_fields=["username"])
        url = "https://twitter.com/" + tw.includes["users"][0].username + "/status/" + str(tweet.id)
        print(url)
        return url

    #def on_data(self, raw_data):
    #    print(raw_data)
    #    print("-"*50)

def get_stream(word):
    printer = TweetPrinterV2(os.getenv('TWITTER_API_BEARER_TOKEN'))

    # add new rules
    rule = tweepy.StreamRule(value=word)
    printer.add_rules(rule)
    printer.filter()

#get_stream('足立区')