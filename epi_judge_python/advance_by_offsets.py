from test_framework import generic_test


def dp_1(a):
    # T(n) = O(n^2)
    # S(n) = O(n)
    n = len(a)
    dp = [True] + [False]*(n-1)
    for j in range(1, n):
        dp[j] = any(dp[i] and i+a[i] >= j for i in range(j-1, -1, -1))
        if not dp[j]:
            return False
    return True


def can_reach_end(a):
    best = float('-inf')
    for i, jump in enumerate(a):
        if i > best:
            return False
        if i+jump >= len(a)-1:
            return True
        best = max(best, i+jump)
    return best >= len(a)-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
