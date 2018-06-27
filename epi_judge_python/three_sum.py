import bisect
from test_framework import generic_test


def has_three_sum_slow(xs, t):
    # T(n) = O(n^2 * log n)
    # S(n) = O(n^2)
    rems = set([t-x-y for x in xs for y in xs])
    xs.sort()
    for rem in rems:
        j = bisect.bisect_left(xs, rem)
        if j < len(xs) and xs[j] == rem:
            return True
    return False


def has_two_sum(xs, t):
    # T(n) = O(n)
    i, j = 0, len(xs)-1
    while i <= j:
        trial = xs[i]+xs[j]
        if trial < t:
            i += 1
        elif trial > t:
            j -= 1
        else:
            return True
    return False


def has_three_sum(xs, t):
    # T(n) = O(n^2)
    xs.sort()
    return any(has_two_sum(xs, t-x) for x in xs)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
