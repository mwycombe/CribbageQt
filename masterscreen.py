# masterscreen.py
#
#   11/4/2024 conversion to Qt from tkinter
#   7/20/2020 cloned from masterscreen.v2.ppy
#
#####################################################################
#
#   Creates root for the application and sets up empty notebook
#   ready for tabs to register themselves
#
#####################################################################
#
#   builds base frames in the root
#   header frame carries all cross-tab static fields some of which
#   get populated from tab actions
#
#####################################################################

# System imports
from PySide6 import QtCore, QtGui, QtWidgets
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox as mbx
# from tkinter import filedialog as fdg


from sqlobject import *

import sys as sys
import os as os

# Personal imports
import cribbageconfig as cfg
from club import Club
from player import Player
# from columnweights import ColumnWeights

class MasterScreen (object):

    @classmethod
    def wipeActivityPanel(cls):
        pass
        # this will be changed to show the blank activity panel and hid all others
        # any tab can call this to grid_remove all other activity panels
        # cfg.screenDict['playersactivity'].hide()
        # cfg.screenDict['tourneysactivity'].hide()
        # cfg.screenDict['resultsactivity'].hide()
        # cfg.screenDict['reportsactivity'].hide()

    def __init__ (self, parent, title):
        # super().__init__( parent)
        # self['text'] = 'Master'
        # self['relief'] = tk.RAISED
        # self.columnconfigure(0, weight=1, uniform='a')
        # self.rowconfigure(0, weight=1, uniform='a')
        # self.grid(row = 0, column = 0, sticky = 'nsew')

        print('MasterScreen started . . .')
        
        # register master screen
        # cfg.screenDict['master'] = self

        # make the columns stretchable
    # # control variables
    #   These are initialized in peggersstartup.py
    #
    #     cfg.clubName = Club.get(1).clubName
    #     cfg.clubNumber = Club.get(1).clubNumber
    #     cfg.clubId = Club.get(1).id
    #     cfg.clubCount = Player.select().count()

