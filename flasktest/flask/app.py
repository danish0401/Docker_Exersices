from flask import Flask
from redis import Redis
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
@app.route('/python_app')
def hello():
    redis.incr('hits')
    counter = "You clicked "+str(redis.get('hits'),'utf-8') + " times"
    return counter
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)