.PHONY: all run clean

all: window_linux.py mobile.py app.py

run: mobile.py
	python mobile.py

clean:
	rm -f __pycache__

.PHONY: flask-setup flask-run

flask-setup:
	pip install Flask

flask-run: app.py flask-setup
	python app.py
