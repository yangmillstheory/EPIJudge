import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset_quadratic(text, words):
    n = len(text)
    min_cover = None
    for i in range(n):
        k = 0
        for j in range(i, n):
            if text[j] == words[k]:
                k += 1
            if k == len(words):
                if min_cover is None or j-i < min_cover[1]-min_cover[0]:
                    min_cover = Subarray(i, j)
                break
    return min_cover


def find_smallest_sequentially_covering_subset(text, words):
    w = len(words)
    ind = {word: j for j, word in enumerate(words)}
    memo, min_length, min_cover = [float('inf')] * w, float('inf'), None
    latest = [-1] * w
    for i, word in enumerate(text):
        if word not in ind:
            continue
        j = ind[word]
        latest[j] = i
        if j == 0:
            memo[j] = 1
        elif memo[j-1] is not None:
            memo[j] = i-latest[j-1]+memo[j-1]
        if j == w-1 and memo[-1] < min_length:
            min_length, min_cover = memo[-1], Subarray(i-memo[-1]+1, i)
    return min_cover


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
