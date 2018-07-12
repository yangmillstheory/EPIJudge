from test_framework import generic_test

to_decimal = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_integer(s):
    # T(n) = O(n)
    # S(n) = O(1)
    res, i, n = 0, 0, len(s)
    while i < n:
        x = s[i]
        p = to_decimal[x]
        if i+1 < n:
            y, q = s[i+1], to_decimal[s[i+1]]
        else:
            y, q = '-', 0
        if (x == 'I' and y in {'V', 'X'}) or \
           (x == 'X' and y in {'L', 'C'}) or \
           (x == 'C' and y in {'D', 'M'}):
            res += q-p
            next_i = i+2
        else:
            res += p
            next_i = i+1
        i = next_i
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
