#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re


def parseSentence(filename):
    ans = []
    with open(filename) as f:
        for row in f.readlines():
            row = row.rstrip()
            for matched in re.findall('[.;:!]\s[A-Z]', row[:-1])[::-1]:
                row = row.replace(matched, re.sub('\s', '\n', matched))
            ans.extend(row.split('\n'))
    return ans


if __name__ == '__main__':
    for v in parseSentence('nlp.txt'):
        print(v)
