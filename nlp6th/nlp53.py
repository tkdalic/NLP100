#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re


def corenlp(filename):
    ans = []
    with open(filename) as f:
        for sentence in re.findall('<sentence id[\s\S]+?</sentence>', f.read()):
            sentence_list = []
            for token in re.findall('<token id[\s\S]+?</token>', sentence):
                token_dic = {}
                id = re.search('"[0-9]+"', token).group()[1:-1]
                token_dic['id'] = id
                for tag in re.findall('<.+?>.*</.+?>', token):
                    key = re.search('<.+?>', tag).group()[1:-1]
                    val = re.search('>.+?<', tag).group()[1:-1]
                    token_dic[key] = val
                sentence_list.append(token_dic)
            ans.append(sentence_list)
    return ans


if __name__ == '__main__':
    for sentence in corenlp('nlp.txt.xml'):
        for token in sentence:
            print(token['word'])
