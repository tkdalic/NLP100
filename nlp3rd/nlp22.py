#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-
from nlp21 import categorier

if __name__ == '__main__':
    category = categorier('jawiki-country.json', 'title', 'イギリス')
    for v in category:
        print(v.lstrip('[[Category:').rstrip('|*]]'))
