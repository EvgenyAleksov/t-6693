PORT ?= 10000
MANAGE := uv run python manage.py

install:
	uv sync

build:
	./build.sh

setup:
	db-clean install migrate

db-clean:
	@rm db.sqlite3 || true

migrate:
	@$(MANAGE) migrate

1


shell:
	@$(MANAGE) shell_plus --ipython

lint:
	uv run ruff check t_6693

dev:
	$(MANAGE) runserver

start:
	uv run gunicorn --workers=5 --bind=0.0.0.0:$(PORT) t_6693.wsgi

render-start:
	gunicorn --workers=5 --bind=0.0.0.0:$(PORT) t_6693.wsgi
