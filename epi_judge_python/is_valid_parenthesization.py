from test_framework import generic_test


def is_well_formed(s):
    '''T(n) = S(n) = O(n)'''
    opens_rem = []
    close_to_open = {'}': '{', ')': '(', ']': '['}
    opens = set(close_to_open.values())
    for ch in s:
        if ch in opens:
            opens_rem.append(ch)
        elif ch in close_to_open:
            if not opens_rem or opens_rem[-1] != close_to_open[ch]:
                return False
            opens_rem.pop()
        else:
            raise ValueError(ch)
    return not opens_rem

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
