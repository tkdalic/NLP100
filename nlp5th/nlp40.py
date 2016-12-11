#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re
from Morth import Morph


def morph_list(filename):
    sentences = []
    sentence = []
    with open(filename, 'r') as f:
        for row in f.readlines():

            if row == 'EOS\n':
                sentences.append(sentence)
                sentence = []

            if row[0] != '*':
                spliter = re.split('\t|,', row)
                if len(spliter) > 7:
                    sentence.append(Morph(spliter[0], spliter[
                        7], spliter[1], spliter[2]))

    return sentences


if __name__ == '__main__':
    for morth in morph_list('neko.txt.cabocha')[2]:
        print(morth.surface, morth.base, morth.pos, morth.pos1)
