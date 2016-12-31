#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp53 import corenlp


if __name__ == '__main__':
    for sentence in corenlp('nlp.txt.xml'):
        for token in sentence:
            if token['NER'] == 'PERSON':
                print(token['word'])
