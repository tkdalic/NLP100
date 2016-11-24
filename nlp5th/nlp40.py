#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re
from Morth import Morph
from pprint import pprint


def mecab_list(filename):
    ans = []
    with open(filename, 'r') as f:
        for row in f.readlines():
            spliter = re.split('\t|,', row)
            if len(spliter) > 7:
                ans.append(Morph(spliter[0], spliter[
                           7], spliter[1], spliter[2]))

    return ans


if __name__ == '__main__':
    pprint(mecab_list('neko.txt.cabocha'))
