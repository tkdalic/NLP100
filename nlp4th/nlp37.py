#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp30 import mecab_list
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    mecablist = mecab_list('neko.txt.mecab')
    ans = defaultdict(int)
    total = len(mecablist)

    for v in mecablist:
        ans[v['surface']] += 1

    bestten = sorted(ans.items(), key=lambda k: k[
        1], reverse=True)[:10]

    plt.bar(np.array(range(10)), np.array(
        [v[1] / total for v in bestten]), tick_label=[v[0] for v in bestten], align='center')
    plt.title('nlp37.py')
    plt.xlabel('出現順位')
    plt.ylabel('出現頻度')
    plt.show()
