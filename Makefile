.PHONY: requirements
requirements:
	python3 -m pip install -r requirements.txt

.PHONY: format
format:
	ruff format

.PHONY: check
check:
	ruff check