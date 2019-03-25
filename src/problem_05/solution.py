"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first
and last element of that pair. For example, car(cons(3, 4)) returns 3,
and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

"""
This isn't a difficult problem but it's a little tricky to handle due to its
functions returns (functional programming?!).

Trying to understand it:
The given 'cons' function receives two parameters (a, b), and returns another 
function that waits as parameter whose handles the two arguments gotten by cons.

Ok, now, we need to implement two functions which take care of cons output.
By the given problem, we can see that car and cdr functions must return 
the first and second arguments of a 2-tuple respectively. I do this with basic
lambda functions.

I'll try to understand better the problem and improve my solution explanation.
Look functional programming could be a good bet.
"""

import unittest

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    return f(lambda x, y: x)


def cdr(f):
    return f(lambda x, y: y)


class Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(car(cons(3, 4)), 3)
        self.assertEqual(cdr(cons(3, 4)), 4)
