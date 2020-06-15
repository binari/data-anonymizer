import random
import json


def get_first_name():
    first_names_file = open('data_anonymizer/assets/first_names_male.json')

    if random.randint(0, 100) > 75:
        first_names_file = open('data_anonymizer/assets/first_names_female.json')

    return random.choice(json.load(first_names_file))


def get_phone_number():
    number = str(random.randint(0, 99999999))
    number = '316' + '0' * (8 - len(number)) + number
    return number


def get_last_name():
    last_names = open('data_anonymizer/assets/last_names.json')
    return random.choice(json.load(last_names))