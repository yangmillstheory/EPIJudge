from test_framework import generic_test


def find_biggest_n_minus_one_product(a):
    n = len(a)
    suf = [1]*n
    for j in range(n-2, -1, -1):
        suf[j] = suf[j+1]*a[j+1]
    pre, res = 1, 0
    for i, x in enumerate(a):
        res = max(res, pre*suf[i])
        pre *= x
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_product_all_but_one.py",
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
