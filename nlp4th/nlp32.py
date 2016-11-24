#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp30 import mecab_list


if __name__ == '__main__':
    for v in mecab_list('neko.txt.mecab'):
        if v['pos'] == '動詞':
            print(v['base'])
