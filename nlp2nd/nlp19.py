#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

from collections import defaultdict

if __name__ == '__main__':
    r = open('hightemp.txt', 'r', encoding='utf-8')

    ans = defaultdict(int)

    for v in r.readlines():
        ans[v.split()[0]] += 1

for k, v in sorted(ans.items(), key=lambda x: x[1], reverse=True):
    print(k)
