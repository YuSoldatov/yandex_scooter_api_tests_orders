import requests
import configuration
import data


# POST-запрос на создание нового заказа
def post_new_order(body):
    # возвращается ответ (response)
    return requests.post(configuration.URL_SERVICE + configuration.POST_ORDER_PATH,  # полный url
                         json=body)  # тело запроса


# Функция получения номера заказа track
def get_new_order_track():
    # В переменную order_response сохраняется результат запроса на создание заказа:
    order_response = post_new_order(data.order_body)
    # Возвращается номер заказа
    return order_response.json()["track"]


# Функция получения заказа по его номеру track
def get_order_by_track(track):
    # Возвращается ответ на GET-запрос на эндпоинт /v1/orders/track?t={track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + f"?t={track}")
