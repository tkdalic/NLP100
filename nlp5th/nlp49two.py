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


def Yword(ynoun):
    Y = ''
    for v in xnoun.morphs:
        if v.pos != '名詞':
            Y += v.surface
        else:
            Y += 'Y'
    return re.sub('Y.+$', 'Y', Y)


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

        for relation in relations:
            for xnoun in noun_list:
                if xnoun in relation:
                    rel = relation[relation.index(xnoun) + 1:]
                    X = Xword(xnoun)
                    for ynoun in noun_list:
                        if ynoun in rel:
                            Y = Yword(ynoun)
                            if len(rel[:relation.index(ynoun) - 1]) > 0:
                                print(' -> '.join([X, ' -> '.join([''.join(
                                    [v2.surface for v2 in v.morphs]) for v in rel[:rel.index(ynoun) - 1]]), Y]))
                            else:
                                print(X, '->', Y)
