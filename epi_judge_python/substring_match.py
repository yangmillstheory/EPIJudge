from functools import reduce
from test_framework import generic_test


def rabin_karp(t, s):
    m, n = len(t), len(s)
    if m < n:
        return -1
    elif m == n:
        return 0 if t == s else -1
    base = 26
    t_hash = reduce(lambda h, ch: base*h + ord(ch), t[:n], 0)
    s_hash = reduce(lambda h, ch: base*h + ord(ch), s, 0)
    for i in range(m-n):
        if t_hash == s_hash and t[i:i+n] == s:
            return i
        t_hash -= pow(base, n-1)*ord(t[i])
        t_hash *= base
        t_hash += ord(t[i+n])
    if t_hash == s_hash and t[m-n:] == s:
        return m-n
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
