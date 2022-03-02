publish:
	python3 index.py | tee index.md
	
run:
	python3 index.py

install:
	pip3 install -r requirements.txt
