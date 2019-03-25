"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

import unittest

def solve(msg): 
    letters = [chr(x) for x in range(96, 123)] 
    numbers = [str(x) for x in range(1, 27)] 
    q = [(0, '')] 
    xx = [] 
    while q: 
        p, s = q.pop(0) 
        if p < len(msg) and msg[p] in numbers: 
            q.append((p+1, s+letters[int(msg[p])])) 
            if p == len(msg) - 1:   
                xx.append(q[-1][1]) 
        if p < len(msg)-1 and msg[p:p+2] in numbers: 
            q.append(((p+2), s+letters[int(msg[p:p+2])])) 
            if p == len(msg) - 2: 
                xx.append(q[-1][1]) 
    return len(xx) 



class Tests(unittest.TestCase):
    def test_example(self):
        ans = solve('111')
        self.assertEqual(ans, 3)

    def test_with_1111(self):
        """1111 can be converted in 'aaaa', 'kaa', 'aka', 'aak', 'kk'"""
        ans = solve('1111')
        self.assertEqual(ans, 5)

    def test_with_zeroes(self):
        ans = solve('10203')
        self.assertEqual(ans, 1)
