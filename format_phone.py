import re
import phonenumbers


def remove_punctuation(phone_number):
    number_punctuation_re = re.compile(r'[\s,.\-\(\)\[\]\{\}_]')
    number_without_punctuation = number_punctuation_re.sub('', phone_number)
    return number_without_punctuation


def remove_country_code(phone_number):
    try:
        phonenumber = phonenumbers.parse(phone_number, "RU")
        if phonenumbers.is_possible_number(phonenumber):
            national_number = str(phonenumber.national_number)
            return national_number
        else:
            return None
    except phonenumbers.NumberParseException:
        return None


def format_phone_number(phone_number):
    if not phone_number:
        return None
    number = remove_punctuation(phone_number)
    if not number:
        return None
    number = remove_country_code(number)
    if number is None or len(number) != 10:
        return None
    return number
