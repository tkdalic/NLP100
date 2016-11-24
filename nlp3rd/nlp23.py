#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re
import json
from nlp20 import articler


if __name__ == '__main__':
    jsons = articler('jawiki-country.json', 'title', 'イギリス')

    for k, v in {v.strip('='): (int)(v.count('=') / 2 - 1)
                 for v in json.loads(jsons)['text'].split('\n')
                 if re.compile("==.*==").match(v)}.items():
        print(k, v)
