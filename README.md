# Antirobot

Телеграм бот для блокировки спама.

## Принцип работы

При входе нового пользователя в чат, ему отправляется сообщение
с просьбой выбрать один _emoji_ из нескольких предложенных.

Список emoji находится в файле *data/emojies.py*, шаблоны сообщений в *data/phrases.py*.

##  Необходимые разрешения

Боту требуются права администратора с возможностями:

- Удалять сообщения
- Блокировать участников

## Docker

`docker-compose up -d`

## Установка и запуск

Переименовать `.env.dist` в `.env`

```shell
python -m venv venv
source venv/bin/activate
# venv\bin\activate.bat - для Windows
pip install -r requirements.txt
```

```shell
python app.py
```

Настройка логирования в файле *utils/logger_config.py*

## Environment

| Переменная   | Тип         | По умолчанию | Обязательная |
|--------------|-------------|--------------|--------------|
| BOT_TOKEN    | str         |              | Да           |
| ADMINS_ID    | list of IDs |              | Да           |
| SKIP_UPDATES | bool        | False        | Нет          |
| NUM_BUTTONS  | int         | 5            | Нет          |
| ENTRY_TIME   | int         | 300          | Нет          |
| BAN_TIME     | int         | 30           | Нет          |

`BOT_TOKEN` -  
`ADMINS_ID` -  
`SKIP_UPDATES` -  
`NUM_BUTTONS` - кол-во предлагаемых вариантов emoji в сообщении от бота. От 2 до 7 включительно.  
`ENTRY_TIME` -  
`BAN_TIME` -  
