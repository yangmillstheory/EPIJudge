from contextlib import contextmanager
from test_framework import generic_test


@contextmanager
def candidate(cand, sub):
    cand.append(sub)
    yield
    cand.pop()


def get_valid_ip_address(s):
    def is_octet(t):
        if not t:
            return False
        if len(t) > 1 and t[0] == '0':
            return False
        return 0 <= int(t) <= 255

    res, cand = [], []
    for i in range(1, 4):
        sub = s[:i]
        if is_octet(sub):
            with candidate(cand, sub):
                for j in range(i+1, i+4):
                    sub = s[i:j]
                    if is_octet(sub):
                        with candidate(cand, sub):
                            for k in range(j+1, len(s)):
                                sub1, sub2 = s[j:k], s[k:]
                                if is_octet(sub1) and is_octet(sub2):
                                    with candidate(cand, sub1), candidate(cand, sub2):
                                        res.append('.'.join(cand))
                                else:
                                    break
                    else:
                        break
        else:
            break
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
