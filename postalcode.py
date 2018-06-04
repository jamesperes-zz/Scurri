__author__ = "James Peres"

import re


def format_code(code):
    """ Format UK Postal Code properly formatted

    Keywords Arguments:
    code - string

    Return:
    type - string
    """

    code_to_check = code.upper()
    first_part = code_to_check[:-3].strip()
    second_part = code_to_check[-3:]
    return "{} {}".format(first_part, second_part)


def validate_code(code):
    """ Validate UK Postal Code with regex available in
    https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    
    Keywords Arguments:
    code - string

    Return:
    type - Boolean
    """


    regex_validate = '(GIR 0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]|[A-HK-Y][0-9]([0-9]|[ABEHMNPRV-Y]))|[0-9][A-HJKPS-UW]) [0-9][ABD-HJLNP-UW-Z]{2})'

    """Explaining Regex
    GIR 0AA = last domestic postcode with a fully alphabetical outward code
    [A-PR-UWYZ] =  The letters QVX are not used in the first position.
    [A-HK-Y] = The letters IJZ are not used in the second position.
    [A-HJKPS-UW] = The only letters to appear in the third position are 
                   ABCDEFGHJKPSTUW when the structure starts with A9A. 
    [ABEHMNPRV-Y] = The only letters to appear in the fourth position are 
                    ABEHMNPRVWXY when the structure starts with AA9A.
    [ABD-HJLNP-UW-Z]{2} = The final two letters do not use the letters CIKMOV
    """

    single_digits = ['BR','FY','HA','HD','HG','HR','HS','HX','JE','LD','SM',\
                     'SR','WC','WN','ZE']
    double_digits = ['AB', 'LL', 'SO']
    digit_zero = ['BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS']

    code = format_code(code)
    if code[:2] in double_digits:
        if re.match('([A-Z]{2}[0-9]{2} [0-9]{1}[BD-HJLNP-UW-Z]{2}$)', code):
            return True
        else:
            return False

    if code[:2] in single_digits:
        if re.match('([A-Z]{2}[0-9]{1} [0-9]{1}[BD-HJLNP-UW-Z]{2}$)', code):
            return True
        else:
            return False

    if code[:2] in digit_zero:
        if re.match('([A-Z]{2}[0]{1} [0-9]{1}[BD-HJLNP-UW-Z]{2}$)', code):
            return True
        else:
            return False

    if re.match(regex_validate, code):
        return True
    else:
       return False
