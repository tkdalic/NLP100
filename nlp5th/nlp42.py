#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp41 import chunks_list


if __name__ == '__main__':
    for chunks in chunks_list('neko.txt.cabocha'):
        for chunk in chunks:
            if chunk.dst != '-1':
                print('{0}\t{1}'.format(''.join([morph.surface for morph in chunk.morphs]),
                                        ''.join([morph.surface for morph in
                                                 chunks[int(chunk.dst)].morphs])))
