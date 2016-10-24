#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

from collections import defaultdict

if __name__ == '__main__':
    r = open('hightemp.txt', 'r', encoding='utf-8')

    ans = defaultdict(list)

    for v in r.readlines():
        ans[v.split()[2]] = v.split()

    for k, v in sorted(ans.items()):
        print('\t'.join(v))
