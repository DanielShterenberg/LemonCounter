import logging
import os
import re
from multiprocessing import Manager

from flask import Flask, request, json

from counters import count_words_from_path, count_words_from_url, count_words_from_string

app = Flask(__name__)
manager = Manager()
word_counter = manager.dict()
logging.basicConfig(filename='logs.log', level=logging.INFO)


@app.route('/all-counts', methods=['GET'])
def all_counts():
    return str(word_counter), 200


@app.route('/reset', methods=['POST'])
def reset_dict():
    word_counter.clear()
    return "Counter has been reset successfully", 200


@app.route('/count', methods=['GET'])
def count():
    word = request.args.get('word')
    if word not in word_counter:
        return str(0), 200
    return str(word_counter[word]), 200


# Decided not to use multipart but rather assume that I have the local file on my environment. I didn't want to start
# exploring a way to only read the file once without saving it.
@app.route('/add_words', methods=['POST'])
def add_words():
    req_data = request.get_data()
    data_json = json.loads(req_data)

    if not data_json:
        return "The request should contain a json with a 'data' field", 400
    raw_data = data_json['data']

    if is_url(raw_data):
        count_words_from_url(word_counter, raw_data)
    elif is_path(raw_data):
        count_words_from_path(word_counter, raw_data)
    else:
        count_words_from_string(word_counter, raw_data)
    return "", 200


# https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not/38020041
def is_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def is_path(path):
    return os.path.exists(os.path.dirname(path))


if __name__ == '__main__':
    manager = Manager()
    app.run(debug=True)
