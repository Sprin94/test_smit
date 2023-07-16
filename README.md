
# Тестовое задание

Python developer

## Стек

Python, FastAPI, Docker, Docker-compose, PostgreSQL.


## Приложение
Приложение по расчёту стоимости страхования.   

# Использование
### Без docker
1. Склонируйте данный репозиторий на свою локальную машину
2. Убедитесь, что у вас установлен пакет [Poetry](https://python-poetry.org/docs/)
3. Установите зависимости командой:
```sh
poetry install
```
4. Заполните .env файл согласно образцу.
5. Запустите приложение:
```
python -m app.main
```

### Использование через docker
1. Склонируйте данный репозиторий на свою локальную машину
2. Заполните .env файл согласно образцу   
3. Выполните команду:
```sh
docker-compose up --build -d
```
