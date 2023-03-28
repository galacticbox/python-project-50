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
	poetry run flake8 gendiff

test:
	poetry run pytest

check:
	poetry run flake8 gendiff
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

gendiff:
	poetry run gendiff /home/sovolis/python-project-50/tests/fixtures/file1.json /home/sovolis/python-project-50/tests/fixtures/file2.json

.PHONY: gendiff