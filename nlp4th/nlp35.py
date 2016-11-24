#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp30 import mecab_list


if __name__ == '__main__':
    ans = []
    syzygy = ''
    length = 0

    for v in mecab_list('neko.txt.mecab'):
        if v['pos'] == '名詞':
            syzygy += v['surface']
            length += 1
        else:
            if length > 1:
                ans.append(syzygy)
            syzygy = ''
            length = 0

    for v in ans:
        print(v)
