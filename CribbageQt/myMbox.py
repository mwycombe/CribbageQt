import os
import sys

from PySide6 import QtCore, QtWidgets,QtGui

from PySide6.QtWidgets import QMessageBox, QApplication, QWidget, QPushButton

class MyClass():

    @classmethod
    def show_info_messagebox(cls):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("Information ")


        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # start the app
        retval = msg.exec()

app = QApplication(sys.argv)
# w = QWidget()
# w.show()

MyClass.show_info_messagebox()

# start the app
sys.exit(app.exec())