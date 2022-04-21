# coding: utf-8
import os
from dotenv import load_dotenv
import tweepy
from datetime import timedelta

load_dotenv(override=True)

class TweetPrinterV2(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print("-"*50)

def get_stream(word):
    printer = TweetPrinterV2(os.getenv('TWITTER_API_BEARER_TOKEN'))

    # add new rules
    rule = tweepy.StreamRule(value=word)
    printer.add_rules(rule)
    printer.filter()