#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    num = -1
    if len(sys.argv) > 1:
        num = int(sys.argv[1])

    f = open('hightemp.txt', 'r', encoding='utf-8')

    for v in f.readlines():
        if num == 0:
            exit()
        print(v.strip())
        num -= 1
