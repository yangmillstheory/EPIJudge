from test_framework import generic_test


n_chars = ord('Z')-ord('A')+1


def ss_decode_col_id(s):
    col_id = 0
    for i, ch in enumerate(reversed(s)):
        c = ord(ch)-ord('A')+1
        col_id += c*pow(n_chars, i)
    return col_id


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
