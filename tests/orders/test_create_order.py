import json
import allure
import pytest
import requests
from data import Urls
from helpers import generate_random_string, generate_random_number, generating_data


class TestCreateOrder:

    @allure.title('Создание заказа ')
    @allure.description("Проверка успешного создания заказа,статус кода и тело ответа содержит track ")
    @pytest.mark.parametrize('color', [(["BLACK"]),(["GREY"]),(["GREY", "BLACK"]),([''])])
    def test_create_order(self,color):
        payload = {
    "firstName": generate_random_string(7),
    "lastName": generate_random_string(7),
    "address": generate_random_string(7),
    "metroStation":generate_random_number(1),
    "phone": generate_random_number(11),
    "rentTime": generate_random_number(1),
    "deliveryDate": generating_data(),
    "comment": generate_random_string(10),
    "color": color}
        payload_order = json.dumps(payload)
        response = requests.post(Urls.CREATE_ORDER, data=payload_order)
        assert response.status_code == 201 and "track" in response.text