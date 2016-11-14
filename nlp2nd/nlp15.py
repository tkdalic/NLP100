#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

import sys
import nlp10


def tail(filename, num):

    num -= nlp10.wc('hightemp.txt')

    f = open(filename, 'r', encoding='utf-8')

    for v in f.readlines():
        if num >= 0:
            print(v.rstrip('\n'))
        num += 1


if __name__ == '__main__':
    tail(sys.argv[1], int(sys.argv[2]))

# diff <(python nlp15.py hightemp.txt 5) <(tail -n 5 hightemp.txt)
