#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp25 import infobox


def infobox2():
    return {k: v.replace("'", '') for k, v in infobox().items()}


if __name__ == '__main__':
    for k, v in infobox2().items():
        print(k, v)
