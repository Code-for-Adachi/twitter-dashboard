# coding: utf-8
import os
from dotenv import load_dotenv
import tweepy
from datetime import timedelta

load_dotenv(override=True)

#auth = tweepy.OAuth1UserHandler(
#   os.getenv('TWITTER_API_KEY'),
#   os.getenv('TWITTER_API_KEY_SECRET'),
#   os.getenv('TWITTER_API_ACCESS_TOKEN'),
#   os.getenv('TWITTER_API_ACCESS_TOKEN_SECRET'),
#)

#api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

#streaming_client = tweepy.StreamingClient(os.getenv('TWITTER_API_BEARER_TOKEN'))
#streaming_client.sample()
#streaming_client.add_rules(tweepy.StreamRule("足立区"))
#streaming_client.filter()

class TweetPrinterV2(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print("-"*50)

printer = TweetPrinterV2(os.getenv('TWITTER_API_BEARER_TOKEN'))

# add new rules
rule = tweepy.StreamRule(value="足立区")
printer.add_rules(rule)
print(printer.get_rules())
printer.filter()
