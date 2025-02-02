
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QWidget, QApplication
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from PySide6.QtCore import QObject, Property, Signal

import sys as sys
import os as os

from sqlobject import *
from CribbageQt.UI.CribbageQt import Ui_MainCribbageWindow

# Personal imports
from ctrlVariables import StringVar, IntVar, DoubleVar
from cribbagestartup import CribbageStartup

import cribbageconfig 	as cfg

from masterscreenV3      import MasterScreen


if __name__ == '__main__':

    # call class level init methods
    print('Starting testmasterscreenV3...')
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()

    print('Window should show...')

    CribbageStartup.initDbms()
    CribbageStartup.createPlayersXref()
    CribbageStartup.createClubXref()
    CribbageStartup.createTourneyXref()

    print ('All actions completed')
# if 'window' not in cfg.screenDict:
# 	print('Empty screenDict')
# 	cfg.screenDict['window'] = window
# 	print('screenDict[window]: ')
# 	print(cfg.screenDict['window'])
    sys.exit(app.exec())
