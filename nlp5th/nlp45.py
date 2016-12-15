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
            if '動詞' in {v.pos for v in chunk.morphs}:
                verb = [morph.base for morph in chunk.morphs if morph.pos == '動詞'][0]
                case = ' '.join(sorted([chunks[src].morphs[-1].surface for src in chunk.srcs if len(
                    chunks[src].morphs) > 0 and chunks[src].morphs[-1].pos == '助詞']))

                if len(case) > 0:
                    print('{0}\t{1}'.format(verb, case))
