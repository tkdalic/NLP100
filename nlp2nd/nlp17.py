#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import sys


def diff(filename):

    lists = []
    for row in open(filename).readlines():
        words = row.split('\t')
        lists.append(words[0])

    return sorted(set(lists))


if __name__ == '__main__':
    for v in diff(sys.argv[1]):
        print(v)

# cut -f1 hightemp.txt|LC_ALL=C sort -d|uniq
# python nlp17.py hightemp.txt
