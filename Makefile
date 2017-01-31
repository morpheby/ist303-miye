
requirements.log: requirements.txt
	pip install -r requirements.txt > $@

init: requirements.log
	

dist: init
	pyinstaller
