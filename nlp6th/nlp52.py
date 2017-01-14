#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp51 import parseWord
import nltk
import re


def word_stem(filename):
    sentence_list = []
    for sentence in parseWord(filename):
        word_list = []
        for word in sentence:
            proto = re.sub('[^a-z]', '', word.lower())
            word_list.append([word, nltk.PorterStemmer().stem(proto)])
        sentence_list.append(word_list)
    return sentence_list


if __name__ == '__main__':
    for sentence in word_stem('nlp.txt'):
        for wordstem in sentence:
            print(wordstem[0] + '\t' + wordstem[1])
