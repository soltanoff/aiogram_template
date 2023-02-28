FROM python:3.10-slim
ENV PYTHONUNBUFFERED 0

RUN apt-get update \
	&& pip install --upgrade --no-cache-dir pip \
	&& pip install --upgrade --no-cache-dir wheel \
	&& pip install --upgrade --no-cache-dir setuptools

COPY .. /src
WORKDIR /src

COPY ../.env.default ./.env

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]