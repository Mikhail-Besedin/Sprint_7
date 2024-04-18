import allure
import datetime
import random
import string

@allure.step("генерация строки")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
@allure.step("генерация даты")
def generating_data():
    data = str(datetime.date.today())
    return data

@allure.step("генерация числа")
def generate_random_number(length):
    digits = string.digits
    random_number = ''.join(random.choice(digits) for i in range(length))
    return random_number





