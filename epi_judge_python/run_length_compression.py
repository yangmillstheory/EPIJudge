from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    # T(n) = S(n) = O(n)
    buf, buf_count = [], []
    for ch in s:
        if ch in '0123456789':
            buf_count.append(ch)
        else:
            count = int(''.join(buf_count))
            buf.extend([ch]*count)
            buf_count = []
    return ''.join(buf)


def encoding(s):
    # T(n) = S(n) = O(n)
    buf, count, term = [], 0, '-'
    for i, ch in enumerate(s + term):
        if i == 0 or ch == s[i-1]:
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
