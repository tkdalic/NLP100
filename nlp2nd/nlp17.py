#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    str = open('hightemp.txt', encoding='utf-8').readline()
    char = set(str)
    for v in sorted(char):
        print(v, end='')
