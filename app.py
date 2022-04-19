from flask import Flask, Response, render_template
import os
from dotenv import load_dotenv
import tweepy
from stream_api import TweetPrinterV2

load_dotenv(override=True)

app = Flask(__name__)

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.disable_buffering()
    return rv

@app.route('/')
def index():
    #return render_template('index.html')
    printer = TweetPrinterV2(os.getenv('TWITTER_API_BEARER_TOKEN'))
    ## add new rules
    rule = tweepy.StreamRule(value="足立区")
    printer.add_rules(rule)
    rows = printer.filter()
    return app.Response(stream_template('index.html', rows=rows))

if __name__ == "__main__":
    app.run(debug=True)