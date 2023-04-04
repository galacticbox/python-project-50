install:
	poetry install
	poetry add flake8
	poetry add pytest-cov

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gen_diff

test:
	poetry run pytest

check:
	poetry run flake8 gen_diff
	poetry run pytest

test-coverage:
	poetry run pytest --cov-report=xml --cov=gen_diff tests/