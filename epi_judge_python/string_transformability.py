import collections
from test_framework import generic_test


def transform_string(words, s, t):
    alpha = {ch for word in words for ch in word}
    q, seen = collections.deque([(s, 0)]), set()
    while q:
        v, n = q.popleft()
        if v == t:
            return n
        chars = list(v)
        for i, ch in enumerate(v):
            for _ch in alpha:
                chars[i] = _ch
                u = ''.join(chars)
                if u in words and u not in seen and u != v:
                    q.append((u, n+1))
                seen.add(u)
            chars[i] = ch
        seen.add(v)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
