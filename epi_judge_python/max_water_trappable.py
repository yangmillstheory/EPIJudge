from test_framework import generic_test


def calculate_trapping_water(hs):
    # return _brute_force(hs)
    return _dp(hs)


def _dp(hs):
    # T(n) = S(n) = O(n)
    n, res = len(hs), 0
    l_heights = [hs[0]] + [float('-inf') for _ in range(n-1)]
    r_heights = [float('-inf') for _ in range(n-1)] + [hs[-1]]
    for i in range(1, n):
        if hs[i] < l_heights[i-1]:
            l_heights[i] = l_heights[i-1]
        elif hs[i] < hs[i-1]:
            l_heights[i] = hs[i-1]
    for i in range(n-2, -1, -1):
        if hs[i] < r_heights[i+1]:
            r_heights[i] = r_heights[i+1]
        elif hs[i] < hs[i+1]:
            r_heights[i] = hs[i+1]
    for i in range(1, n-1):
        l_height, r_height = l_heights[i], r_heights[i]
        if r_height != float('-inf') and l_height != float('-inf'):
            res += min(r_height, l_height)-hs[i]
    return res


def _brute_force(hs):
    # T(n) = O(n^2)
    # S(n) = O(1)
    res, n = 0, len(hs)
    for i in range(1, n-1):
        r_height, l_height = float('-inf'), float('-inf')
        for j in range(i, n):
            if hs[j] > hs[i]:
                r_height = max(r_height, hs[j])
        for j in range(i):
            if hs[j] > hs[i]:
                l_height = max(l_height, hs[j])
        if r_height != float('-inf') and l_height != float('-inf'):
            res += min(r_height, l_height)-hs[i]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_water_trappable.py",
                                       'max_water_trappable.tsv',
                                       calculate_trapping_water))
