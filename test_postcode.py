import unittest

from postcode import *

class PostCodeTest(unittest.TestCase):

    def test_tree_last_digits_missing_one(self):
        self.assertEqual(check_format('QWE QW'), 'Not a valid PostCode in UK')

    def test_tree_last_digits_sequence_wrong(self):
        self.assertEqual(check_format('QWE QW1'), 'Not a valid PostCode in UK')

    def test_tree_last_digits_correct(self):
        self.assertEqual(check_format('QWE 1QW'), 'QWE 1QW')
        self.assertEqual(check_format('qwe 9qw'), 'QWE 9QW')








if __name__ == '__main__':
    unittest.main() 
