from test_framework import generic_test


def maximum_revenue(coins):
    # note that it's harder to do this in a tabular way
    # due to the order that the subproblems are computed
    n = len(coins)
    dp = [[0]*n for _ in range(n)]

    def compute_coin_range(i, j):
        if i > j:
            return 0
        if dp[i][j] != 0:
            return dp[i][j]
        dp[i][j] = max(
            coins[i] + min(compute_coin_range(i+1, j-1), compute_coin_range(i+2, j)),
            coins[j] + min(compute_coin_range(i+1, j-1), compute_coin_range(i, j-2))
        )
        return dp[i][j]
    return compute_coin_range(0, n-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
