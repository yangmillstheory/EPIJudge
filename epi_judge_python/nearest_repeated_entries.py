from test_framework import generic_test


def find_nearest_repetition(words):
    seen = {}
    # odd choice of default return value
    min_dist = -1
    for j, word in enumerate(words):
        if word in seen:
            if min_dist == -1:
                min_dist = float('inf')
            min_dist = min(min_dist, j-seen[word])
        seen[word] = j
    return min_dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
