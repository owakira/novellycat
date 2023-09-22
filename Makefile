.PHONY: run
run:
	poetry run python -m src

.PHONY: lint
lint:
	poetry run ruff check .

.PHONY: test
test:
	poetry run pytest -vv

.PHONY: test-cov
test-cov:
	poetry run pytest --cov-report=html --show-capture=no
