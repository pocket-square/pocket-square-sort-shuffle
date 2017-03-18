from flask import Flask
from flask import request as flask_request
import requests
import json
from random import shuffle

app = Flask(__name__)


@app.route('/sort/<user_id>')
def sort(user_id):
    count = flask_request.args.get('count')
    request = requests.get('http://188.166.174.189:28103/article/byUserId/%s/unread?page=0&size=%s' % (user_id, count))
    response = request.json()

    new_response = []
    for k in response:
        new_response.append(k)
    shuffle(new_response)
    return json.dumps(new_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
