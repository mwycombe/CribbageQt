# Form implementation generated from reading ui file 'resultsActivityPanel.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_resultsactivitypanel(object):
    def setupUi(self, resultsactivitypanel):
        resultsactivitypanel.setObjectName("resultsactivitypanel")
        resultsactivitypanel.resize(711, 161)
        font = QtGui.QFont()
        font.setPointSize(12)
        resultsactivitypanel.setFont(font)
        self.resultsactivitywidget = QtWidgets.QWidget(parent=resultsactivitypanel)
        self.resultsactivitywidget.setGeometry(QtCore.QRect(0, 0, 711, 161))
        self.resultsactivitywidget.setObjectName("resultsactivitywidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.resultsactivitywidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(15, 10, 681, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)

        self.retranslateUi(resultsactivitypanel)
        QtCore.QMetaObject.connectSlotsByName(resultsactivitypanel)

    def retranslateUi(self, resultsactivitypanel):
        _translate = QtCore.QCoreApplication.translate
        resultsactivitypanel.setWindowTitle(_translate("resultsactivitypanel", "Cribbage Grass Roots"))
        self.label_2.setText(_translate("resultsactivitypanel", "F3   Create new result for selected player"))
        self.label.setText(_translate("resultsactivitypanel", "F2   Edit results for selected player"))
        self.label_3.setText(_translate("resultsactivitypanel", "F4   Complete the delete request"))
        self.label_4.setText(_translate("resultsactivitypanel", "F10 Save the results as entered"))
        self.label_5.setText(_translate("resultsactivitypanel", "Esc Quit what you are doing"))
        self.label_6.setText(_translate("resultsactivitypanel", "F9   Removew the selected results from tourney"))
        self.label_7.setText(_translate("resultsactivitypanel", "F11 Force save of partial or diff. results"))
