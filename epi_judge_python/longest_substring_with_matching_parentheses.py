from test_framework import generic_test


def shitty_quad_time_algo(s):
    n, best = len(s), 0
    for i in range(n):
        n_open = 0
        for j in range(i, n):
            if s[j] == '(':
                n_open += 1
            elif n_open:
                n_open -= 1
            else:
                break
            if n_open == 0:
                best = max(best, j-i+1)
    return best


def longest_matching_parentheses(s):
    '''Returns the length of the longest substring with matched
    parentheses in O(n) time and O(n) space.

    :param s: a string consisting of '(' and ')'
    :returns: non-negative int
    '''
    best, left = 0, -1
    o = []
    for j, ch in enumerate(s):
        if ch == '(':
            o.append(j)
        elif o:
            o.pop()
            i = o[-1] if o else left
            best = max(best, j-i)
        else:
            left = j
    return best


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_substring_with_matching_parentheses.py",
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
