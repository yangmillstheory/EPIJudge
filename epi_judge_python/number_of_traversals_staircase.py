from test_framework import generic_test


def number_of_ways_to_top(top, steps):
    # T(n,k) = O(n*k)
    # S(n,k) = O(n)
    dp = [1]+([0]*top)
    for j in range(1, top+1):
        dp[j] = sum(dp[j-i] if j-i >= 0 else 0 for i in range(1, steps+1))
    return dp[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
