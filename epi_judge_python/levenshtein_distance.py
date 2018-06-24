from test_framework import generic_test


def levenshtein_distance(a, b):
    # T(m,n) = S(m,n) = O(m*n)
    m, n = len(a), len(b)
    dp = [[None]*(n+1) for _ in range(m+1)]
    for j in range(n+1):
        dp[0][j] = j
    for i in range(m+1):
        dp[i][0] = i
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = min(
                dp[i-1][j-1]+int(a[i-1] != b[j-1]),
                dp[i-1][j] + 1,
                dp[i][j-1] + 1,
            )
    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
