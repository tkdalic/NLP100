#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp30 import mecab_list
from pprint import pprint


if __name__ == '__main__':
    for v in mecab_list('neko.txt.mecab'):
        if v['pos1'] == 'サ変接続' and v['pos'] == '名詞':
            pprint(v)
