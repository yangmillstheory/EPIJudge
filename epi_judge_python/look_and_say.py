import collections
from test_framework import generic_test

_sentinel = object()


def look_and_say(n):
    res = collections.deque([1, _sentinel])
    for _ in range(1, n):
        count, prev = 0, None
        while res:
            x = res.popleft()
            if prev is None or x == prev:
                count += 1
            else:
                res.append(count)
                res.append(prev)
                count = 1
            if x == _sentinel:
                res.append(_sentinel)
                break
            prev = x
    res.pop()
    return ''.join([str(x) for x in res])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
