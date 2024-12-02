from datetime import date
from datetime import datetime
import datetime
from datetime import datetime as dt
from datetime import timedelta

import json

from pydantic.v1.datetime_parse import date_re


def check_date_of_birth(date_4_check):
    date1 = datetime.datetime.now()
    date2 = dt.strptime(date_4_check, '%Y-%m-%d')
    time_difference = date1 - date2
    print (time_difference)
    if time_difference > timedelta(days=6570):
        return True
    else:
        return False


with open('json_1.data') as file:
    # Загружаем данные json_1.data
    data = json.load(file)
    # Получаем доступ к данным
    print(data)
    print(check_date_of_birth(data.get("date_of_birth")))

with open('json_2.data') as file:
    # Загружаем данные json_1.data
    data = json.load(file)
    # Получаем доступ к данным
    print(data)
    print(check_date_of_birth(data.get("date_of_birth")))

