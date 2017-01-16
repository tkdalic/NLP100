#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import sys
from graphviz import Digraph
import re


def depnlp(filename):
    ans = []
    with open(filename) as f:
        for sentence in re.findall('<sentence id[\s\S]+?</sentence>', f.read()):
            for token in re.findall('<dependencies type="collapsed-dependencies">[\s\S]+?</dependencies>', sentence):
                dep_list = []
                for dep in re.findall('<dep type=".+">[\s\S]+?</dep>', token):

                    type = re.search('dep type=".+?"', dep).group()[10:-1]
                    gover = re.search('<gover.*>', dep).group()
                    depen = re.search('<depen.*>', dep).group()

                    gover_num = re.search(
                        '<governor idx="[0-9]+".*?>', gover).group()[15:-2]
                    depen_num = re.search(
                        '<dependent idx="[0-9]+".*?>', depen).group()[16:-2]

                    gover_word = re.sub('<.*?>', '', gover)
                    depen_word = re.sub('<.*?>', '', depen)

                    dep_list.append(
                        {'type': type,
                         'gover_num': gover_num,
                         'depen_num': depen_num,
                         'gover_word': gover_word,
                         'depen_word': depen_word})

            ans.append(dep_list)
    return ans


if __name__ == '__main__':
    n = 4
    if len(sys.argv) > 1:
        n = int(sys.argv[1]) - 1
    G = Digraph(format='png')
    G.attr('node', shape='circle')

    dep_list = depnlp('nlp.txt.xml')[n]
    for dep in dep_list:
        G.node(dep['gover_num'], dep['gover_word'])
        G.node(dep['depen_num'], dep['depen_word'])

    for dep in dep_list:
        G.edge(dep['depen_num'], dep['gover_num'], dep['type'])

    G.render('dotnlp')
