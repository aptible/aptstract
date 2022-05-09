SHELL := /bin/bash
PYTHON := . .venv/bin/activate && python
export BUNDLE_DIRECTORY := $(shell pwd)/bundles

install: .venv
	$(PYTHON) -m pip install -e .[dev]

build: install
	python -m build --wheel

.venv:
	python -m venv .venv

pretty: pretty_black pretty_isort

pretty_black:
	$(PYTHON) -m black .

pretty_isort:
	$(PYTHON) -m isort .


.PHONY: tests
tests: install pytest isort_check black_check

pytest:
	$(PYTHON) -m pytest

pytest_loud:
	$(PYTHON) -m pytest -s

isort_check:
	$(PYTHON) -m isort --check-only .

black_check:
	$(PYTHON) -m black . --check


pex:
	$(PYTHON) -m pex . --python-shebang="#!/usr/bin/env python3" --console-script aptstract -v -o aptstract.pex --disable-cache

pex_debug: pex
	rm -Rf temp || true
	mkdir temp
	cp aptstract.pex temp/aptstract.pex
	cd temp && unzip aptstract.pex

clean:
	rm -Rf temp || true
	rm -Rf .venv || true
