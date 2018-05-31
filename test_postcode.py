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

    def test_validate_post_code_missing_value(self):
        self.assertEqual(validate_code('QWE 1W'), 'Error in code')

    def test_validate_post_code_missing_value(self):
        self.assertEqual(validate_code('Q 1W'), 'Error in code')

    def test_validate_post_code_missing_value_first(self):
        self.assertEqual(validate_code('1W'), 'Error in code')

    def test_validate_post_code_missing_value_first(self):
        self.assertEqual(validate_code('1W'), 'Error in code')

    def test_validate_post_code_correct(self):
        self.assertEqual(validate_code('CV4 8UW'), 'Post Code valid!')


if __name__ == '__main__':
    unittest.main() 
