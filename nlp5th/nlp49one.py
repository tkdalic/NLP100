#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp41 import chunks_list


if __name__ == '__main__':
    for chunks in chunks_list('neko.txt.cabocha'):
        for chunk in chunks:
            for morph in chunk.morphs[:]:
                if morph.pos == '記号':
                    chunk.morphs.remove(morph)

        for chunk in chunks:
            if '名詞' in {v.pos for v in chunk.morphs}:
                dst = int(chunk.dst)
                pas = [''.join([v.surface for v in chunk.morphs])]
                while dst != -1:
                    pas.append(
                        ''.join([v.surface for v in chunks[dst].morphs]))
                    dst = int(chunks[dst].dst)
                print(' -> '.join(pas))
