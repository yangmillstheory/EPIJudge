from test_framework import generic_test


def rotate_matrix(g):
    '''In-place rotation of a matrix in O(n^2) time.'''
    n = len(g)
    if not n:
        return
    for d in range(n//2):
        for k in range(n-1-(2*d)):
            t1 = g[d+k][-d-1]
            t2 = g[-d-1][-d-1-k]
            t3 = g[-d-1-k][d]
            t4 = g[d][d+k]
            g[d+k][-d-1] = t4
            g[-d-1][-d-1-k] = t1
            g[-d-1-k][d] = t2
            g[d][d+k] = t3


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
