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


def phone_mnemonic(s, i=0, cand=None, res=None):
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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
