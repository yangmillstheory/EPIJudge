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


def decompose_into_dictionary_words(s, words):
    ok, used = _walk(s, words, 0, [], set())
    if ok:
        return used
    return False


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
