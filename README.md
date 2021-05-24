# **polls-api-swagger**
## В данном API реализован функционал
- создание, добавление, изменение, удаление опросов
- прохождение опросов
- автодокументирование SWAGGER

## **Руководство пользователя:**

#### Клонируйте репозиторий в рабочую папку:
    git clone https://github.com/Nikolai-Python/polls-api-swagger.git
    cd polls-api-swagger
#### Создайте виртуальное окружение и установите зависимости:
    pipenv install
    pipenv shell
    pip install -r Requirements.txt
#### Проведите миграции:
    python manage.py makemigrations
    python manage.py migrate
#### Создайте суперпользователя:
    python manage.py createsuperuser
#### Запустите локальный сервер и перейдите в админ.панель с введёнными учётными данными:
    python manage.py runserver
    http://127.0.0.1:8000/admin/
#### В разделе ТОКЕН АУТЕНТИФИКАЦИИ добавьте токен авторизации для своей учётной записи
### **Сохраните токен и работайте в API:**
- наполните БД первоначальными данными в админ-панели
- http://127.0.0.1:8000/swagger/ система автодокументирования
- http://127.0.0.1:8000/redoc/   
- http://127.0.0.1:8000/polls/     список всех опросов
- http://127.0.0.1:8000/polls/id/   страница просмотра/редактирования опроса
- http://127.0.0.1:8000/polls/id/choices/ список вариантов ответов
- http://127.0.0.1:8000/polls/id/choices/id/ страница просмотра/редактирования ответов
- http://127.0.0.1:8000/polls/id/choices/id/vote/ список голосований
- http://127.0.0.1:8000/polls/id/choices/id/vote/id/ страница голосования

# **Технологии**
djangorestframework
