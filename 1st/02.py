#!/Users/rikutakada/.pyenv/shims python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    str1 = 'パトカー'
    str2 = 'タクシー'
    ans = ''

    for a, b in zip(str1, str2):
        ans += a + b
    print(ans)
