#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp50 import parseSentence


def parseWord(filename):
    ans = []
    for sentence in parseSentence(filename):
        ans.append(sentence.split(' '))
    return ans


if __name__ == '__main__':
    for v in parseWord('nlp.txt'):
        for v2 in v:
            print(v2)
        print()
