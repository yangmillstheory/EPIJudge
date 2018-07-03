from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self._maxes = []
        self._stack = []

    def empty(self):
        return not self._stack

    def max(self):
        if not self._maxes:
            raise RuntimeError('no max. values; stack is empty')
        return self._maxes[-1]

    def pop(self):
        x = self._stack.pop()
        if self._maxes and self._maxes[-1] == x:
            self._maxes.pop()
        return x

    def push(self, x):
        _max = self._maxes[-1] if self._maxes else float('-inf')
        if x >= _max:
            self._maxes.append(x)
        self._stack.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
