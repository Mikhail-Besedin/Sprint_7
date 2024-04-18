import allure
import requests

from data import ApiResponse, Urls


class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    @allure.description("Создание курьера, проверка кода и текста ответа")
    def test_create_courier_successfully(self, create_data_for_courier):
        payload = {
            "login": create_data_for_courier[0],
            "password": create_data_for_courier[1],
            "firstName": create_data_for_courier[2]}
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == ApiResponse.TEXT_RESPONSE_LOGIN_SUCCESSFULLY

    @allure.title("Невозможно создать двух одинаковых курьеров")
    @allure.description("Проверка статус кода и текста ошибки при создании курьеров с одинаковыми логинами и паролями")
    def test_create_couriers_with_the_same_data(self,register_new_courier_and_return_login_password):
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1],
            "firstName": register_new_courier_and_return_login_password[2]}

        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 409 and response.text == ApiResponse.RESPONSE_CREATE_COURIERS_WITH_THE_SAME_DATA

    @allure.title("Попытка создать курьера без указания login")
    @allure.description("Проверка статус кода и текста ошибки  при попытки создания курьера без обязательного поля login")
    def test_create_couriers_not_login(self, create_data_for_courier):
        payload = {"password": create_data_for_courier[1], "firstName": create_data_for_courier[2]}
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.text == ApiResponse.RESPONSE_CREATE_COURIERS_WITHOUT_LOGIN

    @allure.title("Попытка создать курьера без указания password")
    @allure.description("Проверка статус кода и текста ошибки  при попытки создания курьера без обязательного поля password")
    def test_create_couriers_not_password(self, create_data_for_courier):
        payload = {"login": create_data_for_courier[0], "firstName": create_data_for_courier[2]}
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.text == ApiResponse.RESPONSE_CREATE_COURIERS_WITHOUT_LOGIN

