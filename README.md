# bitbucket

Технологии и требования:
```
Python 3.9+
Django
Django REST Framework
Poetry
```

#### Тестовые файлы с логами

В папке log_files сохранены 2 файла с логами для проверки работы приложения. 
Один из них подходит под маску, другой нет

### Настройки Docker

##### Установка

* [Подробное руководство по установке](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

### Настройки Docker-compose

##### Установка

* [Подробное руководство по установке](https://docs.docker.com/compose/install/)

### Зависимости

Зависимости в проекте устанавливаются с помощью poetry.
* [документация с информацией по установке poetry](https://python-poetry.org/docs/cli/)

#### Перед запуском проекта создаем переменные окружения
Создаем в корне .env и добавляем в него следующие данные:

* DJANGO_SECRET_KEY=
* DB_NAME=bitbucket
* POSTGRES_USER=bitbucket
* POSTGRES_PASSWORD=bitbucket
* DB_PORT=5432
* SETTINGS_FOR_CELERY=
* APACHE_LOG_FORMAT=%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"
* APACHE_LOG_FOLDER=log_files
* APACHE_LOG_FILE=*access.log

SETTINGS_FOR_CELERY указываем следующие:
* "config.settings.settings" - для запуска всего проекта в контейнерах
* "config.settings.local" - для локальной разработки

APACHE_LOG_FORMAT указывается формат логирования согласно документации 
https://httpd.apache.org/docs/2.4/logs.html

APACHE_LOG_FOLDER - название папки в корне проекта в которой будут находиться 
лог файлы

APACHE_LOG_FILE - маска для файлов с логами

## Запуск проекта полностью в контейнерах docker

* `docker-compose up --build`

Автоматический создается пользователь admin, пароль admin.

#### Доступ

http://127.0.0.1/admin/

#### Автодокументация

http://127.0.0.1/api/v1/schema/swagger-ui/

### Для Локальной разработки (bd и redis в контейнерах + приложение локально)

#### Создаем виртуальное окружение, устанавливаем зависимости
* `python -m venv venv`
* `source venv/bin/activate`
* `poetry install`

#### Команды для запуска bd в контейнере + приложения локально

* `docker-compose -f postgres-local.yml up --build` - создать и запустить контейнеры docker
* `python manage.py runserver --settings config.settings.local` - запускаем 
  проект
* `python manage.py makemigrations --settings config.settings.local` - создать миграции (миграции уже хранятся в репозитории, так что это опционально)
* `python manage.py migrate --settings config.settings.local` - применить миграции
* `python manage.py createsuperuser --settings config.settings.local` - создать суперпользователя
* `docker run -d -p 6379:6379 redis` - запускаем redis в контейнере
* `celery -A logs worker -l info` - запускаем воркер celery
* `celery -A logs bear -l info` - запускаем beat celery
* `python manage.py  filldb` - создаем пользователя admin, пароль admin
* 
#### Доступ

* http://127.0.0.1:8000/admin/

#### Автодокументация

http://127.0.0.1:8000/api/v1/schema/swagger-ui/

### Запуск тестов 

* `docker-compose exec web pytest` - в контейнере
* `pytest` - локально
