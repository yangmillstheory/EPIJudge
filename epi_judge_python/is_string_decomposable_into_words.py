import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def _walk(s, words, start, used, seen):
    if start == len(s):
        return True, used
    if start in seen:
        return False, used
    for i in range(start+1, len(s)+1):
        if i in seen:
            continue
        sub = s[start:i]
        if sub in words:
            used.append(sub)
            if _walk(s, words, i, used, seen)[0]:
                return True, used
            used.pop()
    seen.add(start)
    return False, used


def decompose_into_dictionary_words_recursion(s, words):
    ok, used = _walk(s, words, 0, [], set())
    if ok:
        return used
    return False


def decompose_into_dictionary_words(s, words):
    # really tough to grok O(n^3)/O(n) solution
    n = len(s)
    rev_len = [None]*n
    for j in range(1, n+1):
        if s[:j] in words:
            rev_len[j-1] = j-1
        if rev_len[j-1] is None:
            for i in range(j-1):
                if rev_len[i] is not None and s[i+1:j] in words:
                    rev_len[j-1] = j-1-i-1
    if rev_len[-1] is None:
        return False
    decomp = []
    j = n-1
    while j >= 0:
        if rev_len[j] is not None:
            decomp.append(s[j-rev_len[j]:j+1])
            j -= rev_len[j]+1
    return decomp[::-1]


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
