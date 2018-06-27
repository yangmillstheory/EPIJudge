from test_framework import generic_test


def majority_search(stream):
    count, last = 0, None
    for x in stream:
        if count == 0:
            last, count = x, 1
        elif last == x:
            count += 1
        else:
            count -= 1
    return last


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
