from collections import Counter
from test_framework import generic_test


def find_all_substrings(string, words):
    res = []
    n_words = len(words)
    if not n_words:
        return res
    n_word = len(words[0])
    orig = set(words)
    n = len(string)
    bad = set()
    for i in range(n-(n_words*n_word)+1):
        if i in bad:
            continue
        rem = Counter(words)
        for j in range(i, n-n_word+1, n_word):
            sub = string[j:j+n_word]
            if sub not in orig:
                bad.add(j)
                break
            if sub in rem:
                rem[sub] -= 1
                if not rem[sub]:
                    del rem[sub]
                if not rem:
                    res.append(i)
                    break
            else:
                break
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
