from flask import Flask, Response, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello-world')
def hello_world():
    def generate():
        for comment in ['hoge', 'fuga', 'piyo', 'iruka']:
            yield '<li>' + comment + '</li>'
            time.sleep(0.5)  # 動作をわかりやすくするために追加
    return Response(generate())

if __name__ == "__main__":
    app.run(debug=True)