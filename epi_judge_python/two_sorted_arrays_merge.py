from test_framework import generic_test


def merge_two_sorted_arrays(a, m, b, n):
    k = m-1
    for i in range(m+n-1, n-1, -1):
        a[i] = a[k]
        k -= 1
    for j in range(n):
        a[j] = b[j]
    i = n
    j = 0
    for k in range(m+n):
        if i == m+n:
            a[k] = b[j]
            j += 1
        elif j == n:
            a[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            a[k] = a[i]
            i += 1
        else:
            a[k] = b[j]
            j += 1
        k += 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
