#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import json
from nlp20 import articler


if __name__ == '__main__':
    jsons = articler('jawiki-country.json', 'title', 'イギリス')

    for v in json.loads(jsons)['text'].split('\n'):
        if v.find('Category') > 0:
            print(v)
