from test_framework import generic_test


def longest_contained_range(a):
    '''Find the longest contained range in a list of
    numbers in O(n) time and O(n) space.'''
    max_len = 0
    rem, a = set(a), set(a)
    while rem:
        curr = rem.pop()
        n, l, r = 1, curr-1, curr+1
        while l in a:
            rem.remove(l)
            n, l = n+1, l-1
        while r in a:
            rem.remove(r)
            n, r = n+1, r+1
        max_len = max(max_len, n)
    return max_len


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
