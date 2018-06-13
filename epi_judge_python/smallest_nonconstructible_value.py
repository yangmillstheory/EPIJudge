from test_framework import generic_test


def smallest_nonconstructible_value(xs):
    '''Finds the smallest poz. integer that's not
    a subset sum of xs. xs is assumed to be sorted.

    O(n) time
    O(1) space
    '''
    xs.sort()
    out = 1
    for x in xs:
        if x <= out:
            out += x
        else:
            break
    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
