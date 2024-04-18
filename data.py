class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    LOGIN_COURIER = BASE_URL + "/api/v1/courier/login"
    CREATE_COURIER = BASE_URL + "/api/v1/courier"
    DELETE_COURIER = BASE_URL + "/api/v1/courier/"
    CREATE_ORDER = BASE_URL + "/api/v1/orders"
    GET_LIST_ORDERS = BASE_URL + "/api/v1/orders"


class ApiResponse:
    TEXT_RESPONSE_LOGIN_SUCCESSFULLY = '{"ok":true}'
    RESPONSE_CREATE_COURIERS_WITH_THE_SAME_DATA = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    RESPONSE_CREATE_COURIERS_WITHOUT_LOGIN = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    RESPONSE_LOGIN_COURIERS_WITHOUT_LOGIN = '{"code":400,"message":"Недостаточно данных для входа"}'
    ERROR_INCORRECT_DATA='{"code":404,"message":"Учетная запись не найдена"}'