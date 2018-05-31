import re


def check_format(code):
     second_part = code.split(' ')[-1].upper()
     if re.search('\d{1}[A-Z]{2}', second_part):
         return code.upper()

def validate_code(code):
    regex_validate = '^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$'

    if re.match(regex_validate, str(check_format(code))):
        return 'Post Code valid!'
    return 'Error in code'
