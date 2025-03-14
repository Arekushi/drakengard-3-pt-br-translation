start:
	python main.py

generate:
	python main.py builder generate

install:
	python main.py manager install

install-local:
	python main.py manager install --local

uninstall:
	python main.py manager uninstall

generate-install:
	python main.py builder generate
	python main.py manager install --local

make-translation-folder:
	python main.py builder make-translation-folder

translate:
	python main.py builder translate
