from test_framework import generic_test


def minimum_path_weight(tri):
    # T(m,n) = O(m*n)
    # S(m,n) = O(n)
    if not tri:
        return 0
    m, prev = len(tri), [tri[0][0]]
    for i in range(1, m):
        n = len(tri[i])
        curr = [None]*n
        for j in range(n):
            cand = []
            if j > 0:
                cand.append(tri[i][j]+prev[j-1])
            if j < n-1:
                cand.append(tri[i][j]+prev[j])
            curr[j] = min(cand)
        prev = curr
    return min(prev)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_weight_path_in_a_triangle.py",
                                       'minimum_weight_path_in_a_triangle.tsv',
                                       minimum_path_weight))
