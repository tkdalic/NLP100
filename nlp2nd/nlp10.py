#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-


def wc(filename):
    return open(filename, encoding='utf-8').read().count('\n')


if __name__ == '__main__':
    print(wc('hightemp.txt'))
