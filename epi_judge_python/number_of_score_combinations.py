from test_framework import generic_test


def num_combinations_for_final_score(score, plays):
    # T(a, c) = O(a*c)
    # S(a, c) = O(c)
    if score == 0:
        return 1
    if not plays:
        return 0
    n_plays = len(plays)
    prev = [1]+([0]*score)
    curr, init = [1]+([0]*score), True
    for i in range(n_plays):
        if not init:
            curr = [1]+([0]*score)
        for j in range(1, score+1):
            incl_c_i = curr[j-plays[i]] if j-plays[i] >= 0 else 0
            excl_c_i = prev[j] if i-1 >= 0 else 0
            curr[j] = incl_c_i+excl_c_i
        prev, init = curr, False
    return curr[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
