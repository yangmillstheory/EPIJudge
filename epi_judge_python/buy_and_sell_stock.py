from test_framework import generic_test


def find_maximum_subarray(a):
    prev, max_seen = 0, float('-inf')
    for x in a:
        prev = max(prev+x, x)
        max_seen = max(prev, max_seen)
    return max(max_seen, 0)


def buy_and_sell_stock_once(prices):
    return find_maximum_subarray((prices[i]-prices[i-1] for i in range(1, len(prices))))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
