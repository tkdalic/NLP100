#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import sys


def sed(filename):
    return open(filename, encoding='utf-8').read().rstrip('\n').replace('\t', ' ')


if __name__ == '__main__':
    print(sed(sys.argv[1]))

# diff <(python nlp11.py hightemp.txt) <(cat hightemp.txt |tr '\t' ' ')
