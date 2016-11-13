#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp25 import infobox


def infobox2():
    ans = infobox()
    ans2 = {}
    for k, v in ans.items():
        ans2[k.replace("'", '')] = v.replace("'", '')
    return ans2


if __name__ == '__main__':
    ans = infobox2()

    for k, v in ans.items():
        print(k, v)
