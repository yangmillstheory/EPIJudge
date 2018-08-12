import operator
import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Rectangle = collections.namedtuple('Rectangle', ('left', 'right', 'height'))


def compute_skyline(a):
    min_l = min(a, key=operator.attrgetter('left')).left
    max_r = max(a, key=operator.attrgetter('right')).right
    h = [0]*(max_r - min_l + 1)
    for l, r, _h in a:
        for i in range(l, r+1):
            h[i-min_l] = max(h[i-min_l], _h)
    sl = []
    left = 0
    for i, _h in enumerate(h):
        if i and _h != h[i-1]:
            sl.append(Rectangle(min_l+left, min_l+i-1, h[i-1]))
            left = i
    sl.append(Rectangle(min_l+left, max_r, h[-1]))
    return sl


@enable_executor_hook
def compute_skyline_wrapper(executor, buildings):
    buildings = [Rectangle(*x) for x in buildings]

    result = executor.run(functools.partial(compute_skyline, buildings))

    return [(x.left, x.right, x.height) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("drawing_skyline.py",
                                       'drawing_skyline.tsv',
                                       compute_skyline_wrapper))
