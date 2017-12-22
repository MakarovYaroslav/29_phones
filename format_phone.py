import re


def remove_punctuation(phone_number):
    number_punctuation_re = re.compile(r'[\s,.\-\(\)\[\]\{\}_]')
    number_without_punctuation = number_punctuation_re.sub('', phone_number)
    return number_without_punctuation


def is_numeric(phone_number):
    digits_re = re.compile(r'^\d+$')
    if not digits_re.match(phone_number):
        return False
    else:
        return True


def remove_country_code(phone_number):
    if phone_number[:1] == '+':
        if phone_number[:2] == '+7':
            number_without_code = phone_number[2:]
            return number_without_code
        else:
            return None
    else:
        return phone_number


def truncate_number_length(phone_number):
    digits = len(phone_number)
    if digits == 10:
        return phone_number
    elif digits == 11 and phone_number[:1] == '8':
        phone_number = phone_number[1:]
        return phone_number
    else:
        return None


def format_phone_number(phone_number):
    if not phone_number:
        return None
    number = remove_punctuation(phone_number)
    if not number:
        return None
    number = remove_country_code(number)
    if number is None:
        return None
    if not is_numeric(number):
        return None
    number = truncate_number_length(number)
    return number
