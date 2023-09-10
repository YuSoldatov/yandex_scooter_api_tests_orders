import functions


# Тест на проверку получения данных о заказе по трек-номеру с помощью API Яндекс Самокат
def test_get_order_by_track():
    # Шаги автотеста:
    # Выполнить запрос на создание заказа. (выполняется в functions.post_new_order(body))
    # Сохранить номер трека заказа.
    order_track = functions.get_new_order_track()
    # Выполнить запрос на получения заказа по треку заказа.
    order_response = functions.get_order_by_track(order_track)
    # Проверить, что код ответа равен 200.
    assert order_response.status_code == 200



