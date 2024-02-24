from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QEvent, Qt
from PyQt6.QtGui import QKeyEvent
from package.ui.mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.search_box.installEventFilter(self)

        self.show()


    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress and obj is self.ui.search_box:
            if event.key() == Qt.Key.Key_Return and self.ui.search_box.hasFocus():
                print('Enter pressed')

        return super().eventFilter(obj, event)
