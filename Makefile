PORT ?= 8000
MANAGE := uv run python manage.py

build:
	./build.sh

setup:
	db-clean install migrate

install:
	uv sync

db-clean:
	@rm db.sqlite3 || true

# migrate:
# 	@$(MANAGE) migrate

shell:
	@$(MANAGE) shell_plus --ipython

lint:
	uv run ruff check t_6693

dev:
	$(MANAGE) runserver

start:
	# uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) t_6693.wsgi
	uv run python -m gunicorn t_6693.asgi:application -k uvicorn.workers.UvicornWorker


render-start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) t_6693.wsgi
