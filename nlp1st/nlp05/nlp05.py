#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

import sys


def ngram(str, num):
    ans = [''] * (len(str) + int(num))
    k = -1
    for v in str:
        k += 1
        for i in range(0, int(num)):
            ans[k + i] += v

    for i in range(0, int(num) - 1):
        ans.pop(0)

    return ans


def tgram(str, num):
    ans = [''] * (len(str.split()) + int(num))
    for k, v in enumerate(list(str.split())):
        for i in range(0, int(num)):
            ans[k + i] += v

    for i in range(0, int(num) - 1):
        ans.pop(0)

    return ans


if __name__ == '__main__':
    strs = []
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        for row in f:
            strs.append(row)
    else:
        print('Usage: python 05.py FILE')
        exit()
    torn = input('t or n ? >>')
    num = input('num ? >>')
    if torn == 'n':
        for v in strs:
            ans = ngram(v, num)
            print(ans)
    else:
        for v in strs:
            ans = tgram(v, num)
            print(ans)
