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
    pass


def decode(s):
    pass


class Tests(unittest.TestCase):
    def test_example(self):
        decoded = 'AAAABBBCCDAA'
        encoded = '4A3B2C1D2A'
        self.assertEqual(encode(decoded), encoded)
        self.assertEqual(decode(encoded), decoded)
