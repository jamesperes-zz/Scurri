import unittest

from postcode import *

class PostCodeTest(unittest.TestCase):

    def test_tree_last_digits_missing_one(self):
        self.assertFalse(format_code('QWE QW'))

    def test_tree_last_digits_sequence_wrong(self):
        self.assertFalse(format_code('QWE QW1'))

    def test_digits_sequence_with_number_tohether(self):
        self.assertFalse(format_code('QWEQW1'))

    def test_tree_last_digits_correct(self):
        self.assertEqual(format_code('QWE 1QW'), 'QWE 1QW')
        self.assertEqual(format_code('qwe 9qw'), 'QWE 9QW')

    def test_validate_post_code_missing_value(self):
        self.assertEqual(validate_code('QWE 1W'), 'Error in code')

    def test_validate_post_code_missing_value(self):
        self.assertEqual(validate_code('Q 1W'), 'Error in code')

    def test_validate_post_code_missing_value_first(self):
        self.assertEqual(validate_code('1W'), 'Error in code')

    def test_validate_post_code_correct(self):
        self.assertEqual(validate_code('CV4 8UW'), 'Post Code valid!')

    def test_validate_post_code_correct_but_together(self):
        self.assertEqual(validate_code('CV48UW'), 'Post Code valid!')

    def test_validate_post_code_empty_value(self):
        self.assertEqual(validate_code(''), 'Error in code')

if __name__ == '__main__':
    unittest.main() 
