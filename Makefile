PORT ?= 10000
MANAGE := uv run python manage.py

.PHONY: install
install:
	@uv install

.PHONY: test
test:
	@uv run pytest

.PHONY: setup
setup: db-clean install migrate

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	uv run ruff check t_6693

.PHONY: dev
dev:
	# uv build
	uv run ruff check t_6693
	$(MANAGE) runserver

start:
	$(RUN) @uv run gunicorn --workers=5 --bind=0.0.0.0:$(PORT) t_6693.wsgi
