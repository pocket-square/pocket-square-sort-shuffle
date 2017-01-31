from flask import Flask
import requests
import json
from random import shuffle

app = Flask(__name__)


@app.route('/sort/<user_id>')
def sort(user_id):
    request = requests.get('http://pocket_square_articles:8080/articles/' + user_id + '/unread')
    response = request.json()

    new_response = []
    for k in response:
        new_response.append(k)
    shuffle(new_response)
    return json.dumps(new_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
