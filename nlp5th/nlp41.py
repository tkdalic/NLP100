#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re
import pandas as pd
from Morth import Morph
from Chunk import Chunk


def chunks_list(filename):
    sentences = []
    chunks = []
    relation = []
    with open(filename, 'r') as f:
        for row in f.readlines():

            if row[0] == '*':
                spliter = row.split(' ')
                chunks.append(Chunk([], spliter[2][:-1], []))
                if spliter[2] != '-1D':
                    relation.append((spliter[2][:-1], spliter[1]))
            else:
                spliter = re.split('\t|,', row)
                if len(spliter) > 7:
                    chunks[-1].morphs.append(Morph(spliter[0], spliter[
                        7], spliter[1], spliter[2]))

            if row == 'EOS\n':
                for k, v in relation:
                    chunks[int(k)].src.append(int(v))
                sentences.append(chunks)
                relation = []
                chunks = []

    return sentences


if __name__ == '__main__':
    print(pd.DataFrame([[''.join([morph.surface for morph in chunk.morphs]), chunk.dst]
                        for chunk in chunks_list('neko.txt.cabocha')[7]],
                       columns=['文節', '係り先']))
