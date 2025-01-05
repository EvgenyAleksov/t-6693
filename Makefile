PORT ?= 10000
MANAGE := uv run python manage.py

install:
	uv install

.PHONY: setup
setup: db-clean install migrate

migrate:
	@$(MANAGE) migrate


lint:
	uv run ruff check t_6693

dev:
	uv run ruff check t_6693
	$(MANAGE) runserver

start:
	uv run gunicorn --workers=5 --bind=0.0.0.0:$(PORT) t_6693.wsgi
