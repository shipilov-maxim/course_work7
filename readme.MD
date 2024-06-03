* Клонирование проекта

`git clone https://github.com/shipilov-maxim/drf.git`

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

