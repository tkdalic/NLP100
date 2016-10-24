#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

import sys
import nlp10


if __name__ == '__main__':
    if len(sys.argv) > 1:
        split = int(sys.argv[1])
        num = int(nlp10.wc('hightemp.txt') / split)
        shou = nlp10.wc('hightemp.txt') % split
    else:
        split = 1
        num = nlp10.wc('hightemp.txt')
        shou = 0

    r = open('hightemp.txt', 'r', encoding='utf-8')

    for i in range(split):
        w = open('split-' + str(i) + '.txt', 'w', encoding='utf-8')
        for j in range(num):
            w.write(r.readline())
        if shou != 0:
            shou -= 1
            w.write(r.readline())
