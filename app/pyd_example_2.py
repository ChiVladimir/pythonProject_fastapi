from datetime import date

from pydantic import BaseModel

# Объявляем параметр user_id с типом `str`
# и получаем поддержку проверки типов данных редактора (IDE) внутри функции
def main(user_id: str):
    return user_id


# Модель Pydantic - ещё один пример создания
class User(BaseModel):
    id: int
    name: str
    joined: date
    date_of_birth: date

my_user: User = User(id=3, name="John Doe", joined="2018-07-19", date_of_birth="1980-01-12")

second_user_data = {"id": 4,
                    "name": "Mary",
                    "joined": "2018-11-30",
                    "date_of_birth": "2010-01-12"
                    }

my_second_user: User = User(**second_user_data)

#print(my_second_user)
print(my_user.model_dump_json())
print(my_second_user.model_dump_json())

file_name = "json_1.data"
file = open(file_name, 'a+')
file.write(f'{my_user.model_dump_json()}')
file.close()
file_name = "json_2.data"
file = open(file_name, 'a+')
file.write(f'{my_second_user.model_dump_json()}')
file.close()
