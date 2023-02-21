# Django-actors

Сайт про Известных актеров. Пользователь может смотреть список актеров и просматривать детально их биографию

---

**Стек:**
- Python==3.10.7
- Django==4.1.6
- SQLite3
---
<h3>Руководство по устоновке:</h3>

#### 1) Скалинируте репозиторий
    git clone https://github.com/Raasaal511/actors_site/

#### 2) Создать виртульное окружение
     pip -m venv venv

#### 3) Актвировать веруальное окружение (если оно не активировалось)
###### (windows)
    cd venv/scripts
    activate

#### 4) Сделайте миграцию:
    python manage.py makemigrations
    python manage.py migrate

#### 4) Создайте супер пользвателя:
    python manage.py createsuperuser
