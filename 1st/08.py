#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    str = input('plase input >> ')

    for v in str:
        code = int.from_bytes(v.encode('utf-8'), 'big')
        if code > 0x61 and code < 0x7A:
            print((219 - code).to_bytes(1, 'little').decode('utf-8', 'ignore'), end='')
        else:
            print(v, end='')
