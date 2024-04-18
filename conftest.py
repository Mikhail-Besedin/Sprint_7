import allure
import pytest
import requests
from data import Urls
from helpers import generate_random_string



@allure.step("Генерируем данные для создания курьера и возвращаем список из логина, пароля и имени.")
@pytest.fixture()
def create_data_for_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    login_pass = []
    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    return login_pass



@allure.step("регистрируем нового курьера и возвращаем список из логина и пароля,"
             "  если регистрация не удалась - возвращаем пустой список. После прохождения теста , удаляем курьера.")
@pytest.fixture()
def register_new_courier_and_return_login_password():
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Urls.CREATE_COURIER, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)


    yield login_pass

    payload = {
        "login": login_pass[0],
        "password": login_pass[1], }
    login_courier = requests.post(Urls.LOGIN_COURIER, data=payload)

    id_courier = str(login_courier.json()['id'])
    response_delete = requests.delete(Urls.DELETE_COURIER + id_courier)
    return response_delete
