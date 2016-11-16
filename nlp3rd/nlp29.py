#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp28 import infobox4
import requests
import json


if __name__ == '__main__':
    ans = infobox4()
    print(json.loads(requests.get(
        'https://ja.wikipedia.org/w/api.php?action=query&prop=imageinfo&format=json&iiprop=url&titles=Image:' + ans['国旗画像']).text)['query']['pages']['-1']['imageinfo'][0]['url'])
