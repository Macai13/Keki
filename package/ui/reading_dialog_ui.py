# Form implementation generated from reading ui file 'designer\reading_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1129, 884)
        Dialog.setMinimumSize(QtCore.QSize(1129, 884))
        Dialog.setMaximumSize(QtCore.QSize(1129, 884))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("designer\\../icons/mainwindow_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.page_image = QtWidgets.QLabel(parent=Dialog)
        self.page_image.setGeometry(QtCore.QRect(8, 15, 1111, 831))
        self.page_image.setText("")
        self.page_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.page_image.setObjectName("page_image")
        self.page_number = QtWidgets.QLabel(parent=Dialog)
        self.page_number.setGeometry(QtCore.QRect(564, 0, 49, 16))
        self.page_number.setText("")
        self.page_number.setObjectName("page_number")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(490, 850, 161, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button)
        self.next_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Keki - Reading"))
        self.back_button.setText(_translate("Dialog", "<"))
        self.next_button.setText(_translate("Dialog", ">"))
