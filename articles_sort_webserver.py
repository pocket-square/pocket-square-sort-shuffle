from flask import Flask
from flask import request as flask_request
import requests
import json
from random import shuffle
import os
import yaml

with open("application.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

environment = os.environ['SERVICE_ENVIRONMENT']
if not environment:
    environment = cfg['default_environment']

app = Flask(__name__)


@app.route('/sort/<user_id>')
def sort(user_id):
    count = flask_request.args.get('count')
    request = requests.get('%s/article/byUserId/%s/unread?page=0&size=%s' % (cfg[environment]['pocket_square_articles_service'], user_id, count))
    response = request.json()

    new_response = []
    for k in response:
        new_response.append(k)
    shuffle(new_response)
    return json.dumps(new_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=cfg[environment]['port'], debug=cfg[environment]['debug'])
