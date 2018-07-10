from collections import deque
from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    if x == 0:
        return '0'
    is_neg = x < 0
    buf, x, base = deque(), abs(x), 10
    while x:
        x, rem = divmod(x, base)
        buf.appendleft(str(rem))
    if is_neg:
        buf.appendleft('-')
    return ''.join(buf)


def string_to_int(s):
    if s == '0':
        return 0
    is_neg = s and s[0] == '-'
    if is_neg:
        s = s[1:]
    res, base = 0, 10
    for i, ch in enumerate(reversed(s)):
        res += pow(base, i)*int(ch)
    return -res if is_neg else res


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
