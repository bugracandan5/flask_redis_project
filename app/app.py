from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Hello World! This page has been viewed {count} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


