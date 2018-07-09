from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    # T(n) = S(n) = O(n)
    buf, count = [], 0
    for ch in s:
        if ch in '0123456789':
            count *= 10
            count += int(ch)
        else:
            buf.extend([ch]*count)
            count = 0
    return ''.join(buf)


def encoding(s):
    # T(n) = S(n) = O(n)
    n, buf, count = len(s), [], 0
    for i in range(n+1):
        if i == 0 or (i < n and s[i] == s[i-1]):
            count += 1
        else:
            buf.append(str(count))
            buf.append(s[i-1])
            count = 1
    return ''.join(buf)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
