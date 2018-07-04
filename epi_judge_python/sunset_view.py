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


def examine_buildings_with_sunset(*args):
    return _quadratic_time_slow(*args)


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
