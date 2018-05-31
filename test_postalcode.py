import unittest

from postalcode import *

class PostalCodeTest(unittest.TestCase):

    def test_format_missing_one_last_digit(self):
        self.assertEqual(format_code('QWE QW'), 'QWE  QW')

    def test_format_six_digits(self):
        self.assertEqual(format_code('QWE 1QW'), 'QWE 1QW')
        self.assertEqual(format_code('qwe 9qw'), 'QWE 9QW')

    def test_validate_post_code_missing_value(self):
        self.assertFalse(validate_code('QWE 1W'))

    def test_validate_post_code_wrong_value(self):
        self.assertFalse(validate_code('Q 1W'))

    def test_validate_post_code_missing_value_first(self):
        self.assertFalse(validate_code('1WW'))

    def test_validate_post_code_correct(self):
        self.assertTrue(validate_code('CV4 8UW'))

    def test_validate_post_code_correct_with_values_together(self):
        self.assertTrue(validate_code('CV48UW'))

    def test_validate_post_code_empty_value(self):
        self.assertFalse(validate_code(''))

if __name__ == '__main__':
    unittest.main() 
