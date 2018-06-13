from test_framework import generic_test


def ch_index(ch):
    return ord(ch)-ord('a')


def can_form_palindrome(s):
    '''Check if you can permute a string to be a palindrome.

        T(n) = O(n)
        S(n) = O(1)
    '''
    ch_counts = [0 for _ in range(ch_index('z')+1)]
    n_odd = 0
    for ch in s:
        j = ch_index(ch)
        if ch_counts[j] % 2:
            n_odd -= 1
        else:
            n_odd += 1
        ch_counts[j] += 1
    return n_odd > 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
