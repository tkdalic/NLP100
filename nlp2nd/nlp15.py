#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

import sys
import nlp10


if __name__ == '__main__':
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        num -= nlp10.wc('hightemp.txt')
    else:
        num = 0

    f = open('hightemp.txt', 'r', encoding='utf-8')

    for v in f.readlines():
        if num >= 0:
            print(v.strip())
        num += 1
