FROM python:3.13-slim
ENV PYTHONUNBUFFERED 0

ENV buildDeps=' \
        build-essential \
        musl-dev \
        gcc \
    '

RUN apt-get update \
    && apt-get install -y $buildDeps --no-install-recommends \
    && pip install --upgrade --no-cache-dir pip wheel setuptools poetry

WORKDIR /app

# will be cached if no changes in this files
COPY poetry.lock /app/
COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction

COPY app /app

CMD [ "python", "main.py" ]