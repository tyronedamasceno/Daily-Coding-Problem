"""
Implement an autocomplete system. That is, given a query string s and a set of
all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to
speed up queries.
"""

from collections import defaultdict
import unittest

def prepare(initial_dict):
    output = defaultdict(set)
    for word in initial_dict:
        for i in range(len(word)):
            output[word[:i+1]].add(word)
    return output


def get_words(pref, prepared_data):
    return prepared_data[pref]


class Tests(unittest.TestCase):
    def test_example(self):
        initial_dict = ['dog', 'deer', 'deal']
        prepared_data = prepare(initial_dict)
        ans = get_words('de', prepared_data)
        self.assertIn('deer', ans)
        self.assertIn('deal', ans)
        self.assertNotIn('dog', ans)
