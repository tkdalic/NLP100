#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
import re
import json
from nlp20 import articler


if __name__ == '__main__':
    jsons = articler('jawiki-country.json', 'title', 'イギリス')
    ans = []
    for v in json.loads(jsons)['text'].split('\n'):
        a = re.compile("(File|ファイル):.*\.(jpg|JPG|png|PNG|JPEG|jpeg|svg)")
        if a.search(v):
            appen = a.search(v).group().lstrip(
                'File:').lstrip('ファイル:')
            ans.append(appen)
    for k in [a.search(v).group().lstrip('File:').lstrip('ファイル:')
              for v in json.loads(jsons)['text'].split('\n')
              if re.compile("(File|ファイル):.*\.(jpg|JPG|png|PNG|JPEG|jpeg|svg)")
              .search(v)]:
        print(k)
