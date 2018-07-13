from test_framework import generic_test


def can_reach_end(a):
    n = len(a)
    dp = [True] + [False]*(n-1)
    for j in range(1, n):
        dp[j] = any(dp[i] and i+a[i] >= j for i in range(j-1, -1, -1))
        if not dp[j]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
