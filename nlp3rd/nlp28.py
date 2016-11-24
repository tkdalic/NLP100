#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp27 import infobox3
import re


def infobox4():
    return{k: re.sub('\[|\]|\{|\}', '', v) for k, v in infobox3().items()}


if __name__ == '__main__':

    for k, v in infobox4().items():
        print(k, v)
