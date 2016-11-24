#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

import sys
import nlp10


def sprit(filename, split):

    num = int(nlp10.wc() / split)
    shou = nlp10.wc('hightemp.txt') % split
    num = nlp10.wc('hightemp.txt')

    r = open('hightemp.txt', 'r', encoding='utf-8')

    for i in range(split):
        w = open('split-' + str(i) + '.txt', 'w', encoding='utf-8')
        for j in range(num):
            w.write(r.readline())
        if shou != 0:
            shou -= 1
            w.write(r.readline())


if __name__ == '__main__':
    sprit(sys.argv[1], sys.argv[2])
