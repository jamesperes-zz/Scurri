import unittest

from postcode import *

class PostCodeTest(unittest.TestCase):

    def test_tree_last_digits_missing_one(self):
        self.assertFalse(check_format('QWE QW'))

    def test_tree_last_digits_sequence_wrong(self):
        self.assertFalse(check_format('QWE QW1'))

    def test_tree_last_digits_correct(self):
        self.assertEqual(check_format('QWE 1QW'), 'QWE 1QW')
        self.assertEqual(check_format('qwe 9qw'), 'QWE 9QW')







if __name__ == '__main__':
    unittest.main() 
