run:
	python main.py

ds:
	python.exe -m PyQt6.uic.pyuic designer\mainwindow.ui -o package\ui\mainwindow_ui.py