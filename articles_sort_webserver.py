from flask import Flask
from flask import request
import requests
import json
from random import shuffle
import os
import yaml
from flask_cors import CORS, cross_origin

with open("application.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

if os.environ.has_key('SERVICE_ENVIRONMENT'):
    environment = os.environ['SERVICE_ENVIRONMENT']
else:
    environment = cfg['default_environment']

app = Flask(__name__)


# http://localhost:5002/sort/58b1800dc9e77c0001d1d702?count=10
@app.route('/sort/<user_id>')
@cross_origin()
def sort(user_id):
    print 'RECEIVED REQUEST'
    count = request.args.get('count')
    articles_request = requests.get('%s/article/byUserId/%s/unread?page=0&size=%s' % (cfg[environment]['pocket_square_articles_service'], user_id, count))
    response = articles_request.json()

    new_response = []
    for k in response:
        del k["content"]
        new_response.append(k)
    shuffle(new_response)
    print 'SENT RESPONSES'
    return json.dumps(new_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=cfg[environment]['port'], debug=cfg[environment]['debug'])
