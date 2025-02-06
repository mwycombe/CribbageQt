# cribbagestartup.py
# 7/21/2020 cloned from peggersstartup.py
#
#####################################################
#                                                   #
#   Locates/confirms database                       #
#   User can select new location, use existing      #
#   dbms location.                                  #
#                                                   #
#####################################################

# System imports
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox as mbx
# from tkinter import filedialog as fdg
import sys as sys
import os as os
# from tkinter.messagebox import askokcancel
# replace tkinter with PySide6

from PySide6 import QtWidgets as qtw
from PySide6 import  QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtWidgets import QMessageBox

from sqlobject import *

# Personal imports
import cribbageconfig as cfg
from player import Player
from club import Club
from tourney import Tourney
from accessPlayers import AccessPlayers
from accessTourneys import AccessTourneys
from accessResults import AccessResults
from accessClubs import AccessClubs


class CribbageStartup ():

    # define class method so initDbms can be called without
    # instantiating an instance



    @classmethod
    def initGlobalCfg(cls):
        
        # search baseDir for a sqlite3 file - i.e. a dbms
        # make sure we are positioned at the appropriate directory
        # everyone that needs dmbs initialization calls here
        #
        print('initDbms')
        
        cfg.appTitle = ''
        cfg.dbmsDirectory = ''
        cfg.dbmsName = ''
        cfg.season = ''
        cfg.reportDirectory = ''
        cfg.debug = True

        try:
            dbmsCfg = open('cribbage.cfg')      # this is the master config file
        except FileNotFoundError:
            print ('Unable to locate Cribbage.cfg\n Terminating')
            sys.exit(-1)
        print ('Config file found')
        # iterate through the cfg file and strip out the values for each name in <name> = <value>
        for line in dbmsCfg:
            print (line)
            eName = line.split(sep='=')[0].strip()
            eValue = line.split(sep='=')[1].strip()
            # if eName == 'title':
            #     cfg.appTitle = eValue
            if eName == 'clubNumber':
                cfg.clubNumber = int(eValue)
            elif eName == 'dbmsDirectory':
                cfg.dbmsDirectory = eValue
            elif eName == 'dbms':
                cfg.dbmsName = eValue
            elif eName == 'season':
                cfg.season = eValue
            elif eName == 'reportDirectory':
                cfg.reportDirectory = eValue
            elif eName == 'debug':
                if eValue == 'yes':
                    cfg.debug = True
            elif eName == 'playersdebug':
                if eValue == 'yes':
                    cfg.playersdebug = True
            elif eName == 'tourneysdebug':
                if eValue == 'yes':
                    cfg.tourneysdebug = True
            elif eName == 'resultsdebug':
                if eValue == 'yes':
                    cfg.resultsdebug = True
            elif eName == 'reportsdebug':
                if eValue == 'yes':
                    cfg.reportsdebug = True

        # and go to where the data base is located - ?? why??
