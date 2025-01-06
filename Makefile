PORT ?= 10000
MANAGE := uv run python manage.py

install:
	uv sync
	
build:
	./build.sh

.PHONY: setup
setup: db-clean install migrate

migrate:
	@$(MANAGE) migrate

lint:
	uv run ruff check t_6693

dev:
	uv run ruff check t_6693
	$(MANAGE) runserver

render-start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) t_6693.wsgi
