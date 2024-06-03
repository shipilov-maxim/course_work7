* Клонирование проекта

`git clone https://github.com/shipilov-maxim/course_work7.git`

* Установка переменного окружения

`python -m venv venv`

`pip install -r requirements.txt`

* Создайте файл .env по примеру .env.sample и заполните своими данными

* Применение миграций

`python manage.py makemigrations`

`python manage.py migrate`

* Установка фикстур

`python manage.py loaddata data.json`

* Запуск сервера

`python manage.py runserver`

* Запуск брокера

`redis-server`

* Запуск воркера(флаг "-P eventlet" на Windows)

`celery -A config worker -l INFO`

* Запуск celery-beat

`celery -A config beat -l INFO`

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