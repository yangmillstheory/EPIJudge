from test_framework import generic_test


ops = {'+', '-', '/', '*'}


def signum(x):
    return -1 if x < 0 else 1


def evaluate(tokens):
    # T(n) = S(n) = O(n)
    tokens = tokens.split(',')
    nums = []
    for ch in tokens:
        if ch not in ops:
            nums.append(int(ch))
            continue
        b, a = nums.pop(), nums.pop()
        if ch == '+':
            c = a+b
        elif ch == '-':
            c = a-b
        elif ch == '/':
            c = signum(a)*signum(b)*(abs(a)//abs(b))
        elif ch == '*':
            c = a*b
        else:
            raise ValueError(ch)
        nums.append(c)
    return nums.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
