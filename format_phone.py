import re


def format_phone_number(phone_number):
    if not phone_number:
        return None
    number_punctuation_re = re.compile(r'[\s,.\-\(\)\[\]\{\}_]')
    number = number_punctuation_re.sub('', phone_number)
    if not number:
        return None
    if number[0:1] == '+':
        if number[0:2] == '+7':
            number = number[2:]  # remove country code
        else:
            return None
    digits_re = re.compile(r'^\d+$')
    if not digits_re.match(number):
        return None
    digits = len(number)
    if digits > 10:
        if digits == 11 and number[0:1] == '8':
            number = number[1:]
        else:
            return None
    elif digits < 10:
        return None
    return number
