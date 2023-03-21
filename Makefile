install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

gendiff:
	poetry run gendiff /home/sovolis/python-project-50/gendiff/compare-files/file1.json /home/sovolis/python-project-50/gendiff/compare-files/file2.json

.PHONY: gendiff