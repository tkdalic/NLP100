#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re


def parsenlp(filename):
    with open(filename) as f:
        for sentence in re.findall('<parse>[\s\S]+?</parse>', f.read()):
            print(sentence)
            for v in re.findall('\(NP.+\)', sentence):
                print(v)


if __name__ == '__main__':
    parsenlp('nlp.txt.xml')
