#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp28 import infobox4


if __name__ == '__main__':
    ans = infobox4()
    print('https://www.mediawiki.org/wiki/File:' + ans['国旗画像'].replace(' ', '_'))
