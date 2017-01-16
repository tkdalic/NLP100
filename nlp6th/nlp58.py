#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp57 import depnlp
from itertools import product

if __name__ == '__main__':
    for sentence in depnlp('nlp.txt.xml'):
        nsu_list = []
        dob_list = []
        for dep in sentence:
            if dep['type'] == 'nsubj':
                nsu_list.append(dep)
            elif dep['type'] == 'dobj':
                dob_list.append(dep)
        for nsu, dob in product(nsu_list, dob_list):
            if nsu['gover_num'] == dob['gover_num']:
                print('{0}\t{1}\t{2}'.format(
                    nsu['depen_word'], nsu['gover_word'], dob['depen_word']))
