# coding: utf-8
import os
from dotenv import load_dotenv
import tweepy
from datetime import timedelta

load_dotenv(override=True)

auth = tweepy.OAuth1UserHandler(
   os.getenv('TWITTER_API_KEY'),
   os.getenv('TWITTER_API_KEY_SECRET'),
   os.getenv('TWITTER_API_ACCESS_TOKEN'),
   os.getenv('TWITTER_API_ACCESS_TOKEN_SECRET'),
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)