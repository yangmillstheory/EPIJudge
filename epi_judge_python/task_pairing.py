import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
    # T(n) = O(n*log n)
    n = len(task_durations)
    assert n % 2 == 0
    task_durations.sort()
    return [
        PairedTasks(task_durations[i], task_durations[n-1-i])
        for i in range(n//2)
    ]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
                                       optimum_task_assignment))
