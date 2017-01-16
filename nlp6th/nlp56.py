#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp53 import corenlp
import re


def depnlp(filename):
    ans = []
    with open(filename) as f:
        sentences = re.search('<coreference>[\s\S]+</coreference>', f.read()).group()
        for token in re.findall('<coreference>[\s\S]+?</coreference>', sentences):

            repre = re.search(
                '<mention representative="true">[\s\S]+?</mention>', token)
            rep_text = re.search(
                '<text>.+</text>', repre.group()).group()[6:-7]

            for dep in re.findall('<mention>[\s\S]+?</mention>', token):

                sentence = re.search(
                    '<sentence>[0-9]+</sentence>', dep).group()[10:-11]
                start = re.search('<start>.*</start>', dep).group()[7:-8]
                end = re.search('<end>.*</end>', dep).group()[5:-6]

                ans.append(
                    {'rep_text': rep_text,
                     'sentence': int(sentence),
                     'start': int(start),
                     'end': int(end)})
    return sorted(ans, key=lambda x: (x['sentence'], x['start'], x['end']))


if __name__ == '__main__':
    dep_list = depnlp('nlp.txt.xml')
    end_list = []
    sentences = []
    for k, sentence in enumerate(corenlp('nlp.txt.xml')):
        sentences.append('')
        for k2, token in enumerate(sentence):
            for dep in dep_list[:]:
                if k + 1 == dep['sentence']:
                    if k2 + 1 == dep['start']:
                        sentences[-1] += '「 ' + \
                            dep_list[dep_list.index(
                                dep)]['rep_text'] + ' ( '
                        end_list.append(dep_list.pop(dep_list.index(dep)))

            for end in end_list[:]:
                if k + 1 == end['sentence']:
                    if k2 + 1 == end['end']:
                        sentences[-1] += ')」 '
                        end_list.pop(end_list.index(end))

            sentences[-1] += token['word'] + ' '

    for sentence in sentences:
        re_sentence = sentence.strip().replace(' ?', '?').replace(
            ' .', '.').replace(' ,', ',').replace(' :', ':').replace('-LRB- ', '(').replace(' -RRB-', ')')
        print(re_sentence)
