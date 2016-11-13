#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re
import json
from collections import defaultdict
from nlp20 import articler


if __name__ == '__main__':
    jsons = articler('jawiki-country.json', 'title', 'イギリス')
    ans = defaultdict(int)
    for v in json.loads(jsons)['text'].split('\n'):
        if re.compile("==.*==").match(v):
            ans[v.strip('=')] = (int)(v.count('=') / 2 - 1)

    for k, v in ans.items():
        print(k, v)
