# short 
This application allows you to change the URL to public Telegram channels every N minutes from different accounts in order to avoid temporary blocking.

# Быстрый старт в два шага
### Первый шаг
В файл `config.json` устанавливаем:
- в ключ **channels** список из **id** *(int)* каналов;
- в ключ **bots** список из словарей с соответствующими данными о пользователях (ботах);

Пример:
```JSON
{
    "channels":
        [
            -1001978319159,
            -1001760896418
        ],
    "bots":
        [
            {
                "API_ID": 12345678, 
                "API_HASH": "25tt4t2fbawda66bf3beb43d7476d5f", 
                "PHONE": "8913333999", 
                "PASSWORD": "password"
            }
        ]
}
```
### Второй шаг
В файле `main.py` устанавливаем необходимые задержки (по стандарту 4 минуты).
Запускаем файл `main.py` командой:
```bash
python3 main.py
```
При первом запуске необходимо ввести коды защиты для аккаунтов. После первого запуска, сессии будут сохранены и вводить коды защиты больше не потребуется.
