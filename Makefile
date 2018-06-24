
all: test

.PHONY: clean
clean:
	CLEAR_PATTERNS='*.pyc __pycache__ build dist *.egg-info'; \
	for PATTERN in $$CLEAR_PATTERNS; do \
		echo "find $$PWD -name $$PATTERN -delete"; \
		find $$PWD -name $$PATTERN -delete; \
	done

.PHONY: install
install: clean
	pip install -r requirements.txt

.PHONY: test
test: clean
	python ./attributedict/tests/

.PHONY: build
build: clean
	rm -rf ./dist && \
	python -m pip install --user --upgrade setuptools wheel && \
	python setup.py sdist bdist_wheel

.PHONY: dist
dist: build
	python -m pip install --user --upgrade twine && \
	twine upload dist/*

.PHONY: dist-dev
dist-dev: build
	python -m pip install --user --upgrade twine && \
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
