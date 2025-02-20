# Form implementation generated from reading ui file 'CribbageV1_1_Results_Activity.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_ResultsActivity(object):
    def setupUi(self, ResultsActivity):
        ResultsActivity.setObjectName("ResultsActivity")
        ResultsActivity.resize(1114, 879)
        font = QtGui.QFont()
        font.setPointSize(12)
        ResultsActivity.setFont(font)
        self.TopContainer = QtWidgets.QWidget(parent=ResultsActivity)
        self.TopContainer.setGeometry(QtCore.QRect(0, 0, 1111, 231))
        self.TopContainer.setObjectName("TopContainer")
        self.sessionPanel = QtWidgets.QFrame(parent=self.TopContainer)
        self.sessionPanel.setGeometry(QtCore.QRect(10, 20, 1091, 201))
        self.sessionPanel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.sessionPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sessionPanel.setLineWidth(3)
        self.sessionPanel.setObjectName("sessionPanel")
        self.clubPanel = QtWidgets.QFrame(parent=self.sessionPanel)
        self.clubPanel.setGeometry(QtCore.QRect(20, 20, 301, 171))
        self.clubPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.clubPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubPanel.setLineWidth(2)
        self.clubPanel.setObjectName("clubPanel")
        self.layoutWidget = QtWidgets.QWidget(parent=self.clubPanel)
        self.layoutWidget.setGeometry(QtCore.QRect(14, 20, 123, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.clubNumberLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.clubNumberLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubNumberLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubNumberLabel.setLineWidth(2)
        self.clubNumberLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.clubNumberLabel.setObjectName("clubNumberLabel")
        self.verticalLayout_3.addWidget(self.clubNumberLabel)
        self.clubNameLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.clubNameLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubNameLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubNameLabel.setLineWidth(2)
        self.clubNameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.clubNameLabel.setObjectName("clubNameLabel")
        self.verticalLayout_3.addWidget(self.clubNameLabel)
        self.clubPlayersLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.clubPlayersLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubPlayersLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubPlayersLabel.setLineWidth(2)
        self.clubPlayersLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.clubPlayersLabel.setObjectName("clubPlayersLabel")
        self.verticalLayout_3.addWidget(self.clubPlayersLabel)
        self.clubSeasonLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.clubSeasonLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubSeasonLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubSeasonLabel.setLineWidth(2)
        self.clubSeasonLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.clubSeasonLabel.setObjectName("clubSeasonLabel")
        self.verticalLayout_3.addWidget(self.clubSeasonLabel)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.clubPanel)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 22, 141, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.clubNumber = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.clubNumber.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        self.clubNumber.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubNumber.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubNumber.setLineWidth(2)
        self.clubNumber.setObjectName("clubNumber")
        self.verticalLayout_4.addWidget(self.clubNumber)
        self.clubName = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.clubName.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        self.clubName.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubName.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubName.setLineWidth(2)
        self.clubName.setObjectName("clubName")
        self.verticalLayout_4.addWidget(self.clubName)
        self.clubPlayers = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.clubPlayers.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        self.clubPlayers.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubPlayers.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubPlayers.setLineWidth(2)
        self.clubPlayers.setObjectName("clubPlayers")
        self.verticalLayout_4.addWidget(self.clubPlayers)
        self.clubSeason = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.clubSeason.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        self.clubSeason.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubSeason.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubSeason.setLineWidth(2)
        self.clubSeason.setObjectName("clubSeason")
        self.verticalLayout_4.addWidget(self.clubSeason)
        self.resultsActivityPanel = QtWidgets.QFrame(parent=self.sessionPanel)
        self.resultsActivityPanel.setGeometry(QtCore.QRect(340, 20, 741, 171))
        self.resultsActivityPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.resultsActivityPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.resultsActivityPanel.setLineWidth(2)
        self.resultsActivityPanel.setObjectName("resultsActivityPanel")
        self.frame = QtWidgets.QFrame(parent=self.resultsActivityPanel)
        self.frame.setGeometry(QtCore.QRect(30, 10, 641, 161))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame.setObjectName("frame")
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(16, 11, 611, 141))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.clubFrameLabel = QtWidgets.QLabel(parent=self.sessionPanel)
        self.clubFrameLabel.setGeometry(QtCore.QRect(26, 9, 41, 20))
        self.clubFrameLabel.setAutoFillBackground(True)
        self.clubFrameLabel.setStyleSheet("opacity : 255")
        self.clubFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.clubFrameLabel.setObjectName("clubFrameLabel")
        self.resultsActivityFrameLabel = QtWidgets.QLabel(parent=self.sessionPanel)
        self.resultsActivityFrameLabel.setGeometry(QtCore.QRect(350, 8, 63, 20))
        self.resultsActivityFrameLabel.setAutoFillBackground(True)
        self.resultsActivityFrameLabel.setStyleSheet("opacity: 1.0;")
        self.resultsActivityFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsActivityFrameLabel.setObjectName("resultsActivityFrameLabel")
        self.SessionFrameLabel = QtWidgets.QLabel(parent=self.TopContainer)
        self.SessionFrameLabel.setGeometry(QtCore.QRect(20, 10, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SessionFrameLabel.setFont(font)
        self.SessionFrameLabel.setAutoFillBackground(True)
        self.SessionFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SessionFrameLabel.setObjectName("SessionFrameLabel")

        self.retranslateUi(ResultsActivity)
        QtCore.QMetaObject.connectSlotsByName(ResultsActivity)

    def retranslateUi(self, ResultsActivity):
        _translate = QtCore.QCoreApplication.translate
        ResultsActivity.setWindowTitle(_translate("ResultsActivity", "Cribbage Grass Roots"))
        self.clubNumberLabel.setText(_translate("ResultsActivity", "Club Number:"))
        self.clubNameLabel.setText(_translate("ResultsActivity", "Club Name:"))
        self.clubPlayersLabel.setText(_translate("ResultsActivity", "Players in Club:"))
        self.clubSeasonLabel.setText(_translate("ResultsActivity", "Season:"))
        self.clubNumber.setText(_translate("ResultsActivity", "TextLabel"))
        self.clubName.setText(_translate("ResultsActivity", "TextLabel"))
        self.clubPlayers.setText(_translate("ResultsActivity", "TextLabel"))
        self.clubSeason.setText(_translate("ResultsActivity", "TextLabel"))
        self.label.setText(_translate("ResultsActivity", "F2   Edit results for selected player"))
        self.label_2.setText(_translate("ResultsActivity", "F3   Create new result for selected player"))
        self.label_3.setText(_translate("ResultsActivity", "F4   Complete the delete request"))
        self.label_6.setText(_translate("ResultsActivity", "F9   Removew the selected results from tourney"))
        self.label_4.setText(_translate("ResultsActivity", "F10 Save the results as entered"))
        self.label_7.setText(_translate("ResultsActivity", "F11 Force save of partial or diff. results"))
        self.label_5.setText(_translate("ResultsActivity", "Esc Quit what you are doing"))
        self.clubFrameLabel.setText(_translate("ResultsActivity", "Club"))
        self.resultsActivityFrameLabel.setText(_translate("ResultsActivity", "Activity"))
        self.SessionFrameLabel.setText(_translate("ResultsActivity", "Session"))
