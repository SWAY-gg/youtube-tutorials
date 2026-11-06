# Эпизод 1: первый Discord-бот на disnake

Код из видео [«Бот на disnake — слэш-команды с нуля»]([ССЫЛКА НА ВИДЕО]) с YouTube-канала **Sweet1e42**.

Бот на Python и библиотеке [disnake](https://github.com/DisnakeDev/disnake) с двумя слэш-командами:

| Команда | Что делает |
| --- | --- |
| `/ping` | Отвечает «Понг!» и показывает задержку бота в миллисекундах |
| `/say text:<текст>` | Повторяет ваш текст |

## Что понадобится

- [Python 3.14](https://www.python.org/downloads/). disnake официально поддерживает Python 3.10–3.14, версии 3.15 в этом списке пока нет.
- [Visual Studio Code](https://code.visualstudio.com/) или любой другой редактор.
- Аккаунт Discord и свой тестовый сервер.

## Структура проекта

```
MyBot/
├── main.py           # код бота
├── requirements.txt  # зависимости
├── .env.example      # пример файла с токеном
├── .gitignore        # .env не попадёт в git
└── .vscode/
    └── settings.json # настройки VS Code из видео (необязательно)
```

## Установка

1. Скачайте репозиторий и откройте папку в терминале.
2. Создайте и активируйте виртуальное окружение:

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

   На Linux и macOS вторая команда — `source .venv/bin/activate`.

3. Установите зависимости:

   ```powershell
   pip install -r requirements.txt
   ```

## Создание бота в Discord

1. Откройте [Discord Developer Portal](https://discord.com/developers/applications) и нажмите **New Application**.
2. На вкладке **Bot** нажмите **Reset Token** и скопируйте токен.
3. На вкладке **OAuth2 → URL Generator** отметьте `bot` и `applications.commands`, а в правах бота — **Send Messages**. Откройте получившуюся ссылку и добавьте бота на свой сервер.
4. В Discord включите **Настройки → Расширенные → Режим разработчика**, нажмите правой кнопкой на сервер и выберите **Копировать ID сервера**.

Privileged Gateway Intents для этого бота включать не нужно.

## Настройка `.env`

Переименуйте `.env.example` в `.env` и вставьте свои значения:

```env
TOKEN=ваш_токен_бота
GUILD_ID=123456789012345678
```

> **Токен — это пароль от бота.** Не показывайте его никому и не загружайте `.env` на GitHub: файл уже добавлен в `.gitignore`. Если токен утёк, сразу нажмите **Reset Token** в Developer Portal.

## Запуск

```powershell
python main.py
```

В консоли появится строка `<имя бота> запущен и готов к работе!`. Напишите `/` в чате вашего сервера, и в списке появятся команды бота.

Команды регистрируются только на сервере из `GUILD_ID` (параметр `test_guilds`), поэтому появляются сразу. Чтобы бот работал на всех серверах, уберите `test_guilds` из `main.py`.

## Если не работает

| Проблема | Что проверить |
| --- | --- |
| `ModuleNotFoundError: No module named 'disnake'` | Активировано ли виртуальное окружение (в начале строки терминала должно быть `(.venv)`) |
| PowerShell не даёт активировать окружение | Выполните `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` и повторите |
| `LoginFailure: Improper token has been passed` | Правильно ли скопирован токен, нет ли пробелов и кавычек в `.env` |
| `TypeError: int() argument must be ...` | Заполнен ли `GUILD_ID` в `.env` |
| Команд нет в списке `/` | Совпадает ли `GUILD_ID` с сервером, где бот, и стояла ли галочка `applications.commands` при приглашении |

Не получилось разобраться? Заходите на [Discord-сервер канала]([ССЫЛКА НА СЕРВЕР]), там помогут.

## Дальше

В следующем эпизоде: эмбеды и кнопки.
