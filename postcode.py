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
    https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/488478/Bulk_Data_Transfer_-_additional_validation_valid_from_12_November_2015.pdf

    Keywords Arguments:
    code - string

    Return:
    type - Boolean
    """

    regex_validate = '^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$'

    if re.match(regex_validate, format_code(code)):
        return True
    return False
