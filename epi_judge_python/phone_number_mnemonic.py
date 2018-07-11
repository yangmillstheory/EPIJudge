from collections import deque
from test_framework import generic_test, test_utils


keypad = {
    '0': '0',
    '1': '1',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
}


def _recursive(s, i, cand, res):
    # T(n) = O(n*4^n)
    # S(n) = O(n)
    if res is None:
        res = []
    if cand is None:
        cand = []
    if i == len(s):
        res.append(''.join(cand))
    else:
        for ch in keypad[s[i]]:
            cand.append(ch)
            phone_mnemonic(s, i+1, cand, res)
            cand.pop()
    return res


def compute(s):
    def from_base_10(x, b):
        '''Convert a poz. base 10 integer to a base b string.'''
        buf = deque()
        while x:
            x, rem = divmod(x, b)
            buf.appendleft(str(rem))
        return ''.join(buf)

    # note that this requires the keypad values to be constrained to 3 possible values
    base, res, n = 3, [], len(s)
    for i in range(pow(base, n)):
        x = from_base_10(i, base)
        x = x.zfill(n)
        res.append(''.join([keypad[s[i]][int(d)] for i, d in enumerate(x)]))
    return res


def phone_mnemonic(s):
    return _recursive(s, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
