from test_framework import generic_test


DELIM = '/'


def shortest_equivalent_path(path):
    # T(n) = S(n) = O(n)
    nodes = []
    for node in path.split(DELIM):
        if node == '.' or node == '':
            continue
        if node == '..':
            if not nodes or nodes[-1] == '..':
                nodes.append(node)
            else:
                nodes.pop()
        else:
            nodes.append(node)
    res = DELIM.join(nodes)
    return DELIM+res if path.startswith(DELIM) else res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
