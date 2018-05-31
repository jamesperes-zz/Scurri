import re


def format_code(code):
    code_to_check = code.upper().strip()
    first_part = code_to_check[:-3].strip()
    second_part = code_to_check[-3:]
    if re.search('\d{1}[A-Z]{2}', second_part):
        return "{} {}".format(first_part, second_part)

def validate_code(code):
    regex_validate = '^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$'

    if re.match(regex_validate, str(format_code(code))):
        return 'Post Code valid!'
    return 'Error in code'
