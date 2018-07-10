from collections import deque
from test_framework import generic_test


def to_base_10(s, b):
    '''Convert a string in base b <= 16 to a base 10 integer.'''
    res = 0
    for i, c in enumerate(reversed(s)):
        res += pow(b, i)*(int(c) if c.isdigit() else ord(c)-ord('A')+10)
    return res


def from_base_10(x, b):
    buf = deque()
    while x:
        x, rem = divmod(x, b)
        buf.appendleft(str(rem) if rem < 10 else chr(ord('A')+rem-10))
        if x == -1:
            break
    return ''.join(buf)


def convert_base(s, b1, b2):
    is_neg = s and s[0] == '-'
    if is_neg:
        s = s[1:]
    if s == '0':
        res = '0'
    else:
        res = from_base_10(to_base_10(s, b1), b2)
    return '-' + res if is_neg else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
