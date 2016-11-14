#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

import sys


def head(filename, num):

    f = open(filename, 'r')

    for v in f.readlines():
        if num == 0:
            exit()
        print(v.strip())
        num -= 1


if __name__ == '__main__':
    head(sys.argv[1], int(sys.argv[2]))

# diff <(python nlp14.py hightemp.txt 4) <(head -n 4 hightemp.txt)
