#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
# import re
import json
from nlp20 import articler


def infobox():
    jsons = articler('jawiki-country.json', 'title', 'イギリス')
#    ans = {}
#    end = re.compile("}}")
#    for v in
    return {v.lstrip('*|').split('=', 1)[0].strip(): v.lstrip('*|').split('=', 1)[1].strip()
            for v in json.loads(jsons)['text']
            .split('{{基礎情報', 1)[1].split('\n}}\n', 1)[0].split('\n')
            if v.find('=') != -1}


if __name__ == '__main__':
    ans = infobox()
    for k, v in ans.items():
        print(k, v)
