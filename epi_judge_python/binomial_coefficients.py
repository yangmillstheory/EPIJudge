from test_framework import generic_test


def n_choose_k_slow(n, k):
    if k == 0 or k == n:
        return 1
    if n == 0:
        return 0
    return n_choose_k_slow(n-1, k-1) + n_choose_k_slow(n-1, k)


def n_choose_k_memo(n, k, memo):
    if k == 0 or k == n:
        return 1
    if n == 0:
        return 0
    n_choose_k = memo.get((n, k))
    if n_choose_k is None:
        n_choose_k = n_choose_k_memo(n-1, k-1, memo) + n_choose_k_memo(n-1, k, memo)
    memo[(n, k)] = n_choose_k
    return n_choose_k


def n_choose_k_dp_1(n, k):
    # T(n,k) = S(n,k) = O(n*k)
    dp = [[None for _ in range(k+1)] for _ in range(n+1)]
    for j in range(k+1):
        dp[0][j] = 0
    for i in range(n+1):
        for j in range(k+1):
            if i == j or j == 0:
                dp[i][j] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[-1][-1]


def n_choose_k_dp_2(n, k):
    if n == 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    prev = [0]*(k+1)
    for i in range(1, n+1):
        curr = [0]*(k+1)
        curr[0] = 1
        for j in range(1, k+1):
            if i == j:
                curr[j] = 1
            else:
                curr[j] = prev[j]+prev[j-1]
        prev = curr
    return prev[-1]


def n_choose_k_dp_3(n, k):
    if n == 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    prev = [0]*(k+1)
    curr = [1]+([0]*k)
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == j:
                curr[j] = 1
            else:
                curr[j] = prev[j]+prev[j-1]
        for j in range(k+1):
            prev[j], curr[j] = curr[j], int(j == 0)
    return prev[-1]


def compute_binomial_coefficient(n, k):
    return n_choose_k_dp_3(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
