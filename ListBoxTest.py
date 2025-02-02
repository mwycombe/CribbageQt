# Form implementation generated from reading ui file 'listBoxTest.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QListWidget




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 619)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 281, 61))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.selectionLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.selectionLabel.setGeometry(QtCore.QRect(580, 180, 161, 31))
        self.selectionLabel.setObjectName("selectionLabel")
        self.listSelection = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.listSelection.setGeometry(QtCore.QRect(750, 180, 161, 31))
        self.listSelection.setObjectName("listSelection")
        self.QListWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.QListWidget.setGeometry(QtCore.QRect(250, 220, 256, 192))
        self.QListWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listData = listData()
        self.QListWidget.addItems(self.listData.listData)

        self.filterObject = FunctionKeyFilter()
        self.QListWidget.installEventFilter(self.filterObject)

        self.QListWidget.doubleClicked.connect(self.itemDoubleClicked)
        # self.QListWidget.keyPressEvent.connect(QListWidget.keyPressEvent())

        self.QListWidget.setCurrentRow(0)
        self.QListWidget.setFocus()

    def itemDoubleClicked(self,listItem):
        print ('Was double clicked')
        print (self.QListWidget.currentItem().text())
        print (self.QListWidget.currentRow())
        self.listSelection.setText(self.QListWidget.currentItem().text())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Test area for ListBox emulation"))
        self.selectionLabel.setText(_translate("MainWindow", "Selection Made"))


class FunctionKeyFilter(QObject):
    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            # print(event.key())
            if event.key() == QtCore.Qt.Key_F1:
                print("F1 pressed")
            return False
        else:
            return True

class listData ():
    listData = ['Acai',
                'Apple',
                'Apricot',
                'Banana',
                'Blackberry',
                'Blueberry',
                'Casaba',
                'Cherry',
                'Fig',
                'Grape',
                'Guava',
                'Kiwi',
                'Lemon',
                'Mandarin',
                'Melon',
                'Nectarine',
                'Orange',
                'Peach',
                'Pear',
                'Quince'
                ]
    def getListData(self):
        return self.listData


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
