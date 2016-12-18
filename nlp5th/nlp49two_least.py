#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp41 import chunks_list
import re


def Xword(xnoun):
    X = ''
    for v in xnoun.morphs:
        if v.pos != '名詞':
            X += v.surface
        else:
            X += 'X'
    return re.sub('^.+X', 'X', X)


if __name__ == '__main__':
    for chunks in chunks_list('neko.txt.cabocha'):
        for chunk in chunks:
            for morph in chunk.morphs[:]:
                if morph.pos == '記号':
                    chunk.morphs.remove(morph)

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
            relation.append(next_chunk)
            relations.append(relation)

        noun_list = [chunk for chunk in chunks if '名詞' in {
            v.pos for v in chunk.morphs}]
        least_list = []
        has_rel = set()
        for xnoun in noun_list:
            X = Xword(xnoun)
            for ynoun in noun_list[noun_list.index(xnoun) + 1:]:
                for relation in [v for v in relations if xnoun in v]:
                    rel = relation[relation.index(xnoun) + 1:]
                    if ynoun in rel and (xnoun, ynoun) not in has_rel:
                        has_rel.add((xnoun, ynoun))
                        if rel.index(ynoun) > 0:
                            least_list.append(' -> '.join([X, ' -> '.join([''.join(
                                [v2.surface for v2 in v.morphs]) for v in rel[:rel.index(ynoun)]]), 'Y']))
                        else:
                            least_list.append(X + '-> Y')
                        break
        if len(least_list) > 0:
            leas = min({v.count(' -> ') for v in least_list})
            for v in least_list:
                if v.count(' -> ') == leas:
                    print(v)
