"""
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be
smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

import unittest

class LogBuffer:
    def __init__(self, N):
        self.N = N
        self.buffer = ['']*N
        self.cur = 0

    def record(self, order_id):
        self.buffer[self.cur] = order_id
        self.cur += 1
        self.cur %= self.N

    def get_last(self, i):
        x = (self.cur - i + self.N) % self.N
        return self.buffer[x]


class Tests(unittest.TestCase):
    def test_example(self):
        log = LogBuffer(3)
        for i in range(6):
            log.record(i)
        self.assertEqual(log.get_last(1), 5)
        self.assertEqual(log.get_last(2), 4)
        self.assertEqual(log.get_last(3), 3)
