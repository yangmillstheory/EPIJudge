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
    best, end = 0, -1
    stack = []
    for j, ch in enumerate(s):
        if ch == '(':
            stack.append(j)
        elif stack:
            stack.pop()
            start = stack[-1] if stack else end
            best = max(best, j-start)
        else:
            end = j
    return best


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_substring_with_matching_parentheses.py",
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
