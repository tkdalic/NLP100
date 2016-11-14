#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import sys
from operator import itemgetter

if __name__ == '__main__':

    ans = [v.split()
           for v in open(sys.argv[1], 'r', encoding='utf-8').readlines()]

    for v in sorted(ans, key=itemgetter(2), reverse=True):
        print('\t'.join(v))
