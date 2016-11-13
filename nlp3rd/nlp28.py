#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp27 import infobox3
import re


def infobox4():
    ans = infobox3()
    ans2 = {}
    for k, v in ans.items():
        ans2[k] = re.sub('\[|\]|\{|\}', '', v)
    return ans2


if __name__ == '__main__':
    ans = infobox4()

    for k, v in ans.items():
        print(k, v)
