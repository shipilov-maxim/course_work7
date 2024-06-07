FROM python:3

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver"]
