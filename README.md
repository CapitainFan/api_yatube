# api_yatube
### Описание
Это тестовый сервер для работы с API
### Технологии
Python 3.7 ;  
Django 2.2.19 ;  
API ;  
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:CapitainFan/api_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Авторы
Никита Гудков
