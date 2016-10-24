#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

import random

if __name__ == '__main__':
    str = input('please input >> ')
    ans = ''
    for v1 in str.split(' '):
        if len(v1) < 4:
            ans += v1 + ' '
        else:
            mozilist = list(v1)
            ans += mozilist.pop(0)
            end = mozilist.pop()
            while len(mozilist) > 0:
                ans += mozilist.pop(random.randint(0, len(mozilist) - 1))
            ans += end + ' '

    print(ans)
