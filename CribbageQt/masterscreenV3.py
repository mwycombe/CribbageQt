# masterscreen.py
#
#   1/20/2025 add validaators and ctrl variables for all entry fields.
#   11/4/2024 conversion to Qt from tkinter
#   7/20/2020 cloned from masterscreen.v2.py
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
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtCore import Slot

# imports for handling PyQt versions of events
from PySide6.QtCore import QObject, Property, Signal
from PySide6.QtGui import QShortcut, QKeySequence, QIntValidator


from sqlobject import *

import sys as sys
import os as os

# Personal imports
import cribbageconfig as cfg
from ui_CribbageQt import Ui_MainCribbageWindow
from cribbagestartup import CribbageStartup
from playerstab import PlayersTab
from reportstab import ReportsTab
from tourneystab import TourneysTab
from resultstab import ResultsTab
from club import Club
from player import Player
from ctrlVariables import StringVar, IntVar, DoubleVar

class MasterScreen(qtw.QMainWindow, Ui_MainCribbageWindow):
    def __init__(self):
        super().__init__()
        # this setup call defines all of the fields in the UI from the cribbageQt.ui designer file.
        self.setupUi(self)

        # setup all validators and signals.

        # [Club Hdr]
        self.clubNumber = IntVar()
        self.clubName = StringVar()
        self.activePlayers = IntVar()
        self.clubSeason = StringVar()

        # [Club Hdr signals]
        self.clubNumber.intValueAsStringChange.connect(self.hdrClubNumber)
        self.clubName.strValueChanged.connect(self.hdrClubName)
        self.clubSeason.strValueChanged.connect(self.hdrSeason)

        # [Tourney Hdr]
        self.tourneyHdrDate = StringVar()
        self.tourneyHdrNumber = IntVar()
        self.tourneyHdrCount = IntVar()

        # [Tourney Hdr Signals]
        self.tourneyHdrDate.strValueChanged.connect(self.lb_tourneyHdrDate)
        self.tourneyHdrNumber.intValueAsStringChanged.connect(self.lb_tourneyHdrCount)
        self.tourneyHdrCount.intValueAsStringChanged.connect(self.lb_tourneHdrCount)

        # [Players]
        self.pl_firstName = StringVar()
        self.pl_lastName = StringVar()
        self.pl_street = StringVar()
        self.pl_city = StringVar()
        self.pl_state = StringVar()
        self.pl_zip = StringVar()
        self.pl_phone = StringVar()
        self.pl_email = StringVar()
        self.pl_ACCNumber = StringVar()
        self.pl_joined = StringVar()
        self.pl_expires = StringVar()
        self.pl_active = IntVar()

        self.le_firstNameEntry.editingFinished.connect(self.pl_firstName.myValue)
        self.le_lastNameEntry.editingFinished.connect(self.pl_lastName.myValue)
        self.le_streetEntry.editingFinished.connect(self.pl_street.myValue)
        self.le_cityEntry.editingFinished.connect(self.pl_city.myValue)
        self.le_stateEntry.editingFinished.connect(self.pl_state.myValue)
        self.le_zipEntry.editingFinished.connect(self.pl_zip.myValue)
        self.le_phoneEntry.editingFinished.connect(self.pl_phone.myValue)
        self.le_emailEntry.editingFinished.connect(self.pl_email.myValue)
        self.le_accNumberEntry.editingFinished.connect(self.pl_ACCNumber.myValue)
        self.le_joinedEntry.editingFinished.connect(self.pl_joined.myValue)
        self.le_expiresEntry.editingFinished.connect(self.pl_expires.myValue)
        self.le_activeEntry.editingFinished.connect(self.pl_active.myValue)

        # [Tourneys]
        self.ty_number = IntVar()
        self.ty_date = StringVar()

        # [Tourney signals]
        self.le_tourneyNumberEntry.editingFinished.connect(self.ty_number.acceptIntAsStr)
        self.le_tourneyDateEntry.editingFinished.connect(self.ty_date.myValue)

        # [Tourney validators]
        self.ty_number_validator = QIntValidator(1,50,self)
        self.le_tourneyNumberEntry.setValidator(self.ty_number_validator)

        # [Results Line]
        self.rslt_gp = IntVar()
        self.rslt_gw = IntVar()
        self.rslt_sprd = IntVar()
        self.rslt_tkn = IntVar()
        self.rslt_cash = IntVar()
        self.rslt_gvn = IntVar()
        self.rslt_order = IntVar()

        self.rslt_spread_plus = IntVar()
        self.rslt_spread_minus = IntVar()
        self.rslt_skunks_plus = IntVar()
        self.rslt_skunks_minus = IntVar()
        self.rslt_spread_diff = IntVar()
        self.rslt_skunks_diff = IntVar()

        # [Results Line Signals]
        self.le_resultLinePlayerGp.editingFinished.connect(self.rslt_gp.acceptIntAsStr)
        self.le_resultLinePlayerGw.editingFinished.connect(self.rslt_gw.acceptIntAsStr)
        self.le_resultLinePlayerSprd.editingFinished.connect(self.rslt_sprd.acceptIntAsStr)
        self.le_resultLinePlayerTkn.editingFinished.connect(self.rslt_tkn.acceptIntAsStr)
        self.le_resultLinePlayerCash.editFinished.connect(self.rslt_cash.acceptIntAsStr)


        # [Result Line validators]
        self.rslt_gp_validator = QIntValidator(0,36,self)
        self.rslt_gw_validator = QIntValidator(0,22,self)
        self.rslt_sprd_validator = QIntValidator(-250, 250, self)
        self.rslt_tkn_validator = QIntValidator(0,22,self)
        self.rslt_cash_validator = QIntValidator(0,150,self)

        # set initial conditions
        # make error messages red then hide them
        self.lb_badNumber.setStyleSheet('background-color: white; color: red')
        self.lb_badNumber.hide()
        self.lb_tourneyOutofRange.setStyleSheet('background-color: white; color: red')
        self.lb_tourneyOutofRange.hide()
        self.lb_duplicateTourneyNumber.setStyleSheet('background-color: white; color: red')
        self.lb_duplicateTourneyNumber.hide()
        self.lb_badDateFormat.setStyleSheet('background-color: white; color: red')
        self.lb_badDateFormat.hide()
        self.lb_duplicateTourneyDate.setStyleSheet('background-color: white; color: red')
        self.lb_duplicateTourneyDate.hide()




        # set up database to use
        CribbageStartup.initDbms()

        if cfg.debug:
            print('continue gui setup')

        # populate cfg.screenDict
        cfg.screenDict['masterwindow'] = self
        cfg.screenDict['sessionpanel'] = self.sessionPanel      # container for activity panels
        cfg.screenDict['notebook'] = self.tabWidget             # replaces old tk notebook construct

        # call wipe to see what's there
        # MasterScreen.wipeActivityPanel()
        # self.tourneyTab = TourneysTab(cfg.screenDict['sessionpanel'])

        # set up for stackedwidgets
        cfg.screenDict['activitystack'] = self.stackedActivityWidget

        self.playerstab = PlayersTab()      # initialize players tab
        self.tourneystab = TourneysTab()    # initialize tourneys tab
        self.resultstab = ResultsTab()      # initialize results tab
        self.reportstab = ReportsTab()      # initalize results tab

        # prime the activity stack
        # should not need to do this.
        # stackedActivityDict gets widget index when activitypanel is added to the dict
        # cfg.stackedActivityDict['playersactivitypanel'] = 0
        # cfg.stackedActivityDict['tourneysactivitypanel'] = 1
        # cfg.stackedActivityDict['resultsactivitypanel'] = 2
        # cfg.stackedActivityDict['reportsactivitypanel'] = 3

    # no longer applies as we now use the stackedActivityWidget
    # @classmethod
    # def wipeActivityPanel(cls):
    #     # start by hiding all activity panel children of sessionPanel
    #     listOfChildren = []
    #     listOfChildren = cfg.screenDict['sessionpanel'].children()
    #     for child in listOfChildren :
    #         print (child.objectName())
    #         if child.objectName() == 'activityPanel' or \
    #             child.objectName() == 'playersActivityPanel' or \
    #             child.objectName() == 'tourneysActivityPanel' or \
    #             child.objectName() == 'resultsActivityPanel' or \
    #             child.objectName() == 'reportsActivityPanel':
    #
    #             child.hide()

        # this will be changed to show the blank activity panel and hide all others
        # any tab can call this to grid_remove all other activity panels
        # cfg.screenDict['playersactivity'].hide()
        # cfg.screenDict['tourneysactivity'].hide()
        # cfg.screenDict['resultsactivity'].hide()
        # cfg.screenDict['reportsactivity'].hide()



        # print('MasterScreen started . . .')

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
        self.tabWidget.currentChanged.connect(self.tabChange)

        # start out in tourney tab
        cfg.screenDict['notebook'].setCurrentIndex(1)   # show tourney tab

        # self.F3_shortcut = QShortcut(QKeySequence("Ctrl+F3"), self)
        # self.F3_shortcut.activated.connect(self.newTourney)

        self.tabChange(1)                               # show tourney activity

    #   tab switching handler
    @qtc.Slot(int)
    def tabChange(self, index):
        # this is triggered by tabwidget changed signal
        # print ('Tab changed:= ' + str(index))
        match (index):
            case 0:
                 self.playerstab.tabChange()
            case 1:
                self.tourneystab.tabChange()
            case 2:
                self.resultstab.tabChange()
            case 3:
                self.reportstab.tabChange()

    #   [SIGNAL HANDLERS]
    #   All signal handlers reside in their respective modules and are called with the module prefix
    #   [PLAYER SIGNALS]
    #   [TOURNEY SIGNALS]

    # not needed here - move to tourneystab
    # @qtc.Slot()
    # def newTourney(self):
    #     self.tourneystab.createNewTourney()
    #     self.tourneystab.F3_shortcut.activated.connect(newTourney)

if __name__ == '__main__':

    # fake set up global cfg module for all others to share just for standalone testing
    cfg.clubName = 'Century Peggers'
    cfg.clubId = 1
    cfg.clubNumber = 100
    tourneyDate = '2024-25'  # tourney selection will override this
    tourneyId = 70

    app = qtw.QApplication(sys.argv)
    window = MasterScreen()
    window.show()

    if 'window' not in cfg.screenDict:
        # print(cfg.screenDict)
        cfg.screenDict['window'] = window
    # print (cfg.screenDict)
    sys.exit(app.exec())