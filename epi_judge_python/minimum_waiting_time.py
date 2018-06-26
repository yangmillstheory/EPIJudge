from test_framework import generic_test


def minimum_total_waiting_time(service_times):
    service_times.sort()
    res, n = 0, len(service_times)
    for j, service_time in enumerate(service_times, 1):
        res += (n-j) * service_time
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
