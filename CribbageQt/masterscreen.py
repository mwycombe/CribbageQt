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
from ctrlVariables import StringVar, IntVar, DoubleVar
from seniorsconfig import screenDict


# from seniorsconfig import screenDict


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
    #   These are initialized in cribbagestartup.py
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

        #   build and register top container
        self.TopContainer = QtWidgets.QWidget(parent=cfg.screenDict['masterwindow'])
        self.TopContainer.setObjectName("TopContainer")
        cfg.screenDict['toppanel'] = self.TopContainer

        #   build and register session panel
        self.sessionPanel = QtWidgets.QFrame(parent=cfg.screenDict['toppanel'])
        self.sessionPanel.setGeometry(QtCore.QRect(10, 20, 1091, 201))
        self.sessionPanel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.sessionPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sessionPanel.setLineWidth(3)
        self.sessionPanel.setObjectName("sessionPanel")
        cfg.screenDict['sessionpanel'] = self.sessionPanel

        # build and register club panel
        self.clubPanel = QtWidgets.QFrame(parent=cfg.screenDict['sessionpanel'])
        self.clubPanel.setGeometry(QtCore.QRect(20, 20, 301, 171))
        self.clubPanel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.clubPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.clubPanel.setLineWidth(2)
        self.clubPanel.setObjectName("clubPanel")
        cfg.screenDict['clubpanel'] = self.clubPanel

        #   build out club panel
        self.label_8 = QtWidgets.QLabel(parent=cfg.screenDict['clubpanel'])
        self.label_8.setGeometry(QtCore.QRect(10, 20, 63, 20))
        self.label_8.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_8.setLineWidth(2)
        self.label_8.setObjectName("label_8")
        self.label_17 = QtWidgets.QLabel(parent=cfg.screenDict['clubpanel'])
        self.label_17.setGeometry(QtCore.QRect(10, 95, 61, 21))
        self.label_17.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_17.setLineWidth(2)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=cfg.screenDict['clubpanel'])
        self.label_18.setGeometry(QtCore.QRect(10, 60, 63, 20))
        self.label_18.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_18.setLineWidth(2)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=cfg.screenDict['clubpanel'])
        self.label_19.setGeometry(QtCore.QRect(10, 130, 61, 20))
        self.label_19.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_19.setLineWidth(2)
        self.label_19.setObjectName("label_19")
        self.hdrClubNumber = QtWidgets.QLabel(parent=cfg.screenDict['clubpanel'])
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
        self.hdrClubNumber.setText(str(cfg.clubNumber))

        self.hdrClubName = QtWidgets.QLabel(parent=cfg.screenDict['clubpanel'])
        self.hdrClubName.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.hdrClubName.setStyleSheet("color: rgb(85, 0, 255);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.hdrClubName.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.hdrClubName.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hdrClubName.setLineWidth(2)
        self.hdrClubName.setObjectName("hdrClubName")
        self.hdrClubName.setText(cfg.clubName)

        self.hdrActivePlayerCount = QtWidgets.QLabel(parent=cfg.screenDict['clubpanel'])
        self.hdrActivePlayerCount.setGeometry(QtCore.QRect(80, 95, 31, 20))
        self.hdrActivePlayerCount.setStyleSheet("color: rgb(85, 0, 255);\n"
                                                "background-color: rgb(255, 255, 255);")
        self.hdrActivePlayerCount.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.hdrActivePlayerCount.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hdrActivePlayerCount.setLineWidth(2)
        self.hdrActivePlayerCount.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.hdrActivePlayerCount.setObjectName("hdrActivePlayerCount")
        self.hdrActivePlayerCount.setText(str(cfg.clubCount))

        self.hdrSeason = QtWidgets.QLabel(parent=cfg.screenDict['clubpanel'])
        self.hdrSeason.setGeometry(QtCore.QRect(80, 130, 71, 20))
        self.hdrSeason.setStyleSheet("color: rgb(85, 0, 255);\n"
                                     "background-color: rgb(255, 255, 255);")
        self.hdrSeason.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.hdrSeason.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hdrSeason.setLineWidth(2)
        self.hdrSeason.setObjectName("hdrSeason")
        self.hdrSeason.setText(cfg.season)

        self.activityPanel = QtWidgets.QFrame(parent=cfg.screenDict['sessionpanel'])
        self.activityPanel.setGeometry(QtCore.QRect(340, 20, 741, 171))
        self.activityPanel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.activityPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.activityPanel.setLineWidth(2)
        self.activityPanel.setObjectName("activityPanel")
        cfg.screenDict['activitypanel'] = self.activityPanel    # this is the blank activity panel

        self.clubFrameLabel = QtWidgets.QLabel(parent=cfg.screenDict['sessionpanel'])
        self.clubFrameLabel.setGeometry(QtCore.QRect(26, 10, 41, 20))
        self.clubFrameLabel.setAutoFillBackground(True)
        self.clubFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.clubFrameLabel.setObjectName("clubFrameLabel")
        self.activityFrameLabel = QtWidgets.QLabel(parent=cfg.screenDict['sessionpanel'])
        self.activityFrameLabel.setGeometry(QtCore.QRect(350, 10, 63, 20))
        self.activityFrameLabel.setAutoFillBackground(True)
        self.activityFrameLabel.setStyleSheet("opacity: 1.0;")
        self.activityFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.activityFrameLabel.setObjectName("activityFrameLabel")
        self.SessionFrameLabel = QtWidgets.QLabel(parent=cfg.screenDict['toppanel'])
        self.SessionFrameLabel.setGeometry(QtCore.QRect(20, 10, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SessionFrameLabel.setFont(font)
        self.SessionFrameLabel.setAutoFillBackground(True)
        self.SessionFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SessionFrameLabel.setObjectName("SessionFrameLabel")

        ##############################################
        #       start of tab widgets
        #       this is the 'notebook'
        ##############################################
        self.tabWidget = QtWidgets.QTabWidget(parent=self.TopContainer)
        self.tabWidget.setGeometry(QtCore.QRect(0, 220, 1101, 691))
        self.tabWidget.setObjectName("tabWidget")
        cfg.screenDict['notebook'] = self.tabWidget

        #   capture tabchange signal
        self.tabWidget.currentChanged.connect(self.tabchange)
        self.tabWidget.currentChanged.connect(cfg.screenDict['uimaster'].tabChange)

        #############################################
        #       set up tourneys tab
        #############################################
        self.playersTab = QtWidgets.QWidget()
        self.playersTab.setAutoFillBackground(True)
        self.playersTab.setObjectName("playersTab")
        self.playerTabPanel = QtWidgets.QFrame(parent=self.playersTab)
        self.playerTabPanel.setGeometry(QtCore.QRect(10, 10, 1071, 641))
        self.playerTabPanel.setAutoFillBackground(True)
        self.playerTabPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.playerTabPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.playerTabPanel.setLineWidth(2)
        self.playerTabPanel.setObjectName("playerTabPanel")
        self.newPlayerFrame = QtWidgets.QFrame(parent=self.playerTabPanel)
        self.newPlayerFrame.setGeometry(QtCore.QRect(420, 80, 451, 511))
        self.newPlayerFrame.setAutoFillBackground(True)
        self.newPlayerFrame.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.newPlayerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.newPlayerFrame.setLineWidth(2)
        self.newPlayerFrame.setObjectName("newPlayerFrame")
        self.newPlayerLabel = QtWidgets.QLabel(parent=self.newPlayerFrame)
        self.newPlayerLabel.setGeometry(QtCore.QRect(30, 20, 91, 20))
        self.newPlayerLabel.setObjectName("newPlayerLabel")
        self.NewPlayerLabelFrame = QtWidgets.QFrame(parent=self.newPlayerFrame)
        self.NewPlayerLabelFrame.setGeometry(QtCore.QRect(30, 80, 122, 421))
        self.NewPlayerLabelFrame.setAutoFillBackground(True)
        self.NewPlayerLabelFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.NewPlayerLabelFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.NewPlayerLabelFrame.setLineWidth(2)
        self.NewPlayerLabelFrame.setObjectName("NewPlayerLabelFrame")
        self.formLayout = QtWidgets.QFormLayout(self.NewPlayerLabelFrame)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.firstNameLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.firstNameLabel.setEnabled(True)
        self.firstNameLabel.setAutoFillBackground(True)
        self.firstNameLabel.setScaledContents(False)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.verticalLayout.addWidget(self.firstNameLabel)
        self.lastNameLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.verticalLayout.addWidget(self.lastNameLabel)
        self.streetLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.streetLabel.setObjectName("streetLabel")
        self.verticalLayout.addWidget(self.streetLabel)
        self.cityLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.cityLabel.setObjectName("cityLabel")
        self.verticalLayout.addWidget(self.cityLabel)
        self.stateLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.stateLabel.setObjectName("stateLabel")
        self.verticalLayout.addWidget(self.stateLabel)
        self.zipLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.zipLabel.setObjectName("zipLabel")
        self.verticalLayout.addWidget(self.zipLabel)
        self.phoneLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.phoneLabel.setObjectName("phoneLabel")
        self.verticalLayout.addWidget(self.phoneLabel)
        self.emailLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.emailLabel.setObjectName("emailLabel")
        self.verticalLayout.addWidget(self.emailLabel)
        self.accNumberLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.accNumberLabel.setObjectName("accNumberLabel")
        self.verticalLayout.addWidget(self.accNumberLabel)
        self.expiresLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.expiresLabel.setObjectName("expiresLabel")
        self.verticalLayout.addWidget(self.expiresLabel)
        self.joinedLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.joinedLabel.setObjectName("joinedLabel")
        self.verticalLayout.addWidget(self.joinedLabel)
        self.activeLabel = QtWidgets.QLabel(parent=self.NewPlayerLabelFrame)
        self.activeLabel.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.activeLabel.setObjectName("activeLabel")
        self.verticalLayout.addWidget(self.activeLabel)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verticalLayout)
        self.layoutWidget = QtWidgets.QWidget(parent=self.newPlayerFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(146, 90, 152, 408))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.firstNameEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.firstNameEntry.setObjectName("firstNameEntry")
        self.verticalLayout_2.addWidget(self.firstNameEntry)
        self.lastNameEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lastNameEntry.setObjectName("lastNameEntry")
        self.verticalLayout_2.addWidget(self.lastNameEntry)
        self.streetEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.streetEntry.setObjectName("streetEntry")
        self.verticalLayout_2.addWidget(self.streetEntry)
        self.cityEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.cityEntry.setObjectName("cityEntry")
        self.verticalLayout_2.addWidget(self.cityEntry)
        self.stateEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.stateEntry.setObjectName("stateEntry")
        self.verticalLayout_2.addWidget(self.stateEntry)
        self.zipEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.zipEntry.setObjectName("zipEntry")
        self.verticalLayout_2.addWidget(self.zipEntry)
        self.phoneEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.phoneEntry.setObjectName("phoneEntry")
        self.verticalLayout_2.addWidget(self.phoneEntry)
        self.emailEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.emailEntry.setObjectName("emailEntry")
        self.verticalLayout_2.addWidget(self.emailEntry)
        self.accNumberEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.accNumberEntry.setObjectName("accNumberEntry")
        self.verticalLayout_2.addWidget(self.accNumberEntry)
        self.expiresEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.expiresEntry.setObjectName("expiresEntry")
        self.verticalLayout_2.addWidget(self.expiresEntry)
        self.joinedEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.joinedEntry.setObjectName("joinedEntry")
        self.verticalLayout_2.addWidget(self.joinedEntry)
        self.activeEntry = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.activeEntry.setObjectName("activeEntry")
        self.verticalLayout_2.addWidget(self.activeEntry)
        self.existingPlayersPanel = QtWidgets.QFrame(parent=self.playerTabPanel)
        self.existingPlayersPanel.setGeometry(QtCore.QRect(30, 10, 341, 631))
        self.existingPlayersPanel.setAutoFillBackground(True)
        self.existingPlayersPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.existingPlayersPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.existingPlayersPanel.setLineWidth(2)
        self.existingPlayersPanel.setObjectName("existingPlayersPanel")
        self.label = QtWidgets.QLabel(parent=self.existingPlayersPanel)
        self.label.setGeometry(QtCore.QRect(50, 10, 111, 20))
        self.label.setObjectName("label")
        self.activePlayerLabel = QtWidgets.QLabel(parent=self.existingPlayersPanel)
        self.activePlayerLabel.setGeometry(QtCore.QRect(40, 50, 81, 20))
        self.activePlayerLabel.setObjectName("activePlayerLabel")
        self.showAllPlayers = QtWidgets.QCheckBox(parent=self.existingPlayersPanel)
        self.showAllPlayers.setGeometry(QtCore.QRect(140, 50, 87, 24))
        self.showAllPlayers.setObjectName("showAllPlayers")
        self.playerList = QtWidgets.QListWidget(parent=self.existingPlayersPanel)
        self.playerList.setGeometry(QtCore.QRect(30, 80, 231, 541))
        self.playerList.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.playerList.setLineWidth(3)
        self.playerList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.playerList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.playerList.setSelectionRectVisible(True)
        self.playerList.setObjectName("playerList")
        self.tabWidget.addTab(self.playersTab, "")
        #############################################
        #       here's where the player tab is added to the notebook
        #############################################

        #############################################
        #       set up tourneys tab
        #############################################
        self.tourneysTab = QtWidgets.QWidget()
        self.tourneysTab.setAutoFillBackground(True)
        self.tourneysTab.setObjectName("tourneysTab")
        self.tourneyTabPanel = QtWidgets.QFrame(parent=self.tourneysTab)
        self.tourneyTabPanel.setGeometry(QtCore.QRect(10, 10, 1041, 641))
        self.tourneyTabPanel.setAutoFillBackground(True)
        self.tourneyTabPanel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tourneyTabPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tourneyTabPanel.setLineWidth(2)
        self.tourneyTabPanel.setObjectName("tourneyTabPanel")
        self.TourneysFrame = QtWidgets.QFrame(parent=self.tourneyTabPanel)
        self.TourneysFrame.setGeometry(QtCore.QRect(10, 10, 1031, 631))
        self.TourneysFrame.setAutoFillBackground(True)
        self.TourneysFrame.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.TourneysFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.TourneysFrame.setLineWidth(2)
        self.TourneysFrame.setObjectName("TourneysFrame")
        self.F6TourneyFrame = QtWidgets.QFrame(parent=self.TourneysFrame)
        self.F6TourneyFrame.setGeometry(QtCore.QRect(10, 20, 381, 61))
        self.F6TourneyFrame.setAutoFillBackground(True)
        self.F6TourneyFrame.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.F6TourneyFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.F6TourneyFrame.setLineWidth(2)
        self.F6TourneyFrame.setObjectName("F6TourneyFrame")
        self.tourneyF6EnterResultsLabel = QtWidgets.QLabel(parent=self.F6TourneyFrame)
        self.tourneyF6EnterResultsLabel.setGeometry(QtCore.QRect(10, 10, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.tourneyF6EnterResultsLabel.setFont(font)
        self.tourneyF6EnterResultsLabel.setStyleSheet("\n"
                                                      "color: rgb(65, 161, 5);")
        self.tourneyF6EnterResultsLabel.setLineWidth(-5)
        self.tourneyF6EnterResultsLabel.setObjectName("tourneyF6EnterResultsLabel")
        self.ExistingTourneysPanel = QtWidgets.QFrame(parent=self.TourneysFrame)
        self.ExistingTourneysPanel.setGeometry(QtCore.QRect(10, 91, 261, 541))
        self.ExistingTourneysPanel.setAutoFillBackground(True)
        self.ExistingTourneysPanel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.ExistingTourneysPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.ExistingTourneysPanel.setLineWidth(2)
        self.ExistingTourneysPanel.setObjectName("ExistingTourneysPanel")
        self.trnyNoHdr = QtWidgets.QLabel(parent=self.ExistingTourneysPanel)
        self.trnyNoHdr.setGeometry(QtCore.QRect(8, 30, 41, 41))
        self.trnyNoHdr.setWordWrap(True)
        self.trnyNoHdr.setObjectName("trnyNoHdr")
        self.trnyDataHdr = QtWidgets.QLabel(parent=self.ExistingTourneysPanel)
        self.trnyDataHdr.setGeometry(QtCore.QRect(70, 50, 41, 20))
        self.trnyDataHdr.setObjectName("trnyDataHdr")
        self.trnyDateHdr = QtWidgets.QLabel(parent=self.ExistingTourneysPanel)
        self.trnyDateHdr.setGeometry(QtCore.QRect(150, 30, 41, 41))
        self.trnyDateHdr.setWordWrap(True)
        self.trnyDateHdr.setObjectName("trnyDateHdr")
        self.label_4 = QtWidgets.QLabel(parent=self.TourneysFrame)
        self.label_4.setGeometry(QtCore.QRect(20, 82, 151, 20))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.listOfTourneys = QtWidgets.QListWidget(parent=self.TourneysFrame)
        self.listOfTourneys.setGeometry(QtCore.QRect(10, 170, 231, 461))
        self.listOfTourneys.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listOfTourneys.setLineWidth(2)
        self.listOfTourneys.setObjectName("listOfTourneys")
        self.NewTourneyPanel = QtWidgets.QFrame(parent=self.TourneysFrame)
        self.NewTourneyPanel.setGeometry(QtCore.QRect(420, 170, 341, 101))
        self.NewTourneyPanel.setAutoFillBackground(True)
        self.NewTourneyPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.NewTourneyPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.NewTourneyPanel.setLineWidth(2)
        self.NewTourneyPanel.setObjectName("NewTourneyPanel")
        self.newTourneyNumberLabel = QtWidgets.QLabel(parent=self.NewTourneyPanel)
        self.newTourneyNumberLabel.setGeometry(QtCore.QRect(10, 30, 161, 20))
        self.newTourneyNumberLabel.setObjectName("newTourneyNumberLabel")
        self.newTourneyDateLabel = QtWidgets.QLabel(parent=self.NewTourneyPanel)
        self.newTourneyDateLabel.setGeometry(QtCore.QRect(10, 60, 151, 20))
        self.newTourneyDateLabel.setObjectName("newTourneyDateLabel")
        self.newTourneyNumberEntry = QtWidgets.QLineEdit(parent=self.NewTourneyPanel)
        self.newTourneyNumberEntry.setGeometry(QtCore.QRect(180, 30, 51, 26))
        self.newTourneyNumberEntry.setObjectName("newTourneyNumberEntry")
        self.newTourneyDateEntry = QtWidgets.QLineEdit(parent=self.NewTourneyPanel)
        self.newTourneyDateEntry.setGeometry(QtCore.QRect(180, 60, 141, 26))
        self.newTourneyDateEntry.setObjectName("newTourneyDateEntry")
        self.newTourneyFrameLabel = QtWidgets.QLabel(parent=self.TourneysFrame)
        self.newTourneyFrameLabel.setGeometry(QtCore.QRect(430, 160, 101, 20))
        self.newTourneyFrameLabel.setAutoFillBackground(True)
        self.newTourneyFrameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.newTourneyFrameLabel.setObjectName("newTourneyFrameLabel")
        self.F6TourneyFrame.raise_()
        self.ExistingTourneysPanel.raise_()
        self.label_4.raise_()
        self.NewTourneyPanel.raise_()
        self.newTourneyFrameLabel.raise_()
        self.listOfTourneys.raise_()
        self.label_2 = QtWidgets.QLabel(parent=self.tourneyTabPanel)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 63, 20))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tourneysTab, "")
        ####################################
        #       here's where the tourney tab is added to the 'notebook'
        ####################################

        #############################################
        #       set up results tab
        #############################################
        self.resultsTab = QtWidgets.QWidget()
        self.resultsTab.setAutoFillBackground(True)
        self.resultsTab.setObjectName("resultsTab")
        self.resultsTabPanel = QtWidgets.QFrame(parent=self.resultsTab)
        self.resultsTabPanel.setGeometry(QtCore.QRect(10, 10, 1071, 641))
        self.resultsTabPanel.setAutoFillBackground(True)
        self.resultsTabPanel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.resultsTabPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.resultsTabPanel.setObjectName("resultsTabPanel")
        self.resultsPanel = QtWidgets.QFrame(parent=self.resultsTabPanel)
        self.resultsPanel.setGeometry(QtCore.QRect(10, 10, 1091, 631))
        self.resultsPanel.setAutoFillBackground(True)
        self.resultsPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.resultsPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.resultsPanel.setLineWidth(2)
        self.resultsPanel.setObjectName("resultsPanel")
        self.resultsHdrPanel = QtWidgets.QFrame(parent=self.resultsPanel)
        self.resultsHdrPanel.setGeometry(QtCore.QRect(20, 20, 241, 91))
        self.resultsHdrPanel.setAutoFillBackground(True)
        self.resultsHdrPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.resultsHdrPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.resultsHdrPanel.setLineWidth(2)
        self.resultsHdrPanel.setObjectName("resultsHdrPanel")
        self.label_9 = QtWidgets.QLabel(parent=self.resultsHdrPanel)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 101, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.resultsHdrPanel)
        self.label_10.setGeometry(QtCore.QRect(10, 36, 91, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.resultsHdrPanel)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 63, 20))
        self.label_11.setObjectName("label_11")
        self.tourneyHdrDate = QtWidgets.QLabel(parent=self.resultsHdrPanel)
        self.tourneyHdrDate.setGeometry(QtCore.QRect(130, 10, 91, 20))
        self.tourneyHdrDate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tourneyHdrDate.setText("")
        self.tourneyHdrDate.setObjectName("tourneyHdrDate")
        self.tourneyHdrNumber = QtWidgets.QLabel(parent=self.resultsHdrPanel)
        self.tourneyHdrNumber.setGeometry(QtCore.QRect(131, 35, 31, 20))
        self.tourneyHdrNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tourneyHdrNumber.setText("")
        self.tourneyHdrNumber.setObjectName("tourneyHdrNumber")
        self.tourneyHdrCount = QtWidgets.QLabel(parent=self.resultsHdrPanel)
        self.tourneyHdrCount.setGeometry(QtCore.QRect(130, 60, 31, 20))
        self.tourneyHdrCount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tourneyHdrCount.setText("")
        self.tourneyHdrCount.setObjectName("tourneyHdrCount")
        self.frame_2 = QtWidgets.QFrame(parent=self.resultsPanel)
        self.frame_2.setGeometry(QtCore.QRect(300, 20, 261, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 63, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 60, 63, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(90, 10, 31, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(140, 10, 51, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(210, 10, 31, 20))
        self.label_16.setObjectName("label_16")
        self.spreadPlusValue = QtWidgets.QLabel(parent=self.frame_2)
        self.spreadPlusValue.setGeometry(QtCore.QRect(88, 33, 41, 20))
        self.spreadPlusValue.setStyleSheet("\n"
                                           "background-color: rgb(187, 255, 215)\n"
                                           "")
        self.spreadPlusValue.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.spreadPlusValue.setText("")
        self.spreadPlusValue.setObjectName("spreadPlusValue")
        self.spreadMinusValue = QtWidgets.QLabel(parent=self.frame_2)
        self.spreadMinusValue.setGeometry(QtCore.QRect(139, 34, 41, 20))
        self.spreadMinusValue.setStyleSheet("background-color: rgb(255, 211, 205);")
        self.spreadMinusValue.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.spreadMinusValue.setText("")
        self.spreadMinusValue.setObjectName("spreadMinusValue")
        self.spreadDiffValue = QtWidgets.QLabel(parent=self.frame_2)
        self.spreadDiffValue.setGeometry(QtCore.QRect(210, 35, 31, 20))
        self.spreadDiffValue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spreadDiffValue.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.spreadDiffValue.setText("")
        self.spreadDiffValue.setObjectName("spreadDiffValue")
        self.skunkPlusValue = QtWidgets.QLabel(parent=self.frame_2)
        self.skunkPlusValue.setGeometry(QtCore.QRect(88, 58, 41, 20))
        self.skunkPlusValue.setStyleSheet("background-color: rgb(187, 255, 215);")
        self.skunkPlusValue.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.skunkPlusValue.setText("")
        self.skunkPlusValue.setObjectName("skunkPlusValue")
        self.skunkMinusValue = QtWidgets.QLabel(parent=self.frame_2)
        self.skunkMinusValue.setGeometry(QtCore.QRect(140, 59, 41, 20))
        self.skunkMinusValue.setStyleSheet("background-color: rgb(255, 211, 205);")
        self.skunkMinusValue.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.skunkMinusValue.setText("")
        self.skunkMinusValue.setObjectName("skunkMinusValue")
        self.skunkDiffValue = QtWidgets.QLabel(parent=self.frame_2)
        self.skunkDiffValue.setGeometry(QtCore.QRect(209, 58, 31, 20))
        self.skunkDiffValue.setStyleSheet("\n"
                                          "background-color: rgb(255, 255, 255);")
        self.skunkDiffValue.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.skunkDiffValue.setText("")
        self.skunkDiffValue.setObjectName("skunkDiffValue")
        self.selectedPlayersPanel = QtWidgets.QFrame(parent=self.resultsPanel)
        self.selectedPlayersPanel.setGeometry(QtCore.QRect(20, 130, 241, 491))
        self.selectedPlayersPanel.setAutoFillBackground(True)
        self.selectedPlayersPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.selectedPlayersPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.selectedPlayersPanel.setLineWidth(2)
        self.selectedPlayersPanel.setObjectName("selectedPlayersPanel")
        self.label_7 = QtWidgets.QLabel(parent=self.selectedPlayersPanel)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 41, 20))
        self.label_7.setObjectName("label_7")
        self.listOfPlayerNames = QtWidgets.QLabel(parent=self.selectedPlayersPanel)
        self.listOfPlayerNames.setGeometry(QtCore.QRect(60, 10, 91, 20))
        self.listOfPlayerNames.setObjectName("listOfPlayerNames")
        self.listOfPoints = QtWidgets.QListWidget(parent=self.selectedPlayersPanel)
        self.listOfPoints.setGeometry(QtCore.QRect(10, 30, 31, 451))
        self.listOfPoints.setObjectName("listOfPoints")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.selectedPlayersPanel)
        self.listWidget_2.setGeometry(QtCore.QRect(60, 30, 151, 451))
        self.listWidget_2.setObjectName("listWidget_2")
        self.tourneyResultsPanel = QtWidgets.QFrame(parent=self.resultsPanel)
        self.tourneyResultsPanel.setGeometry(QtCore.QRect(300, 130, 541, 491))
        self.tourneyResultsPanel.setAutoFillBackground(True)
        self.tourneyResultsPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.tourneyResultsPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tourneyResultsPanel.setLineWidth(2)
        self.tourneyResultsPanel.setObjectName("tourneyResultsPanel")
        self.listOfResulsNames = QtWidgets.QListWidget(parent=self.tourneyResultsPanel)
        self.listOfResulsNames.setGeometry(QtCore.QRect(10, 30, 161, 451))
        self.listOfResulsNames.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.listOfResulsNames.setLineWidth(3)
        self.listOfResulsNames.setObjectName("listOfResulsNames")
        self.label_23 = QtWidgets.QLabel(parent=self.tourneyResultsPanel)
        self.label_23.setGeometry(QtCore.QRect(60, 6, 63, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.tourneyResultsPanel)
        self.label_24.setGeometry(QtCore.QRect(193, 10, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.tourneyResultsPanel)
        self.label_25.setGeometry(QtCore.QRect(228, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.tourneyResultsPanel)
        self.label_26.setGeometry(QtCore.QRect(274, 10, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.tourneyResultsPanel)
        self.label_27.setGeometry(QtCore.QRect(325, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.tourneyResultsPanel)
        self.label_28.setGeometry(QtCore.QRect(450, 10, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(parent=self.tourneyResultsPanel)
        self.label_29.setGeometry(QtCore.QRect(414, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(parent=self.tourneyResultsPanel)
        self.label_31.setGeometry(QtCore.QRect(373, 10, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.listOfResultsGp = QtWidgets.QListWidget(parent=self.tourneyResultsPanel)
        self.listOfResultsGp.setGeometry(QtCore.QRect(180, 30, 41, 451))
        self.listOfResultsGp.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listOfResultsGp.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.listOfResultsGp.setLineWidth(2)
        self.listOfResultsGp.setObjectName("listOfResultsGp")
        self.listOfResultGw = QtWidgets.QListWidget(parent=self.tourneyResultsPanel)
        self.listOfResultGw.setGeometry(QtCore.QRect(220, 30, 41, 451))
        self.listOfResultGw.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listOfResultGw.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.listOfResultGw.setLineWidth(2)
        self.listOfResultGw.setObjectName("listOfResultGw")
        self.listOfResultsSprd = QtWidgets.QListWidget(parent=self.tourneyResultsPanel)
        self.listOfResultsSprd.setGeometry(QtCore.QRect(260, 30, 61, 451))
        self.listOfResultsSprd.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listOfResultsSprd.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.listOfResultsSprd.setLineWidth(2)
        self.listOfResultsSprd.setObjectName("listOfResultsSprd")
        self.listOfResultsTkn = QtWidgets.QListWidget(parent=self.tourneyResultsPanel)
        self.listOfResultsTkn.setGeometry(QtCore.QRect(320, 30, 41, 451))
        self.listOfResultsTkn.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listOfResultsTkn.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.listOfResultsTkn.setLineWidth(2)
        self.listOfResultsTkn.setObjectName("listOfResultsTkn")
        self.listOfResultsCash = QtWidgets.QListWidget(parent=self.tourneyResultsPanel)
        self.listOfResultsCash.setGeometry(QtCore.QRect(360, 30, 51, 451))
        self.listOfResultsCash.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listOfResultsCash.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.listOfResultsCash.setLineWidth(2)
        self.listOfResultsCash.setObjectName("listOfResultsCash")
        self.listOfResultsGvn = QtWidgets.QListWidget(parent=self.tourneyResultsPanel)
        self.listOfResultsGvn.setGeometry(QtCore.QRect(410, 30, 41, 451))
        self.listOfResultsGvn.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listOfResultsGvn.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.listOfResultsGvn.setLineWidth(2)
        self.listOfResultsGvn.setObjectName("listOfResultsGvn")
        self.listOfResultsOrder = QtWidgets.QListWidget(parent=self.tourneyResultsPanel)
        self.listOfResultsOrder.setGeometry(QtCore.QRect(450, 30, 41, 451))
        self.listOfResultsOrder.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listOfResultsOrder.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.listOfResultsOrder.setLineWidth(2)
        self.listOfResultsOrder.setObjectName("listOfResultsOrder")
        self.label_5 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 121, 20))
        self.label_5.setAutoFillBackground(True)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_6.setGeometry(QtCore.QRect(400, 120, 121, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.resultLinePlayerName = QtWidgets.QLabel(parent=self.resultsPanel)
        self.resultLinePlayerName.setGeometry(QtCore.QRect(590, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.resultLinePlayerName.setFont(font)
        self.resultLinePlayerName.setStyleSheet("color: rgb(122, 122, 122)")
        self.resultLinePlayerName.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.resultLinePlayerName.setObjectName("resultLinePlayerName")
        self.label_40 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_40.setGeometry(QtCore.QRect(970, 90, 31, 20))
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_41.setGeometry(QtCore.QRect(590, 60, 141, 20))
        self.label_41.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_42.setGeometry(QtCore.QRect(743, 60, 31, 20))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_43.setGeometry(QtCore.QRect(790, 60, 31, 20))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_44.setGeometry(QtCore.QRect(844, 60, 51, 20))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_45.setGeometry(QtCore.QRect(905, 60, 31, 20))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_46.setGeometry(QtCore.QRect(955, 60, 31, 20))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(parent=self.resultsPanel)
        self.label_47.setGeometry(QtCore.QRect(992, 60, 41, 20))
        self.label_47.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.resultLinePlayerGp = QtWidgets.QLineEdit(parent=self.resultsPanel)
        self.resultLinePlayerGp.setGeometry(QtCore.QRect(737, 90, 41, 21))
        self.resultLinePlayerGp.setMouseTracking(False)
        self.resultLinePlayerGp.setAcceptDrops(False)
        self.resultLinePlayerGp.setAutoFillBackground(True)
        self.resultLinePlayerGp.setObjectName("resultLinePlayerGp")
        self.resultLinePlayerGw = QtWidgets.QLineEdit(parent=self.resultsPanel)
        self.resultLinePlayerGw.setGeometry(QtCore.QRect(783, 90, 41, 21))
        self.resultLinePlayerGw.setAcceptDrops(False)
        self.resultLinePlayerGw.setAutoFillBackground(True)
        self.resultLinePlayerGw.setObjectName("resultLinePlayerGw")
        self.resultLinePlayerTkn = QtWidgets.QLineEdit(parent=self.resultsPanel)
        self.resultLinePlayerTkn.setGeometry(QtCore.QRect(900, 90, 41, 21))
        self.resultLinePlayerTkn.setAutoFillBackground(True)
        self.resultLinePlayerTkn.setObjectName("resultLinePlayerTkn")
        self.resultLinePlayerCash = QtWidgets.QLineEdit(parent=self.resultsPanel)
        self.resultLinePlayerCash.setGeometry(QtCore.QRect(950, 90, 41, 21))
        self.resultLinePlayerCash.setAutoFillBackground(True)
        self.resultLinePlayerCash.setObjectName("resultLinePlayerCash")
        self.resultLinePlayerSprd = QtWidgets.QLineEdit(parent=self.resultsPanel)
        self.resultLinePlayerSprd.setGeometry(QtCore.QRect(830, 90, 61, 21))
        self.resultLinePlayerSprd.setAutoFillBackground(True)
        self.resultLinePlayerSprd.setObjectName("resultLinePlayerSprd")
        self.resultLinePlayerGvn = QtWidgets.QLabel(parent=self.resultsPanel)
        self.resultLinePlayerGvn.setGeometry(QtCore.QRect(1000, 90, 31, 20))
        self.resultLinePlayerGvn.setAutoFillBackground(False)
        self.resultLinePlayerGvn.setStyleSheet("background-color: rgb(187, 255, 215)")
        self.resultLinePlayerGvn.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.resultLinePlayerGvn.setText("")
        self.resultLinePlayerGvn.setObjectName("resultLinePlayerGvn")
        self.label_3 = QtWidgets.QLabel(parent=self.resultsTabPanel)
        self.label_3.setGeometry(QtCore.QRect(30, 0, 91, 20))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.resultsTab, "")
        ############################################
        #       here's where the results tab is added to the 'notebook'
        ############################################

        #############################################
        #       set up reports tab
        #############################################

        self.reportsTab = QtWidgets.QWidget()
        self.reportsTab.setAutoFillBackground(True)
        self.reportsTab.setObjectName("reportsTab")
        self.reportsTabPanel = QtWidgets.QFrame(parent=self.reportsTab)
        self.reportsTabPanel.setGeometry(QtCore.QRect(10, 10, 1081, 651))
        self.reportsTabPanel.setAutoFillBackground(False)
        self.reportsTabPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.reportsTabPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.reportsTabPanel.setLineWidth(2)
        self.reportsTabPanel.setObjectName("reportsTabPanel")
        self.tourneysPanel = QtWidgets.QFrame(parent=self.reportsTabPanel)
        self.tourneysPanel.setGeometry(QtCore.QRect(10, 0, 201, 621))
        self.tourneysPanel.setAutoFillBackground(True)
        self.tourneysPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.tourneysPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.tourneysPanel.setLineWidth(3)
        self.tourneysPanel.setObjectName("tourneysPanel")
        self.listOfReportTourneys = QtWidgets.QListWidget(parent=self.tourneysPanel)
        self.listOfReportTourneys.setGeometry(QtCore.QRect(10, 20, 151, 571))
        self.listOfReportTourneys.setObjectName("listOfReportTourneys")
        self.reportButtonsPanel = QtWidgets.QFrame(parent=self.reportsTabPanel)
        self.reportButtonsPanel.setGeometry(QtCore.QRect(210, 0, 231, 621))
        self.reportButtonsPanel.setAutoFillBackground(True)
        self.reportButtonsPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.reportButtonsPanel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.reportButtonsPanel.setLineWidth(3)
        self.reportButtonsPanel.setObjectName("reportButtonsPanel")
        self.allReportsCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.allReportsCKB.setGeometry(QtCore.QRect(30, 70, 101, 24))
        self.allReportsCKB.setChecked(False)
        self.allReportsCKB.setObjectName("allReportsCKB")
        self.alphaCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.alphaCKB.setGeometry(QtCore.QRect(30, 150, 121, 24))
        self.alphaCKB.setObjectName("alphaCKB")
        self.battingAverageCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.battingAverageCKB.setGeometry(QtCore.QRect(30, 190, 191, 24))
        self.battingAverageCKB.setObjectName("battingAverageCKB")
        self.cashCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.cashCKB.setGeometry(QtCore.QRect(30, 230, 131, 24))
        self.cashCKB.setObjectName("cashCKB")
        self.individStatsCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.individStatsCKB.setGeometry(QtCore.QRect(30, 270, 161, 24))
        self.individStatsCKB.setObjectName("individStatsCKB")
        self.nationalAvgesCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.nationalAvgesCKB.setGeometry(QtCore.QRect(30, 310, 181, 24))
        self.nationalAvgesCKB.setObjectName("nationalAvgesCKB")
        self.qtrDropCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.qtrDropCKB.setGeometry(QtCore.QRect(30, 350, 131, 24))
        self.qtrDropCKB.setObjectName("qtrDropCKB")
        self.qtrFullCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.qtrFullCKB.setGeometry(QtCore.QRect(30, 390, 121, 24))
        self.qtrFullCKB.setObjectName("qtrFullCKB")
        self.skunkCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.skunkCKB.setGeometry(QtCore.QRect(30, 430, 121, 24))
        self.skunkCKB.setObjectName("skunkCKB")
        self.tourneyCKB = QtWidgets.QCheckBox(parent=self.reportButtonsPanel)
        self.tourneyCKB.setGeometry(QtCore.QRect(30, 470, 131, 24))
        self.tourneyCKB.setObjectName("tourneyCKB")
        self.runReportsButton = QtWidgets.QPushButton(parent=self.reportButtonsPanel)
        self.runReportsButton.setGeometry(QtCore.QRect(20, 510, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.runReportsButton.setFont(font)
        self.runReportsButton.setFlat(False)
        self.runReportsButton.setObjectName("runReportsButton")
        self.label_36 = QtWidgets.QLabel(parent=self.reportsTab)
        self.label_36.setGeometry(QtCore.QRect(30, -2, 71, 20))
        self.label_36.setAutoFillBackground(True)
        self.label_36.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(parent=self.reportsTab)
        self.label_37.setGeometry(QtCore.QRect(230, 0, 63, 20))
        self.label_37.setAutoFillBackground(True)
        self.label_37.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.tabWidget.addTab(self.reportsTab, "")
        ##########################################
        #       here's where the reports tab is added to the 'notebook'
        ##########################################

        self.tabWidget.raise_()
        self.sessionPanel.raise_()
        self.SessionFrameLabel.raise_()


        self.retranslateUi(Master)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Master)

    def retranslateUi(self, Master):
        _translate = QtCore.QCoreApplication.translate
        Master.setWindowTitle("Cribbage Grass Roots")
        self.label_8.setText("Club No:")
        self.label_17.setText("Active:")
        self.label_18.setText("Name:")
        self.label_19.setText("Season:")
        self.hdrClubNumber.setText("100")
        self.hdrClubName.setText("Century Peggers")
        self.hdrActivePlayerCount.setText("30")
        self.hdrSeason.setText("2024-25")
        self.clubFrameLabel.setText("Club")
        self.activityFrameLabel.setText("Activity")
        self.SessionFrameLabel.setText("Session")
        self.newPlayerLabel.setText("New Player")
        self.firstNameLabel.setText("First Name")
        self.lastNameLabel.setText("Last Name")
        self.streetLabel.setText("Street")
        self.cityLabel.setText("City")
        self.stateLabel.setText("State")
        self.zipLabel.setText("Zip")
        self.phoneLabel.setText("Phone")
        self.emailLabel.setText("Email")
        self.accNumberLabel.setText("ACC Number")
        self.expiresLabel.setText("Expires")
        self.joinedLabel.setText("Joined")
        self.activeLabel.setText("Active")
        self.label.setText("Existing Players")
        self.activePlayerLabel.setText("* = Active")
        self.showAllPlayers.setText("Show All")
        self.playerList.setSortingEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.playersTab), "Players")
        self.tourneyF6EnterResultsLabel.setText("F6 - Enter results for selected tourney")
        self.trnyNoHdr.setText("Trny No.")
        self.trnyDataHdr.setText("Data")
        self.trnyDateHdr.setText("Trny Date")
        self.label_4.setText("Existing Tournaments")
        self.newTourneyNumberLabel.setText("New Tourney Number")
        self.newTourneyDateLabel.setText("New Tourney Date")
        self.newTourneyFrameLabel.setText("New Tourney")
        self.label_2.setText("Tourneys")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tourneysTab), "Tourneys")
        self.label_9.setText("Tourney Date")
        self.label_10.setText("Tourney No.")
        self.label_11.setText("Count")
        self.label_12.setText("Spread")
        self.label_13.setText("Skunks")
        self.label_14.setText("Plus")
        self.label_15.setText("Minus")
        self.label_16.setText("Diff")
        self.label_7.setText("Points")
        self.listOfPlayerNames.setText("Player Name")
        self.label_23.setText("Names")
        self.label_24.setText("Gp")
        self.label_25.setText("Gw")
        self.label_26.setText("Sprd")
        self.label_27.setText("Tkn")
        self.label_28.setText("Order")
        self.label_29.setText("Gvn")
        self.label_31.setText("$\'s")
        self.label_5.setText("Selected Players")
        self.label_6.setText("Tourney Results")
        self.resultLinePlayerName.setText("TextLabel")
        self.label_41.setText("Name")
        self.label_42.setText("Gp")
        self.label_43.setText("Gw")
        self.label_44.setText("Sprd")
        self.label_45.setText("Tkn")
        self.label_46.setText("$\'s")
        self.label_47.setText("Gvn")
        self.label_3.setText("Results Panel")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resultsTab), "Results")
        self.allReportsCKB.setText("All Reports")
        self.alphaCKB.setText("Alpha Report")
        self.battingAverageCKB.setText("Batting Average Report")
        self.cashCKB.setText("Cash Report")
        self.individStatsCKB.setText("Individ. Stats Report")
        self.nationalAvgesCKB.setText("National Avges Reports")
        self.qtrDropCKB.setText("Qtr Drop Report")
        self.qtrFullCKB.setText("Qtr Full Report")
        self.skunkCKB.setText("Skunk Report")
        self.tourneyCKB.setText("Tourney Report")
        self.runReportsButton.setText("Run Selected Reports")
        self.label_36.setText("Tourneys")
        self.label_37.setText("Reports")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reportsTab), "Reports")

        # build the notebook in the lower frame tabPanel
        # replace with QtTabWidget definition
        # self.notebook = ttk.Notebook(self)
        # self.notebook.grid(row=1, column=0,
        #                    sticky='news')

        # register notebook panel for tab builders to reference
        # print('Register notebook')
        # cfg.screenDict['notebook'] = self.notebook


        #
        # self.notebook.bind("<<NotebookTabChanged>>",self.tabchange)
        # set this from the module that cares to track tabchanges
        # tabs within this notebook will register themselves

        cfg,screenDict['notebook'] = self.tabWidget

    @QtCore.Slot()
    def tabchange(self, index):
        print ('Tab changed:= ' + str(index))

if __name__ == '__main__':

    # fake set up global cfg module for all others to share just for standalone testing
    cfg.clubName = 'Century Peggers'
    cfg.clubId = 1
    cfg.clubNumber = 100
    tourneyDate = '2024-25'  # tourney selection will override this
    tourneyId = 0

    app = QtWidgets.QApplication(sys.argv)

    if 'window' not in cfg.screenDict:
        print(cfg.screenDict)
        Master = QtWidgets.QMainWindow()
        cfg.screenDict['window'] = Master



    app = MasterScreen(Master, 'Cribbage Qt')
    app.mainloop()