from test_framework import generic_test


def _quadratic_time_slow(bs):
    # T(n) = O(n^2)
    # S(n) = O(n)
    n = len(bs)
    res = set(range(n))
    for i in range(n):
        for j in range(i+1, n):
            if bs[i] <= bs[j]:
                res.remove(i)
                break
    res = list(res)
    res.reverse()
    return res


def examine_buildings_with_sunset(bs):
    # T(n) = S(n) = O(n)
    n, cands = len(bs), []
    for i, h in enumerate(bs):
        if i == n-1 or bs[i+1] < h:
            while cands and bs[cands[-1]] <= h:
                cands.pop()
            cands.append(i)
    cands.reverse()
    return cands


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
