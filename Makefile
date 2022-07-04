
SRC_DIR = src/
TESTS_DIR = tests/

.PHONY: test test-cov

venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements-devel.txt

test: venv
	venv/bin/pytest

test-cov: venv
	venv/bin/pytest --cov $(SRC_DIR) --cov-report html
	if which sensible-browser >/dev/null; then \
	    sensible-browser htmlcov/index.html; \
	fi

black: venv
	venv/bin/black $(SRC_DIR) $(TESTS_DIR)

black-check: venv
	venv/bin/black --check $(SRC_DIR) $(TESTS_DIR)

pr: test black-check
