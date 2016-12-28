from flask import Flask
from urllib2 import Request, urlopen, URLError
import json
from random import shuffle

app = Flask(__name__)


@app.route('/sort')
def sort():
    request = Request('http://127.0.0.1:8080/fetch_cached')

    try:
        response_json = urlopen(request).read()
        response = json.loads(response_json)
        new_response = []
        for k in response:
            new_response.append(response[k])
        shuffle(new_response)
        return json.dumps(new_response)
    except URLError, e:
        return 'Something went wrong:', e


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')