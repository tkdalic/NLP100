#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    hightemp = open('hightemp.txt', 'r', encoding='utf-8')

    col1 = open('col1.txt', 'w', encoding='utf-8')
    col2 = open('col2.txt', 'w', encoding='utf-8')

    for row in hightemp:
        words = row.split('\t')
        col1.write(words[0] + '\n')
        col2.write(words[1] + '\n')
