from test_framework import generic_test


DELIM = '/'


def append_if_nonempty(l, x):
    if x:
        l.append(x)


def shortest_equivalent_path(path):
    # T(n) = S(n) = O(n)
    nodes, cur = [], ''
    i, n = 0, len(path)
    while i < n:
        ch = path[i]
        if ch == DELIM:
            # eat up the extra delimiters
            j = i
            while j < n and path[j] == DELIM:
                j += 1
            append_if_nonempty(nodes, cur)
            cur, i = '', j
        else:
            cur += ch
            i += 1
    append_if_nonempty(nodes, cur)
    res = []
    for node in nodes:
        if node == '..':
            if res and res[-1] != '..':
                res.pop()
            else:
                res.append(node)
        elif node != '.':
            res.append(node)
    res = DELIM.join(res)
    return DELIM+res if path.startswith(DELIM) else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
