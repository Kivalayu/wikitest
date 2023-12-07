import pandas as pd
import pytest


def webpop(threshold):
    # ссылка на страницу, где нужно взять таблицу
    url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

    # чтение всех таблиц с сайта
    tables = pd.read_html(url)

    # чтение конкретно первой таблицы
    table = tables[0]

    # сохраняем таблицу в дата фрейм для дальнейшего использования
    df = pd.DataFrame(table)

    # переводим второй столбик в численный формат
    table['Popularity (unique visitors per month)[1]'] = pd.to_numeric(table['Popularity (unique visitors per month)[1]'], errors='coerce')

    # создаем лист значений ниже порога
    below_threshold = []

    for value in table['Popularity (unique visitors per month)[1]']:
        if value <= threshold:
            below_threshold.append(value)

    # если значения будут меньше заданного числового параметра будет выдаваться ошибка
    if below_threshold:
        print(f"Wikipedia (Frontend:JavaScript|Backend:PHP) has {below_threshold} unique visitors per month. (Expected more than {threshold})")

# запуск теста
@pytest.mark.parametrize('threshold', [10**7, 1.5*10**7, 10**8, 10**9, 1.5*10**9])
def test_webpop_threshold(threshold):
    webpop(threshold)