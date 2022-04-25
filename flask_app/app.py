# coding: utf-8
import os
from datetime import timedelta
import threading
from flask import Flask, Response, render_template
from dotenv import load_dotenv
import tweepy

load_dotenv(override=True)
api = tweepy.Client(os.getenv('TWITTER_API_BEARER_TOKEN'))
app = Flask(__name__)

class TweetPrinterV2(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        #print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        list = []
        list.append(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        #print(api.get_tweet(id=tweet.id, expansions=["author_id"], user_fields=["username"]))
        #tw = api.get_tweet(id=tweet.id, expansions=["author_id"], user_fields=["username"])
        #url = "https://twitter.com/" + tw.includes["users"][0].username + "/status/" + str(tweet.id)
        #return url
        return list

@app.route('/')
def index():
    t = Thread()
    t.start()
    return render_template('index.html')

@app.route('/data')
def get_stream():
    printer = TweetPrinterV2(os.getenv('TWITTER_API_BEARER_TOKEN'))

    # add new rules
    rule = tweepy.StreamRule(value="足立区")
    printer.add_rules(rule)
    printer.filter()

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True, port=5000, debug=True)