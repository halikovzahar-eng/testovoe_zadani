# Тестовое задиние

## Структура проекта
1. backend/
    - app.py
    - Dockerfile
2. nginx/
    - nginx.conf
3. docker-compose.yml

## Как развернуть
1. В VS code  установить расширения GitHub Repositories, Docker DX, Python
2. Установить docker desktop либо docker engine + docker compose(для Linux без графического интерфейса)
3. Установить git и клонировать уделнный репозиторий ``` git clone "ссылка либо SHH-ключ репизитория" ``` и переходим в него командой в VS Code создаем терминал
4. Выполнить команду ```docker-compose build``` собирает приложения, ``` docker compose up -d ```  запустит web-приложение и nginx  
5. Для проверки в Docker Desktop  во вкладке контейнеры посмотреть запущенные, там будет docker-compose в котором web-backend, revers_proxy-nginx. либо командой ``` docker ps ```
6. В терминале ``` curl http://localhost ``` либо в браузере http://localhost. Ответ должен быть Hello from Effective Mobile!


## Как работает
*Docker-compose.yml* собирает 2 контейнера: **web-приложение** из dockerfile который нахожится вместе с приложение в папке *backend*, и **nginx** из готового образа с dockerhub который берет файл конфигурации **nginx.conf** из репозитория в папке *ninx/nginx.conf*. Контейнеры находятся в docker-сети взаимодествуют между собой по портам **8080**(web-приложениеоткрыт только в нутри сети) и **80**(порт nginx открыт)
Когда идет обращение к *http://lockalhost* get-запрос идет на порт 80, nginx перенапраляет его на порт 8080 приложения и ввыодит ответ **"Hello from Effective Mobile!"**. Если ввсести *http://lockalhost:8080* будет ошибка 404

