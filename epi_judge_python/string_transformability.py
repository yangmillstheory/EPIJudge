import collections
from test_framework import generic_test


def transform_string(words, s, t):
    def get_alpha():
        alpha = collections.defaultdict(set)
        for word in words:
            for i, ch in enumerate(word):
                alpha[i].add(ch)
        return alpha
    alpha = get_alpha()
    q, seen = collections.deque([(s, 0)]), set()
    while q:
        v, n = q.popleft()
        if v == t:
            return n
        if v in seen:
            continue
        chars = list(v)
        for i, ch in enumerate(v):
            for _ch in alpha[i]:
                chars[i] = _ch
                u = ''.join(chars)
                if u in words and u not in seen and u != v:
                    q.append((u, n+1))
            chars[i] = ch
        seen.add(v)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
