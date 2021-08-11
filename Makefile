VENV = search-local-breweries-with-google-maps-api

activate:
	$(VENV)\Scripts\activate

init:
	pip install -r requirements.txt

format: activate
	@black .

test: activate
	pytest

build-image: init
	docker build --tag $(VENV) .

run-image: build-image
	docker run --name $(VENV) -d -p 80:80 $(VENV)

copy: run-image
	timeout 180
	docker cp $(VENV):/Docker/breweries.csv .
