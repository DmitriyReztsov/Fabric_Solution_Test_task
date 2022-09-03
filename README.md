# Solution Fabric test
Реализация API сервиса управления рассылками тестового проекта EmphaSoft.


# Использованные языки и фреймворки:
- [Python](https://www.python.org/) 3.10.4
- [Django](https://www.djangoproject.com/) 3.2
- [Django Rest Framework](https://www.django-rest-framework.org/) 3.13.1
- [Celery](https://docs.celeryq.dev/en/stable/) 5.2.7


# Приступая к работе

- Клонируйте репозиторий:
```
git clone https://gitlab.com/DmitriyReztsov/fabric
```

- Установите зависимости:
```
pip install -r requirements.txt
```

- Выполните миграции:
```
python manage.py makemigrations
python manage.py migrate
```

- Создайте суперпользователя:
```
python manage.py createsuperuser
Username (leave blank to use 'user'): # Придумайте логин (например, admin)
Email address: # укажите почту
Password: # придумайте пароль
Password (again): # повторите пароль
Superuser created successfully.
```

- Запустите сервер:
```
python manage.py runserver
```

- Запустите брокера сообщений (в моем случае - из докера):
```
docker run -d -p 5672:5672 rabbitmq
```

- Запустите Celery:
```
celery -A mailing.tasks worker --loglevel=INFO
```

# Endpoints

Запустите сервер. Доступные эндпойнты будут доступны по адресу http://127.0.0.1:8000/swagger/

Список доступных эндпойнтов:
| Endpoint | Доступные методы | Описание |
| -------- | ---------------- | -------- |
| /mailing/mailings/ | GET, POST | получение и создание рассылки |
| /mailing/mailings/{id} | GET, PUT, PATCH, DELETE | получение, изменения и удаление рассылки |
| /clients/clients/ | GET, POST | получение и создание клиента |
| /clients/clients/{id}/ | GET, PUT, PATCH, DELETE | получение, изменения и удаление пользователя |
| /mailing/statistic/ | GET | получение статистики по всем рассылкам в формате json |
| /mailing/statistic/{id}/ | GET | получение статистики по рассылке {id} в формате json |


# Автор

Dmitriy Reztsov