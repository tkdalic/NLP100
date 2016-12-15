#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp30 import mecab_list
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    mecablist = mecab_list('neko.txt.mecab')
    occur = defaultdict(int)
    total = len(mecablist)

    for v in mecablist:
        occur[v['surface']] += 1

    plt.hist(np.array([k for k in sorted(occur.values())]) / total, bins=14)
    plt.title('nlp38.py')
    plt.xlabel('出現頻度')
    plt.ylabel('種類数')
    plt.show()
