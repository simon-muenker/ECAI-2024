.PHONY: install run

install:
	@python3 -m pip install -r requirements.txt

run:
	@python3 main.py
