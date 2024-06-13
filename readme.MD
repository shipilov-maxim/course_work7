* Клонирование проекта

`git clone https://github.com/shipilov-maxim/course_work7.git`

Заполните файл .env своими данным по примеру .env.sample


Сборка и запуск контейнеров

`docker-compose up --build`

* Регистрация нового пользователя http://127.0.0.1:8000/users/users/ {POST}

`{
    "email": "user@example.com",
    "password": "Somepassword",
    "chat_id": "000000001"
}`

* Получение токена http://127.0.0.1:8000/users/token/
* Создание привычки http://127.0.0.1:8000/habits/create/

`{
    "place": "на улице",
    "time": "10:00",
    "action": "погулять",
    "is_enjoyable": false,
    "periodicity": 3, # по выходным
    "treat": "поиграть в пк",
    "duration": 120,
    "is_public": true
}`

* Документация 


* Swagger - http://127.0.0.1:8000/docs/
* Redoc - http://127.0.0.1:8000/redoc/