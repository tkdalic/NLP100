#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import sys


def cut(name1='hightemp.txt', name2='col1.txt', name3='col2.txt'):
    hightemp = open('hightemp.txt', 'r', encoding='utf-8')

    col1 = open('col1.txt', 'w', encoding='utf-8')
    col2 = open('col2.txt', 'w', encoding='utf-8')

    for row in hightemp:
        words = row.split('\t')
        col1.write(words[0] + '\n')
        col2.write(words[1] + '\n')


if __name__ == '__main__':
    cut(sys.argv[1], sys.argv[2], sys.argv[3])

#  cut -f1 hightemp.txt|diff - col1.txt
#  cut -f2 hightemp.txt|diff - col2.txt
