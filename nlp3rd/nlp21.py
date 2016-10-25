#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import json
from nlp20 import articler


def categorier(filename, key, value):
    jsons = articler(filename, key, value)
    category = []
    for v in json.loads(jsons)['text'].split('\n'):
        if v.find('Category') > 0:
            category.append(v)

    return category


if __name__ == '__main__':
    category = categorier('jawiki-country.json', 'title', 'イギリス')

    for v in category:
        print(v)
