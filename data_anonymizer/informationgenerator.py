import random

class InformationGenerator:
    def __init__(self):
        return

    def phonenumber(self):
        number = str(random.randint(0,99999999))
        number = '316' + '0' * (8 - len(number)) + number
        return number