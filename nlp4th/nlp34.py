#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp30 import mecab_list


if __name__ == '__main__':
    mecablist = mecab_list('neko.txt.mecab')
    for k, v in enumerate(mecablist):
        if v['surface'] == 'の' and mecablist[k - 1]['pos'] == '名詞' and mecablist[k + 1]['pos'] == '名詞':
            print(mecablist[k - 1]['surface'] +
                  v['surface'] + mecablist[k + 1]['surface'])
