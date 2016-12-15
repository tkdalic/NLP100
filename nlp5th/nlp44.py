#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import sys
from nlp41 import chunks_list
from graphviz import Digraph


if __name__ == '__main__':
    n = 11
    if len(sys.argv) > 1:
        n = int(sys.argv[1]) - 1
    G = Digraph(format='png')
    G.attr('node', shape='circle')

    for k, chunk in enumerate(chunks_list('neko.txt.cabocha')[n]):
        G.node(str(k), ''.join([morph.surface for morph in chunk.morphs]))

    for k, chunk in enumerate(chunks_list('neko.txt.cabocha')[n]):
        if chunk.dst != '-1':
            G.edge(str(k), chunk.dst)

    G.render('nlp44')
