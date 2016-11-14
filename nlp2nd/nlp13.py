#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-


import sys


def paste(cols1, cols2, cols):
    col1 = open(cols1, 'r', encoding='utf-8')
    col2 = open(cols2, 'r', encoding='utf-8')
    col = open(cols, 'w', encoding='utf-8')

    for c1, c2 in zip(col1.readlines(), col2.readlines()):
        col.write(c1.strip() + '\t' + c2)


if __name__ == '__main__':
    paste(sys.argv[1], sys.argv[2], sys.argv[3])

# diff <(cat col.txt ) <(paste col1.txt col2.txt)
