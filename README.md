# aiogram bot template (skeleton)

[![\[Telegram\] aiogram live](https://img.shields.io/badge/telegram-aiogram-blue.svg?style=flat-square)](https://t.me/aiogram_live)
[![Supported python versions](https://img.shields.io/pypi/pyversions/aiogram.svg?style=flat-square)](https://pypi.python.org/pypi/aiogram)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-8.0-blue.svg?style=flat-square&logo=telegram)](https://core.telegram.org/bots/api)
[![MIT License](https://img.shields.io/pypi/l/aiogram.svg?style=flat-square)](https://opensource.org/licenses/MIT)

This is just a project template for writing telegram bots. The project has linter, logger, docker, dot-env configured.

## Features

- SQLite (user info storage)
- custom aiogram middlewares ([middlewares.py](app/bot_controller/middlewares.py))
- custom aiogram router ([router.py](app/bot_controller/router.py))

## Command list

- `/help` - view all commands
- `/start` - base command for user registration
- `/hello` - just hello command
- `/user_info` - just hello command

## How to run

### Without Docker:

- Make virtual environment
- Install package requirements
- Create `.env` or set env-variables as you like (example: [.env.default](.env.default))
- Run it! :)

### With Docker

- Create `.env` or set env-variables as you like (example: [.env.default](.env.default)
  and see [docker-compose.yml](docker-compose.yml))
- Run it! :)

## Development tools

More helpful commands in [Makefile](Makefile).