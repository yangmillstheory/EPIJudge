import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    # T(i,c) = O(i*c)
    # S(i,c) = O(c)
    memo = [0]*(capacity+1)
    for weight, value in items:
        for j in range(capacity, 0, -1):
            memo[j] = max(
                memo[j],
                memo[j-weight]+value if j-weight >= 0 else float('-inf')
            )
    return memo[-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