##        os.chdir(cfg.dbmsDirectory)
        # close out the config file
        dbmsCfg.close()

        # this is good to continue for debugging for future seasons
        print ('Current directory: ' + cfg.dbmsDirectory)
        # print ('appTitle:= ' + cfg.appTitle)
        print ('dbmsDirectory:= ' + cfg.dbmsDirectory)
        print ('dbmsName:= ' + cfg.dbmsName)
        print ('season:= ' + cfg.season)
        print ('clubNumber:= ' + str(cfg.clubNumber))

    @classmethod
    def initDbms(cls):
        print ('QMessageBox...')
        # result = QMessageBox.question(None, 'Use this database?', cfg.dbmsName)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText('Use ' + cfg.dbmsDirectory + cfg.dbmsName + ' ?')
        msgBox.setWindowTitle('Check dbms name')
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        result = msgBox.exec()
        if result != QMessageBox.Ok:
            sys.exit('Wrong data base in use')
        else:
            print ('QMessageBox dropped thru')

        # see if we can connect to the database
        try:
            # validate where we are trying to connect to the database
            print('In try block')
            print('Connecting to: ' + cfg.dbmsDirectory + cfg.dbmsName)
            connection_string = 'sqlite:' + cfg.dbmsDirectory + cfg.dbmsName
            print ('connection_string:= ' + connection_string)
            conn = connectionForURI(connection_string)
            sqlhub.processConnection = conn     # make available to all classses
            # none of these widgets yet exist so promote the
            # action to the higher level
        except:
            print ('Unable to locate data base - terminating')
            sys._exit(-1)

        # global reference variables
        cfg.ap = AccessPlayers()
        cfg.ar = AccessResults()
        cfg.at = AccessTourneys()
        cfg.ac = AccessClubs()

        # init stackedWidgets dictionary
        # this defines which widget page the activity is loaded
        # into the stackedWidget layout
        # cfg.stackedActivityDict['playersActivityPage', 0]
        # cfg.stackedActivityDict['tourneysActivityPage', 1]
        # cfg.stackedActivityDict['resultsActivityPage', 2]
        # cfg.stackedActivityDict['reportsActivityPage', 3]

        cfg.clubRecord = cfg.ac.clubByNumber(cfg.clubNumber)[0]      # returns one club record in a list
        print (type(cfg.clubRecord))
        cfg.clubId = cfg.clubRecord.id
        cfg.clubName = cfg.clubRecord.clubName
        cfg.clubNumber = cfg.clubRecord.clubNumber
        cfg.clubLocation = cfg.clubRecord.location
        cfg.reportDirectory = cfg.clubRecord.reportDirectory
        cfg.clubCount = len(cfg.ap.allActivePlayers(cfg.clubRecord))

        # init screen hdr with retrieved information

        cfg.main = cfg.screenDict['masterwindow']
        cfg.main.hdrClubName = cfg.clubName
        cfg.main.hdrClubNumber = str(cfg.clubNumber)
        cfg.main.hdrSeason = cfg.season
        cfg.main.hdrActivePlayerCount = cfg.clubCount

        if cfg.debug == True:
            print('clubId:= ' + str(cfg.clubId))
            print('clubName:= ' + cfg.clubName)
            print('clubLocation:= ' + cfg.clubLocation)
            print ('reportDirectory:= ' + cfg.reportDirectory)
            print('clubCount:= ' + str(cfg.clubCount))

        CribbageStartup.createPlayersXref()
        CribbageStartup.createTourneyXref()
        CribbageStartup.createClubXref()

    @classmethod
    def createPlayersXref(cls):
        # cross-refs used to build results screens
        cfg.playerXref = {p.id: p.LastName + ', ' + p.FirstName for p in list(Player.select())}
        for p in cfg.playerXref.items():
            print ('playerXref:', p)
        cfg.playerRefx = {v: k for k, v in cfg.playerXref.items()}

    @classmethod
    def createClubXref(cls):
        cfg.clubXref = {x[0]: x[1] for x in cfg.ac.clubXref()}

    @classmethod
    def createTourneyXref(cls):
        #  {tid: tno}
        cfg.tourneyXref = {x.id : x.TourneyNumber for x in cfg.at.allTourneysForClubBySeason(cfg.clubRecord, cfg.season)}
        print ('tourneyXref: ', cfg.tourneyXref)
        # {tno : tid}
        cfg.tourneyRefx = { v:k for k, v in cfg.tourneyXref.items() }
    #************************************************************
    #   call startup for command line start

    def __init__(parent):
        print('In startup ....')


    # if 'window' not in cfg.screenDict:
    # 	print('Empty screenDict')
    # 	cfg.screenDict['window'] = window
    # 	print('screenDict[window]: ')
    # 	print(cfg.screenDict['window'])


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = qtw.QMainWindow()
    window.show()
    CribbageStartup.initGlobalCfg()
    CribbageStartup.initDbms()
 
