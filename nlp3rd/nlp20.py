#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

import json


def articler(filename, key, value):
    f = open(filename, 'r', encoding='utf-8')
    for jsons in f.readlines():
        if json.loads(jsons)[key] == value:
            return jsons


if __name__ == '__main__':
    jsons = articler('jawiki-country.json', 'title', 'イギリス')
    print(json.loads(jsons))
