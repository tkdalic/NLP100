#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp30 import mecab_list
from collections import defaultdict


if __name__ == '__main__':
    mecablist = mecab_list('neko.txt.mecab')
    ans = defaultdict(int)
    total = len(mecablist)
    i = 0
#    confirm = 0

    for v in mecablist:
        ans[v['surface']] += 1

    for k, v in sorted(ans.items(), key=lambda k: k[1], reverse=True):
        print(k, v / total)
#        confirm += v / total

#    print(confirm)
