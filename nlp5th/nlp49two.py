#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp41 import chunks_list


if __name__ == '__main__':
    for chunks in chunks_list('neko.txt.cabocha'):
        for chunk in chunks:
            for morph in chunk.morphs[:]:
                if morph.pos == '記号':
                    chunk.morphs.remove(morph)

        noun_list = [chunk for chunk in chunks if '名詞' in {
            v.pos for v in chunk.morphs}]
        relations = []
        has_relations = set()
        for chunk in chunks:

            if chunk in has_relations:
                continue

            relation = []
            next_chunk = chunk

            while int(next_chunk.dst) != -1:
                relation.append(next_chunk)
                has_relations.add(next_chunk)
                next_chunk = chunks[int(next_chunk.dst)]
            relations.append(relation)

            for relation in relations:
                for noun in noun_list:
                    if noun in relation:
                        rel = relation[relation.index(noun) + 1:]
                        for noun2 in noun_list:
                            if noun2 in rel:
                                xnoun = 'X' + \
                                    ''.join(
                                        [v.surface for v in noun.morphs[noun.index(noun.morphs.pos == '名詞')]])
                                print(rel[:relation.index(noun2) - 1])

        for chunk in chunks:
            if '名詞' in {v.pos for v in chunk.morphs}:
                dst = int(chunk.dst)
                pas = [''.join([v.surface for v in chunk.morphs])]
                while dst != -1:
                    pas.append(
                        ''.join([v.surface for v in chunks[dst].morphs]))
                    dst = int(chunks[dst].dst)
