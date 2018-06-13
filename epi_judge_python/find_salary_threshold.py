from test_framework import generic_test


def find_salary_cap(t, xs):
    xs.sort()
    n = len(xs)
    raw = 0
    for j, x in enumerate(xs):
        adj = (n-j)*x
        if raw + adj >= t:
            return (t-raw)/(n-j)
        raw += x
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
