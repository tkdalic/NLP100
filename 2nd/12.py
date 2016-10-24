#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    hightemp = open('hightemp.txt', 'r', encoding='utf-8')
    open('col1.txt', 'w', encoding='utf-8').write(hightemp.readline())
    open('col2.txt', 'w', encoding='utf-8').write(hightemp.readline())
