from test_framework import generic_test


def _search_recursive(cands, k, lo, hi):
    # T(n) = S(n) = O(log n)
    if lo > hi:
        return -1
    mid = lo + (hi-lo)//2
    if cands[mid] == k:
        if mid == 0 or cands[mid-1] != k:
            return mid
        return _search_recursive(cands, k, lo, mid-1)
    elif cands[mid] < k:
        return _search_recursive(cands, k, mid+1, hi)
    else:
        return _search_recursive(cands, k, lo, mid-1)


def _search_iterative(cands, k):
    lo, hi = 0, len(cands)-1
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if cands[mid] == k:
            if mid == 0 or cands[mid-1] != k:
                return mid
            hi = mid-1
        elif cands[mid] < k:
            lo = mid+1
        else:
            hi = mid-1
    return -1


def search_first_of_k(cands, k):
    # return _search_recursive(cands, k, 0, len(cands)-1)
    return _search_iterative(cands, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
