from test_framework import generic_test


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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
