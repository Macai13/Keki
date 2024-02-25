run:
	python main.py

ds:
	python.exe -m PyQt6.uic.pyuic designer\mainwindow.ui -o package\ui\mainwindow_ui.py
	python.exe -m PyQt6.uic.pyuic designer\error_dialog.ui -o package\ui\error_dialog_ui.py
	python.exe -m PyQt6.uic.pyuic designer\reading_dialog.ui -o package\ui\reading_dialog_ui.py