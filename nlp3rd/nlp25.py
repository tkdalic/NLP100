#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re
import json
from nlp20 import articler


def infobox():
    jsons = articler('jawiki-country.json', 'title', 'イギリス')
    ans = {}
    flag = False
    start = re.compile("{{基礎情報")
    end = re.compile("}}")
    for v in json.loads(jsons)['text'].split('\n'):
        if start.search(v):
            flag = True
        if flag:
            if v.find('=') != -1:
                spliter = v.lstrip('*|').split('=', 1)
                ans[spliter[0].strip()] = spliter[1].strip()
            if end.match(v):
                return ans


if __name__ == '__main__':
    ans = infobox()
    for k, v in ans.items():
        print(k, v)
