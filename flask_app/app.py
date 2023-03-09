# coding: utf-8
import os
from flask import Flask, render_template
from tweet_store import TweetStore

app = Flask(__name__)
store = TweetStore()

@app.route('/')
def index():
    return render_template('index.html',
        search_strigns = os.getenv('SEARCH_STRINGS'))

@app.route('/tweets')
def show_tweets():
    tweets = store.tweets()
    return render_template('tweets.html', tweets=tweets)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", threaded=True, port=8000, debug=True)
