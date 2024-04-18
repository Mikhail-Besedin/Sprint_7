import allure
import requests

from data import Urls


class TestGetListOrder:
    @allure.title('Получение списка  заказов ')
    @allure.description("Проверка получения списка заказов, статус кода и в тексте ответа есть orders ")
    def test_get_10_free_orders(self):
        response = requests.get(Urls.GET_LIST_ORDERS)
        assert response.status_code == 200 and 'orders' in response.json()

