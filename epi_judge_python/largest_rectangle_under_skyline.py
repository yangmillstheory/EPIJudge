from collections import namedtuple
from test_framework import generic_test

Pillar = namedtuple('Pillar', ['i', 'h'])


def calculate_largest_rectangle(hs):
    pillars, res = [], 0
    for i, h in enumerate(hs + [0]):
        while pillars and pillars[-1].h > h:
            _i, _h = pillars.pop()
            if pillars:
                w = i - pillars[-1].i - 1
            else:
                w = i
            res = max(res, w*_h)
        pillars.append(Pillar(i, h))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
