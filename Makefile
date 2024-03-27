.PHONY: install run

install:
	@python3 -m pip install -r requirements.txt

run_prediction:
	cd prediction && python3 __main__.py
