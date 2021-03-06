HH METRO
==============

Микросервис для проверки станций метро через API HH

Сервис поднят на адресе http://172.105.66.14:8080

Установка
-----------

Клонирование репозитория::

    $ git clone git@github.com:O3DB/hh_metro.git

Установа зависимостей::

    $ cd metro
    $ pip install -r requirements.txt

Запуск приложения::

    $ python ./metro/main.py

Запуск в docker-контейнере
---------------------------

Скачайте *docker-compose.yaml*

Запустите контейнер::

    $ docker-compose up -d

API
==============



Принимает на вход список станций, сравнивает со списком,
получаемым с https://api.hh.ru/metro/1 и возвращает перечень переименованных станций, добавленных и станций без изменения.

**URL**::


    /api/v1/metro/verificate/

**Method**::

    POST

**Headers**::

    Content-Type: application/json; charset=utf-8

**Body**::

    JSON список станций
    [
	"Каховская",
	"Баррикадная",
	...
    ]

**Формат ответа**::

    {
        "unchanged": [...],
        "updated": [...],
        "deleted": [...]
    }
