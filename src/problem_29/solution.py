"""
Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid
"""

import unittest


def encode(s):
    ans = ''
    cur = s[0]
    counter = 1
    for l in s[1:]:
        if l == cur:
            counter += 1
        else:
            ans += (str(counter)+cur)
            cur = l
            counter = 1
    ans += (str(counter)+cur)
    return ans


def decode(s):
    ans = ''
    counter = 0
    for l in s:
        if l.isalpha():
            ans += (counter*l)
            counter = 0
        else:
            counter *= 10
            counter += int(l)
    return ans


class Tests(unittest.TestCase):
    def test_example(self):
        decoded = 'AAAABBBCCDAA'
        encoded = '4A3B2C1D2A'
        self.assertEqual(encode(decoded), encoded)
        self.assertEqual(decode(encoded), decoded)

    def test_counter_bigger_than_10(self):
        decoded = 'AAAAAAAAAAA'
        encoded = '11A'
        self.assertEqual(encode(decoded), encoded)
        self.assertEqual(decode(encoded), decoded)
