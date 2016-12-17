#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp41 import chunks_list
import re


def word(noun, char):
    str = ''
    for v in noun.morphs:
        if v.pos != '名詞':
            str += v.surface
        else:
            str += 'X'
    return re.sub('^.*X', char, str)


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
        has_rel = set()
        least_list = []
        for xnoun in noun_list:
            for ynoun in noun_list[noun_list.index(xnoun) + 1:]:
                for relation in [v for v in relations if xnoun not in v]:
                    if ynoun in relation and (xnoun, ynoun) not in has_rel:
                        has_rel.add((xnoun, ynoun))
                        relation2 = [v for v in relations if xnoun in v][0]
                        for rel_ele in relation:
                            if rel_ele in relation2:
                                if relation2.index(rel_ele) - relation2.index(xnoun) <= 1:
                                    X = word(xnoun, 'X')
                                else:
                                    X = word(xnoun, 'X') + ' -> ' + ' -> '.join([''.join([v2.surface for v2 in v.morphs]) for v in relation2[
                                        relation2.index(xnoun) + 1:relation2.index(rel_ele)]])
                                if relation.index(rel_ele) - relation.index(ynoun) <= 1:
                                    Y = word(ynoun, 'Y')
                                else:
                                    Y = word(ynoun, 'Y') + ' -> ' + ' -> '.join([''.join([v2.surface for v2 in v.morphs]) for v in relation[
                                        relation.index(ynoun) + 1:relation.index(rel_ele)]])
                                least_list.append(
                                    ' | '.join([X, Y, ''.join([v.surface for v in rel_ele.morphs])]))
                                break
                        break
        if len(least_list) > 0:
            leas = min({v.count(' -> ') for v in least_list})
            for v in least_list:
                if v.count(' -> ') == leas:
                    print(v)
