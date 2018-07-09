from test_framework import generic_test


def is_palindrome(string):
    n = len(string)
    i, j = 0, n-1
    while True:
        while i < n and not string[i].isalnum():
            i += 1
        while j >= 0 and not string[j].isalnum():
            j -= 1
        if i > j or i > n or j < 0:
            break
        elif string[i].lower() != string[j].lower():
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
