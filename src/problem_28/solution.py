"""
Write an algorithm to justify text. Given a sequence of words and an integer
line length k, return a list of strings which represents each line, fully
justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when
necessary so that each line has exactly length k. Spaces should be distributed
as equally as possible, with the extra spaces, if any, distributed starting
from the left.

If you can only fit one word on a line, then you should pad the right-hand
side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

import unittest


def solve(inp_list, k):
    ans = []
    cur_line = []
    for word in inp_list:
        if not len(cur_line):
            cur_line = list(word)
        elif len(cur_line) + len(word) + 1 <= k:
            cur_line.extend([' '] + list(word))
        else:
            ans.append(cur_line)
            cur_line = list(word)
    if cur_line:
        ans.append(cur_line)
    return [''.join(line) for line in ans]


class Tests(unittest.TestCase):
    def test_example(self):
        l = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        k = 16
        ans = solve(l, k)
        expected = [
            "the  quick brown",
            "fox  jumps  over",
            "the   lazy   dog"
        ]
        self.assertEqual(ans, expected)
