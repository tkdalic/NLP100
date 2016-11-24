#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp26 import infobox2


def infobox3():
    return {k: v.replace("[[", '').replace(']]', '') for k, v in infobox2().items()}


if __name__ == '__main__':
    for k, v in infobox3().items():
        print(k, v)
