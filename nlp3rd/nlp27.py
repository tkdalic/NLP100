#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp26 import infobox2


def infobox3():
    ans = infobox2()
    ans2 = {}
    for k, v in ans.items():
        ans2[k] = v.replace("[[", '').replace(']]', '')
    return ans2


if __name__ == '__main__':
    ans = infobox3()

    for k, v in ans.items():
        print(k, v)
