start:
	python app.py

init:
	pip install -r requirements.txt

update-reqs:
	pipreqs . --force