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

    def test_validate_post_code_invalid_missing_one_number(self):
        self.assertFalse(validate_code('AB1 1AA'))

    def test_validate_post_code_valid(self):
        self.assertTrue(validate_code('AB12 3XY'))
        self.assertFalse(validate_code('AB12 1AA'))

    def test_validate_post_code_invalid_with_QVX_first_possition(self):
        self.assertFalse(validate_code('WQA 0AX'))
        self.assertFalse(validate_code('WVA 0AX'))
        self.assertFalse(validate_code('WXA 0AX'))

    def test_validate_post_code_invalid_with_IJZ_second_possition(self):
        self.assertFalse(validate_code('AJ1 1AA'))
        self.assertFalse(validate_code('BJ1 1AA'))
        self.assertFalse(validate_code('CZ1 1AA'))

    def test_validate_post_code_valid_with_third_possition(self):
        valid = 'ABCDEFGHJKPSTUW'
        for i in valid:
            self.assertTrue(validate_code(f"W1{i} 0AX"))

    def test_validate_post_code_invalid_with_third_possition(self):
        invalid = 'ILMNOQRVXYZ'
        for i in invalid:
            self.assertFalse(validate_code(f"W1{i} 0AX"))

    def test_validate_post_code_valid_with_fourth_possition(self):
        valid = 'ABEHMNPRVWXY'
        for i in valid:
            self.assertTrue(validate_code(f"EC1{i} 1BB"))

    def test_validate_post_code_invalid_with_fourth_possition(self):
        invalid = 'CDFGIJKLOQSTUZ'
        for i in invalid:
            self.assertFalse(validate_code(f"EC2{i} 1BB"))

    def test_validate_post_code_invalid_final_letters(self):
        invalid = 'CIKMOV'
        for i in invalid:
            self.assertFalse(validate_code(f"CR2 6{i}H"))

        for i in invalid:
            self.assertFalse(validate_code(f"CR2 6X{i}"))

    def test_validate_post_code_valid_with_single_digit_district(self):
        valid = ['BR','FY','HA','HD','HG','HR','HS','HX','JE','LD','SM','SR','WC','WN','ZE']

        for i in valid:
            self.assertTrue(validate_code(f"{i}1 1BB"))

    def test_validate_post_code_valid_with_double_digit_district(self):
        valid = ['AB', 'LL', 'SO']

        for i in valid:
            self.assertTrue(validate_code(f"{i}12 1BB"))


    def test_validate_post_code_valid_with_double_digit_district_zero(self):
        valid = ['BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS'] 

        for i in valid:
            self.assertTrue(validate_code(f"{i}0 1BB"))



if __name__ == '__main__':
    unittest.main() 
