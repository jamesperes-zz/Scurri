import re


def check_format(code):
    second_part = code.split(' ')[1].upper()
    if re.search('\d{1}[A-Z]{2}', second_part):
        return code.upper()
    else:
        return 'Not a valid PostCode in UK'
