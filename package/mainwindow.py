from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QEvent, Qt
from package.ui.mainwindow_ui import Ui_MainWindow
from package.manga import get_manga, get_chapter

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.search_chapter_box = None
        self.search_title : str = ''
        self.search_chapter: str = ''

        self.ui.search_box.installEventFilter(self)

        self.show()


    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress and obj is self.ui.search_box:
            if event.key() == Qt.Key.Key_Return:
                self.search_title = self.ui.search_box.toPlainText()

                self.spawn_chapter_box()

                self.ui.search_box.clearFocus()
                self.ui.search_chapter_box.setFocus()

                return True
            
        if event.type() == QEvent.Type.KeyPress and obj is self.ui.search_chapter_box:
            if event.key() == Qt.Key.Key_Return:
                self.search_chapter = self.ui.search_chapter_box.toPlainText()

                chapter = self.manga_search(self.search_chapter)

                self.ui.result_label.setText(f"The chapter ID is: {chapter}")

                return True

        return False


    def spawn_chapter_box(self):
        self.ui.search_chapter_label = QtWidgets.QLabel(parent=self.ui.centralwidget)
        self.ui.search_chapter_label.setGeometry(QtCore.QRect(217, 90, 211, 16))
        self.ui.search_chapter_label.setObjectName("search_chapter_label")
        self.ui.search_chapter_label.setText("What chapter?")
        
        self.ui.search_chapter_box = QtWidgets.QPlainTextEdit(parent=self.ui.centralwidget)
        self.ui.search_chapter_box.setGeometry(QtCore.QRect(210, 110, 341, 41))
        self.ui.search_chapter_box.setObjectName("search_chapter_box")

        self.ui.search_chapter_box.installEventFilter(self)

        self.ui.search_chapter_box.show()
        self.ui.search_chapter_label.show()

    
    def manga_search(self, chapter_index: str):
        manga_id = get_manga(self.search_title)
        manga_chapter = get_chapter(chapter_index, manga_id)

        return manga_chapter
