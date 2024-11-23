.PHONY: static

docker_compose_path = "docker-compose.yml"

DC = docker-compose -f $(docker_compose_path)


format: # format your code according to project linter tools
	poetry run black .
	poetry run isort .

lint:
	poetry run black --check app
	poetry run isort --check app
	poetry run flake8 --inline-quotes '"'
	@# For some reason, mypy and pylint fails to resolve PYTHONPATH, set manually.
	PYTHONPATH=./app poetry run pylint app
	#PYTHONPATH=./app poetry run mypy --namespace-packages --show-error-codes app --check-untyped-defs --ignore-missing-imports --show-traceback

safety:
	@# Ignore 62044 / CVE-2024-22190, we're not using GitPython
    # Ignore 70612 / CVE-2019-8341, Jinja2 is a safety dep, not ours
	poetry run safety check --ignore 63687 --ignore 70612

app-up: # Up the project using docker-compose
	$(DC) up -d --build

down: # Down the project using docker-compose
	$(DC) down
