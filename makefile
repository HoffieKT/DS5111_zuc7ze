
default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update:  env
	. env/bin/activate; pip install -r requirements.txt

lint: 
	. env/bin/activate; pylint clean_ids.py; echo $?

test: lint
	. env/bin/activate; pytest -vv tests
