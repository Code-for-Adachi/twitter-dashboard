# coding: utf-8
from flask import Flask, Response, render_template, stream_with_context, request
import time
import stream_api

app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    for buffer in rv:
        yield buffer
        time.sleep(0.5)

@app.route('/')
def hello_world_with_template():
    comments = ['Count: {}'.format(i) for i in range(20)]
    return Response(stream_template('index.html', comments=comments))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)