# coding: utf-8
from flask import Flask, Response, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    def generate():
        for comment in ["https://twitter.com/0f04ibFRe3hd9cE/status/1517357824040652801", "https://twitter.com/salmonpink778/status/1517358229520408578"]:
            yield comment
            time.sleep(5)  # 動作をわかりやすくするために追加
    return Response(generate())

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    for buffer in rv:
        yield buffer
        time.sleep(0.5)

@app.route('/hello-world-with-template')
def hello_world_with_template():
    comments = ["https://twitter.com/0f04ibFRe3hd9cE/status/1517357824040652801", "https://twitter.com/salmonpink778/status/1517358229520408578"]
    return Response(stream_template('index.html', comments=comments))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)