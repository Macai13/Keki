from PyQt6.QtWidgets import QApplication
from package.mainwindow import MainWindow
import sys 

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
  
    app.exec()