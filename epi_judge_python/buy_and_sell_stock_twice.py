import itertools
from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    n = len(prices)
    forward = [0]*n
    min_price, best = float('inf'), 0
    for i, price in enumerate(prices):
        min_price = min(min_price, price)
        best = max(best, price-min_price)
        forward[i] = best
    # don't reset best here, in order to account for a single buy-sell scenario
    max_price = float('-inf')
    for j, price in zip(range(n-1, -1, -1), reversed(prices)):
        if j == 0:
            break
        max_price = max(max_price, price)
        best = max(best, forward[j-1]+max_price-price)
    return best


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
