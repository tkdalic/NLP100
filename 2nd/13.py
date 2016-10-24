#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    col1 = open('col1.txt', 'r', encoding='utf-8')
    col2 = open('col2.txt', 'r', encoding='utf-8')
    col = open('col.txt', 'w', encoding='utf-8')

    for c1, c2 in zip(col1.readlines(), col2.readlines()):
        col.write(c1.strip() + ' ' + c2)
