from package.ui.mainwindow_ui import Ui_MainWindow
from package.ui import error_dialog_ui
from package.ui import reading_dialog_ui
from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QMainWindow, QDialog, QPushButton
from PyQt6.QtCore import QEvent, Qt
import qdarktheme
from package.manga import get_manga, get_chapter_id, get_chapter, get_page 


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        qdarktheme.setup_theme()

        self.page_count = 0
        self.chapter_image = None
        self.ui.read_button = None
        self.ui.search_chapter_box = None
        self.chapter = []
        self.lang: str = "en"
        self.manga_title: str = ''
        self.search_title : str = ''
        self.search_chapter: str = ''
        self.chapter_id: str = ''

        self.ui.search_box.installEventFilter(self)
        self.ui.en_button.clicked.connect(lambda: self.set_lang("en"))
        self.ui.ptbr_button.clicked.connect(lambda: self.set_lang("pt-br"))

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

                self.chapter_id, self.manga_title = self.manga_search(self.search_chapter)

                if self.chapter_id != None:
                    self.spawn_read_button()

                self.ui.result_label.setText(f"The manga title is: {self.manga_title}\nThe chapter ID is: {self.chapter_id}")

                self.ui.search_chapter_box.clearFocus()

                return True

        return False


    def spawn_chapter_box(self):
        if self.ui.search_chapter_box != None:
            return
        
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


    def spawn_read_button(self):
        self.ui.read_button = QtWidgets.QPushButton(parent=self.ui.centralwidget)
        self.ui.read_button.setGeometry(QtCore.QRect(350, 400, 100, 35))
        self.ui.read_button.setObjectName("read_button")
        self.ui.read_button.setText("Read chapter")

        self.ui.read_button.clicked.connect(self.read_chapter)

        self.ui.read_button.show()

    
    def manga_search(self, chapter_index: str):
        self.page_count = 0
        manga_chapter = None
        manga_title = None
        
        try:
            manga_id = get_manga(self.search_title)
            manga_chapter, manga_title = get_chapter_id(chapter_index, manga_id, self.lang)
        except IndexError as e:
            self.error_message("Error: Manga not found!", e)
        except TypeError as e:
            self.error_message("Error: Chapter not found!", e)
        if manga_chapter == None:
            self.error_message("Error: Chapter not found!")

        return manga_chapter, manga_title


    def error_message(self, message: str, error_type: Exception = None):
        dialog = QDialog()
        ui = error_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        dialog.setWindowTitle(message)

        exception = error_type.__str__().capitalize()
        ui.label.setText(f"{message}\n\nException: {exception}")

        dialog.exec()


    def read_chapter(self):
        dialog = QDialog()
        ui = reading_dialog_ui.Ui_Dialog()
        ui.setupUi(dialog)

        self.chapter = get_chapter(self.chapter_id)

        self.set_page(ui)

        ui.next_button.clicked.connect(lambda: self.next_page(ui))   
        ui.back_button.clicked.connect(lambda: self.back_page(ui)) 

        dialog.exec()


    def next_page(self, ui):
        self.page_count += 1
        self.set_page(ui)


    def back_page(self, ui):
        self.page_count -= 1
        self.set_page(ui)

    def set_page(self, ui):
        try:    
            self.chapter_image = get_page(self.chapter[self.page_count])
            ui.page_number.setText(f"{self.page_count + 1}/{len(self.chapter)}")
        except IndexError as e:
            self.error_message("Error: No more pages!", e)
            self.page_count -= 1

        ui.page_image.setPixmap(self.chapter_image)


    def set_lang(self, lang: str):
        self.lang = lang
