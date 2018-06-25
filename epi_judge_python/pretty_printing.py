from test_framework import generic_test


def minimum_messiness(words, length):
    n = len(words)
    n_blanks = length - len(words[0])
    dp = [pow(n_blanks, 2)] + [float('inf') for _ in range(n-1)]
    for j in range(1, n):
        n_blanks = length - len(words[j])
        dp[j] = dp[j-1] + pow(n_blanks, 2)
        for i in range(j-1, -1, -1):
            n_blanks -= len(words[i]) + 1
            if n_blanks < 0:
                break
            dp[j] = min(dp[j], (dp[i-1] if i-1 >= 0 else 0) + pow(n_blanks, 2))
    return dp[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "pretty_printing.py", 'pretty_printing.tsv', minimum_messiness))
