# aiogram bot template (skeleton)

[![\[Telegram\] aiogram live](https://img.shields.io/badge/telegram-aiogram-blue.svg?style=flat-square)](https://t.me/aiogram_live)
[![Supported python versions](https://img.shields.io/pypi/pyversions/aiogram.svg?style=flat-square)](https://pypi.python.org/pypi/aiogram)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-7.0-blue.svg?style=flat-square&logo=telegram)](https://core.telegram.org/bots/api)
[![MIT License](https://img.shields.io/pypi/l/aiogram.svg?style=flat-square)](https://opensource.org/licenses/MIT)

This is just a project template for writing telegram bots. The project has linter, logger, docker, dot-env configured.

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

### Bandit tool

[Bandit](https://github.com/PyCQA/bandit) is a tool designed to find common security issues in Python code. To do this
Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has
finished scanning all the files it generates a report.

```shell
bandit -r .
```

### flake8

[flake8](https://github.com/PyCQA/flake8) is a python tool that glues together pycodestyle, pyflakes, mccabe, and
third-party plugins to check the style and quality of some python code.

```shell
flake8 .
```