##        self.headerPanel = ttk.Frame (self,
##                                       height='3c',
##                                       width ='10c',
##                                       borderwidth='10',
##                                       relief = 'sunken')
##        self.headerPanel.grid(row=0, column=0, sticky='n')
##
##        # self register
##        print ('Register header')
##        cfg.screenDict['header'] = self.headerPanel
        # self.sessionHeader = tk.LabelFrame(self,
        #                                     # height = '3c',
        #                                     # width = '10c',
        #                                     relief = tk.RAISED,
        #                                     borderwidth = 5,
        #                                     text = 'Session'
        #                                     )
        # self.sessionHeader.columnconfigure(0, weight=1)
        # self.sessionHeader.columnconfigure(1, weight=1)
        # self.sessionHeader.grid(row = 0, column = 0, sticky='ew')
        #
        # # register both header subpanels
        # cfg.screenDict['session'] = self.sessionHeader
        #
        # self.clubPanel = tk.LabelFrame (self.sessionHeader,
        #                                  # height='3c',
        #                                  # width ='10c',
        #                                  borderwidth = 2,
        #                                  relief = tk.GROOVE,
        #                                  text = 'Club')
        # self.clubPanel.grid(row=0, column=0,
        #                     sticky = 'nsew')
        # # register club panel
        # cfg.screenDict['club'] = self.clubPanel
        #
        # self.activityPanel = tk.LabelFrame(self.sessionHeader,
        #                                     # height = '3c',
        #                                     # width = '10c',
        #                                     borderwidth = 2,
        #                                     relief = tk.GROOVE,
        #                                     text = 'Activity'
        #                                     )
        # self.activityPanel.grid(row = 0, column = 1,
        #                       stick = 'nsew')

        # register action panel
        # cfg.screenDict['activity'] = self.activityPanel
        #
        # the action panel is a 'scratch' area that notebook tabs can post
        # specific local information for that tab.

        # # weight as many columns as there are children - after children are created
        # ColumnWeights.columnWeights(self.sessionHeader,len(self.sessionHeader.winfo_children()))
        #
        #
        # self.clubNumber = tk.Label(self.clubPanel,
        #                             text='Club No.:    ',
        #                             relief='sunken',
        #                             borderwidth='2')
        # self.clubNumber.grid(row=0, column=0, sticky='w')
        #
        # self.clubNumberLabel = tk.Label(self.clubPanel,
        #                                  text=cfg.clubNumber,
        #                                  relief='sunken',
        #                                  borderwidth='2',
        #                                  font=('Helvetica', '10', 'bold'),
        #                                  foreground='blue')
        # self.clubNumberLabel.grid(row=0, column=1, sticky='w')
        # self.clubLabel = ttk.Label (self.clubPanel,
        #                             text = '    Name:  ',
        #                             relief = 'sunken',
        #                             borderwidth = '10p')
        # self.clubLabel.grid(row=0, column=2, sticky='w')
        #
        # self.clubNameLabel = ttk.Label (self.clubPanel,
        #                            text=cfg.clubName,
        #                            relief = 'sunken',
        #                            borderwidth='2c',
        #                            font = ('Helvetica', '10', 'bold'),
        #                            foreground='blue')
        # self.clubNameLabel.grid(row=0, column=3, sticky='w')
        #
        # self.countLabel = ttk.Label(self.clubPanel,
        #                             text='Players in Club   ',
        #                             relief='sunken',
        #                             borderwidth='10p')
        # self.countLabel.grid(row=1, column=0, sticky='w')
        #
        # self.memberCount = ttk.Label(self.clubPanel,
        #                              text=cfg.clubCount,
        #                              relief='sunken',
        #                              borderwidth='2c',
        #                              font=('Helvetica', '10', 'bold'),
        #                              foreground='blue')
        # self.memberCount.grid(row=1, column=1, sticky='w')
        #
        # self.seasonLabel = ttk.Label(self.clubPanel,
        #                              text='Season: ',
        #                              relief='sunken',
        #                              borderwidth='10p')
        # self.seasonLabel.grid(row=1, column = 2, sticky='w')
        #
        # self.season = ttk.Label(self.clubPanel,
        #                         text=cfg.season,
        #                         relief = 'sunken',
        #                         borderwidth = '2c',
        #                         font = ('Helvetica', '10', 'bold'),
        #                         foreground = 'blue')
        # self.season.grid(row=1, column = 3, sticky = 'w')
        self.sessionPanel = QtWidgets.QFrame(parent,TopContainer)
        self.sessionPanel.setGeometry(QtCore.QRect(10, 20, 1091, 201))
        self.sessionPanel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.sessionPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sessionPanel.setLineWidth(3)
        self.sessionPanel.setObjectName("sessionPanel")
        #   register sessionPanel
        cfg.screenDict['sessionpanel'] = self.sessionPanel

        self.clubPanel = QtWidgets.QFrame(parent=self.sessionPanel)
        self.clubPanel.setGeometry(QtCore.QRect(20, 20, 301, 171))
        self.clubPanel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubPanel.setLineWidth(2)
        self.clubPanel.setObjectName("clubPanel")
        #   register clubPanel
        cfg.screenDict['clubpanel'] = self.clubPanel

        self.label_8 = QtWidgets.QLabel(parent=self.clubPanel)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 63, 20))
        self.label_8.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_8.setLineWidth(2)
        self.label_8.setObjectName("label_8")
        self.label_17 = QtWidgets.QLabel(parent=self.clubPanel)
        self.label_17.setGeometry(QtCore.QRect(10, 95, 61, 21))
        self.label_17.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_17.setLineWidth(2)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.clubPanel)
        self.label_18.setGeometry(QtCore.QRect(10, 60, 63, 20))
        self.label_18.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_18.setLineWidth(2)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.clubPanel)
        self.label_19.setGeometry(QtCore.QRect(10, 130, 61, 20))
        self.label_19.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_19.setLineWidth(2)
        self.label_19.setObjectName("label_19")
        self.hdrClubNumber = QtWidgets.QLabel(parent=self.clubPanel)
        self.hdrClubNumber.setGeometry(QtCore.QRect(80, 20, 31, 20))
        self.hdrClubNumber.setAutoFillBackground(False)
        self.hdrClubNumber.setStyleSheet("color: rgb(85, 0, 255);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.hdrClubNumber.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.hdrClubNumber.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hdrClubNumber.setLineWidth(2)
        self.hdrClubNumber.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.hdrClubNumber.setObjectName("hdrClubNumber")
        self.hdrClubName = QtWidgets.QLabel(parent=self.clubPanel)
        self.hdrClubName.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.hdrClubName.setStyleSheet("color: rgb(85, 0, 255);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.hdrClubName.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.hdrClubName.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hdrClubName.setLineWidth(2)
        self.hdrClubName.setObjectName("hdrClubName")
        self.hdrActivePlayerCount = QtWidgets.QLabel(parent=self.clubPanel)
        self.hdrActivePlayerCount.setGeometry(QtCore.QRect(80, 95, 31, 20))
        self.hdrActivePlayerCount.setStyleSheet("color: rgb(85, 0, 255);\n"
                                                "background-color: rgb(255, 255, 255);")
        self.hdrActivePlayerCount.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.hdrActivePlayerCount.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hdrActivePlayerCount.setLineWidth(2)
        self.hdrActivePlayerCount.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.hdrActivePlayerCount.setObjectName("hdrActivePlayerCount")
        self.hdrSeason = QtWidgets.QLabel(parent=self.clubPanel)
        self.hdrSeason.setGeometry(QtCore.QRect(80, 130, 71, 20))
        self.hdrSeason.setStyleSheet("color: rgb(85, 0, 255);\n"
                                     "background-color: rgb(255, 255, 255);")
        self.hdrSeason.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.hdrSeason.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hdrSeason.setLineWidth(2)
        self.hdrSeason.setObjectName("hdrSeason")
        self.activityPanel = QtWidgets.QFrame(parent=self.sessionPanel)
        self.activityPanel.setGeometry(QtCore.QRect(340, 20, 741, 171))
        self.activityPanel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.activityPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.activityPanel.setLineWidth(2)
        self.activityPanel.setObjectName("activityPanel")
        #   register blank activity panel
        cfg.screenDict['activitytab'] = self.activityPanel

        self.clubFrameLabel = QtWidgets.QLabel(parent=self.sessionPanel)
        self.clubFrameLabel.setGeometry(QtCore.QRect(26, 10, 41, 20))
        self.clubFrameLabel.setAutoFillBackground(True)
        self.clubFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.clubFrameLabel.setObjectName("clubFrameLabel")
        self.activityFrameLabel = QtWidgets.QLabel(parent=self.sessionPanel)
        self.activityFrameLabel.setGeometry(QtCore.QRect(350, 10, 63, 20))
        self.activityFrameLabel.setAutoFillBackground(True)
        self.activityFrameLabel.setStyleSheet("opacity: 1.0;")
        self.activityFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.activityFrameLabel.setObjectName("activityFrameLabel")
        self.SessionFrameLabel = QtWidgets.QLabel(parent=self.TopContainer)
        self.SessionFrameLabel.setGeometry(QtCore.QRect(20, 10, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SessionFrameLabel.setFont(font)
        self.SessionFrameLabel.setAutoFillBackground(True)
        self.SessionFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SessionFrameLabel.setObjectName("SessionFrameLabel")



        # build the notebook in the lower frame tabPanel
        # replace with QtTabWidget definition
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0,
                           sticky='news')

        # register notebook panel for tab builders to reference
        print('Register notebook')
        cfg.screenDict['notebook'] = self.notebook


        #
        # self.notebook.bind("<<NotebookTabChanged>>",self.tabchange)
        # set this from the module that cares to track tabchanges
        # tabs within this notebook will register themselves

    def tabchange(self,event):
        print ('Tab changed:= ' + event)

if __name__ == '__main__':

    # fake set up global cfg module for all others to share just for standalone testing
    cfg.clubName = 'Century Peggers'
    cfg.clubId = 1
    cfg.clubNumber = 100
    tourneyDate = ''  # tourney selection will override this
    tourneyId = 0

    app = QtWidgets.QApplication(sys.argv)

    if 'window' not in cfg.screenDict:
        print(cfg.screenDict)
        Master = QtWidgets.QMainWindow()
        cfg.screenDict['window'] = Master



    app = MasterScreen(window)
    app.mainloop()