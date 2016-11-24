#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import json
from nlp20 import articler


def categorier(filename, key, value):
    jsons = articler(filename, key, value)

    return [v for v in json.loads(jsons)['text'].split('\n') if v.find('Category') > 0]


if __name__ == '__main__':
    for v in categorier('jawiki-country.json', 'title', 'イギリス'):
        print(v)
