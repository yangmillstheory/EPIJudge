from test_framework import generic_test

def intersect_two_sorted_arrays(a, b):
    """Returns the intersection of two sorted lists
    in O(m + n) time.

    """
    m, n = len(a), len(b)
    i = j = 0
    res = []
    while i < m and j < n:
        if a[i] > b[-1] or b[j] > a[-1]:
            break
        elif a[i] == b[j]:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
