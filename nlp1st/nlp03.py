#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    str = str.replace(',', '').replace('.', '')
    for v in str.split():

        print(len(v), end='')
