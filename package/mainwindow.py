from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QEvent, Qt
from package.ui.mainwindow_ui import Ui_MainWindow
from package.manga import get_manga

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.search_title : str = ""
        self.ui.search_box.installEventFilter(self)

        self.show()


    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress and obj is self.ui.search_box:
            if event.key() == Qt.Key.Key_Return and self.ui.search_box.hasFocus():
                self.search_title = self.ui.search_box.toPlainText()
                self.ui.result_label.setText((get_manga(self.search_title)).__str__())

                return True

        return False
