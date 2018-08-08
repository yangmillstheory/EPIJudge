from test_framework import generic_test


def justify_text(words, max_len):
    res, curr = [], []
    for w in words:
        len_w_spaces = 0 if not curr else len(curr)-1 + sum(map(len, curr))
        if int(len_w_spaces != 0) + len(w) + len_w_spaces <= max_len:
            curr.append(w)
            continue
        left = max_len - len_w_spaces
        if len(curr) == 1:
            res.append(curr[0] + ' '*left)
        else:
            m, n = divmod(left, len(curr)-1)
            for k in range(n):
                curr[k] += ' '
            res.append((' '*(m+1)).join(curr))
        curr = [w]
    res.append(' '.join(curr) + (' '*(max_len - sum(map(len, curr)) - len(curr) + 1)))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("left_right_justify_text.py",
                                       'left_right_justify_text.tsv',
                                       justify_text))
