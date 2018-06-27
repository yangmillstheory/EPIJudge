from test_framework import generic_test


def flip_color(x, y, image):
    orig = image[x][y]

    def can_visit(i, j):
        return 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == orig

    def dfs(i, j):
        image[i][j] = not orig
        for p, q in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
            if can_visit(p, q):
                dfs(p, q)
    dfs(x, y)


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
