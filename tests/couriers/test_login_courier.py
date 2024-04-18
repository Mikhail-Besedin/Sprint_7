import allure
import requests
from data import Urls, ApiResponse


class TestLoginCourier:

    @allure.title('Успешная авторизация ')
    @allure.description("Проверка успешной авторизации,статус кода и возврат id ")
    def test_authorization_courier_successfully(self,register_new_courier_and_return_login_password):
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1],
            "firstName": register_new_courier_and_return_login_password[2]}
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and "id" in response.text

    @allure.title('Авторизация без указания login')
    @allure.description("Проверка ошибки авторизации курьера без указания обязательного поля login")
    def test_courier_authorization_not_login(self, register_new_courier_and_return_login_password):
        payload = {"password": register_new_courier_and_return_login_password[2]}
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.text == ApiResponse.RESPONSE_LOGIN_COURIERS_WITHOUT_LOGIN

    @allure.title('Авторизация с указанием некоррекных данных')
    @allure.description("Проверка  ошибки авторизации курьера с некоррекным логином")
    def test_courier_authorization_with_incorrect_data(self, register_new_courier_and_return_login_password,create_data_for_courier ):
        payload = {
            "login": create_data_for_courier[0],
            "password": register_new_courier_and_return_login_password[1],
            "firstName": register_new_courier_and_return_login_password[2]}
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        assert response.text == ApiResponse.ERROR_INCORRECT_DATA