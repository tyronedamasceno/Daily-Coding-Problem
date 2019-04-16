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
    def _find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr==ch]
    lines = []
    cur_line = []
    for word in inp_list:
        if not len(cur_line):
            cur_line = list(word)
        elif len(cur_line) + len(word) + 1 <= k:
            cur_line.extend([' '] + list(word))
        else:
            lines.append(cur_line)
            cur_line = list(word)
    if cur_line:
        lines.append(cur_line)

    for line in lines:
        missing = k - len(line)
        spaces = line.count(' ')
        n, r = divmod(missing, spaces)
        r = spaces - r
        if missing:
            if spaces:
                spaces_idx = _find(line, ' ')
                for i in spaces_idx[::-1]:
                    if r:
                        r -= 1
                    else:
                        line.insert(i, ' ')
                    line.insert(i, n*' ')
            else:
                line = [' ']*missing + line

    return [''.join(line) for line in lines]


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
