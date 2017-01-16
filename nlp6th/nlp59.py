#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re


def nest_match(sentence):
    nest = 0
    for k, char in enumerate(sentence):
        if char == '(':
            nest += 1
        elif char == ')':
            nest -= 1
            if nest == 0:
                return sentence[:k]


def parsenlp(filename):
    with open(filename) as f:
        for sentence in re.findall('<parse>.+</parse>', f.read()):
            for v in re.finditer('\(NP', sentence):
                yield re.sub('\)|\([^ ]+?\s', '',
                             nest_match(sentence[v.start():]))


if __name__ == '__main__':
    for phrase in parsenlp('nlp.txt.xml'):
        print(phrase.replace('-LRB- ', '(').replace(' -RRB-', ')'))
