from test_framework import generic_test


def generate_pascal_triangle(n):
    if not n:
        return []
    tri = [[1]]
    prev = tri[-1]
    for i in range(1, n):
        curr = [None]*(i+1)
        for j in range(i+1):
            entry = 0
            if j:
                entry += prev[j-1]
            if j < len(prev):
                entry += prev[j]
            curr[j] = entry
        tri.append(curr)
        prev = curr
    return tri


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
