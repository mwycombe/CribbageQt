# triple-list-box-tourneystab.py
# 7/21/2020 updated to cribbageconfig
#   Nov 2024 replace tkinter with PySide6
#
#   tab is automatically part of PyQt master screen definition
#   no need for separate registration in 'notebook' screenDict entry
#
#   tkinter uses control variables with call-backs to link fields
#   PyQt replaces these with Signals and Slots
#   Use ctrVariables to get Signals from changed variables
#   All tourney screen fields accessed via cfg.screenDict['masterwindow'] widget
#####################################################################
#
#   Creates tab screen for add/change/delete tourneys by date
#   Will self-register in notebook found in screenDict of cfg
#   ManageTourneys was Version 1.0
#   triple-list-box-tourneystab.py was version with multiple listboxes
#   this turned out to be an unnecessary complication - only needed for results, if then
#####################################################################
#   Tourneys 1-36 are regular club weekly tourneys
#   41 is reserved for GRRT tourney results
#   42 is reserved for GRNT tourney results
#   41 & 42 contribute to the NatAll report for the club championship but nowhere else.
#####################################################################
# TODO: On delete, if trny number and trny date both exist, make sure they are in the same trny record.
# TODO: Add up/down key actions to existing tourneys listbox
# TODO: When tourneystab first open up, focus positioned in listbox but line not activated
# System imports
##########################################
# tkinter replaced with PySide6
#
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox as mbx
# from tkinter import filedialog as fdg
########################################
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtCore import Slot
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from PySide6.QtCore import QObject, Property, Signal
from PySide6.QtGui import QShortcut, QKeySequence, QIntValidator

from cribbageconfig import tourneysdebug
from ctrlVariables import StringVar, IntVar, DoubleVar
from tourneysActivityPanel import Ui_tourneysactivitypanel

from sqlobject import *

import sys
import os
import datetime
import dateparser

# Personal imports
import cribbageconfig as cfg
from tourney import Tourney


class TourneysTab (qtw.QWidget, Ui_tourneysactivitypanel):
    # screen class is always a frame
    #************************************************************   
    #   
    #   sets up tab for add/change/delete tourney dates

    def __init__ (self, parent=None):
        print ('starting tourneystab')
        super().__init__()
        self.setupUi(self)
        # set up reference to main ui
        self.main = cfg.screenDict['masterwindow']

        self.tourneyToDelete = ''       # holds tourney record for deleting
        self.unsortedTourneys = []      # unstored all tourney records for club, season
        self.tourneysByNumber = []        # holds tourney records sorted by number
        self.tourneysByDate = []        # tourneys sorted by date
        self.editingState = ''   #1 = creating #2 = editing #3 = deleting

        cfg.screenDict['ttab'] = self

        # [Tourneys]
        self.ty_number = IntVar()
        self.ty_date = StringVar()

        # [Tourney signals]
        self.main.le_tourneyNumberEntry.textEdited.connect(self.ty_number.acceptIntAsStr)
        self.main.le_tourneyDateEntry.textEdited.connect(self.ty_date.acceptStr)

        # [Tourney validators]
        self.ty_number_validator = QIntValidator(1,50,self)
        self.main.le_tourneyNumberEntry.setValidator(self.ty_number_validator)


        #   [PYQT BINDING] section
        #   Set up short cut keys then connect signals to slots

        # self.F3_shortcut = QShortcut(QKeySequence("F3"),self.main.newTourneyNumberEntry)
        self.F2_shortcut = QShortcut(QKeySequence(Qt.Key_F2), self.main.tourneysTabPanel)
        self.F2_shortcut.activated.connect(self.editSelectedTourney)

        self.F3_shortcut = QShortcut(QKeySequence(Qt.Key_F3), self.main.tourneysTabPanel)
        self.F3_shortcut.activated.connect(self.createNewTourney)

        self.F6_shortcut = QShortcut(QKeySequence(Qt.Key_F6),self.main.tourneysTabPanel)
        self.F6_shortcut.activated.connect(self.enterResults)

        self.F9_shortcut = QShortcut(QKeySequence(Qt.Key_F9), self.main.tourneysTabPanel)
        self.F9_shortcut.activated.connect(self.deleteChosenTourney)

        self.F10_shortcut = QShortcut(QKeySequence(Qt.Key_F10), self.main.tourneysTabPanel)
        self.F10_shortcut.activated.connect(self.addOrEditTourney)

        self.Esc_shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self.main.tourneysTabPanel)
        self.Esc_shortcut.activated.connect(self.cancelEdit)

        # self.main.listOfTourneys.currentItemChanged.connect(self.listBoxUpDown)
        self.main.lw_listOfTourneys.currentRowChanged.connect(self.listBoxUpDown)

        # puts activity panel into widget stack
        self.installTourneysActivity()

        # simulated tk.control vars
        self.tourneyNumberEntry = StringVar()
        self.tourneyDateEntry = StringVar()

        self.main.le_tourneyNumberEntry.textEdited.connect(self.setTourneyNumberEntry)
        self.main.le_tourneyDateEntry.textEdited.connect(self.setTourneyDateEntry)

        # this does not create a loop because textEdited signal is not raised
        # by programmatic changes to the lineEdit field
        self.tourneyNumberEntry.strValueChanged.connect(self.main.le_tourneyNumberEntry.setText)
        self.tourneyDateEntry.strValueChanged.connect(self.main.le_tourneyDateEntry.setText)
        # super().__init__(parent)
        # self.grid()
        # self.parent = parent
        #
        # # [control variables] for tourneys
        # self.newTourneyDate = tk.StringVar()
        # self.newTourneyNumber = tk.StringVar()
        # self.editTourneyNumber = tk.StringVar()
        # self.editTourneyDate = tk.StringVar()
        # self.existingTourneyNumber = tk.StringVar()
        # self.existingTourneyDate = tk.StringVar()
        # self.deleteNumber = tk.StringVar()
        # self.deleteDate = tk.StringVar()

        ################################################################
        #   UI code now in masterscreen - ref'd by self.main
        #
        # # build out tab and register with notebook
        # self.config(padx = 5, pady = 5)
        # parent.add(self,text='Tourneys')
        # # register this tab
        # cfg.screenDict['ttab'] = self
        #
        # self.tourneysPanel = tk.LabelFrame(self,
        #                                    text='Tourneys',
        #                                    height=10, width=6, bd='2', relief='sunken')
        # self.tourneysPanel.grid(row=0,column=0, sticky='nw')
        # # self.tourneysPanel.rowconfigure(0, weight=1)
        # # self.tourneysPanel.rowconfigure(1, weight=1)
        # # self.tourneysPanel.rowconfigure(2, weight=1)
        # self.keyF6 = tk.Label(self.tourneysPanel,
        #                       text = 'F6 - Enter results for selected tourney',
        #                       fg='green',
        #                       font=('Helvetica', '12', 'bold'))
        # self.keyF6.grid(row=0, column=0, sticky='w')
        #
        # # [create tourney section]
        # self.tourneyCreationPanel = tk.LabelFrame(self,
        #                                      text="Create a Tourney",
        #                                      height=10, width=8, bd=2, relief='sunken')
        # self.tourneyCreationPanel.grid(row=0, column=1, sticky='nw')
        # self.createInstructionsPanel = tk.LabelFrame(self.tourneyCreationPanel,
        #                                      text='Create New Tourney',
        #                                      padx=10, pady=10, height=10, width=7, bd=2, relief='sunken')
        # self.createNotesPanel = tk.LabelFrame(self.tourneyCreationPanel,
        #                                      text='Create Tourney Notes',
        #                                      padx=10, pady=10, height=10, width=7, bd=2, relief='sunken')
        # self.createInstructionsPanel.grid(row=0, column=1, sticky='nw')
        # self.createNotesPanel.grid(row=0, column=2, sticky='nw')
        # self.createInstructions1 = tk.Label(self.createNotesPanel,
        #                                     text='Enter unique Tourney No. & Date')
        # # self.createInstructions2 = tk.Label(self.createNotesPanel,
        # #                                     text='Then F10 to save or Esc to cancel')
        # self.createInstructions1.grid(row=0, column=0, sticky='nw')
        # self.newInstructions1 = tk.Label(self.createInstructionsPanel,
        #                                text='Enter new fields')
        # self.newInstructions2 = tk.Label(self.createInstructionsPanel,
        #                                  text='Then F10 to save or Esc to cancel')
        # self.newInstructions1.grid(row=0, column=0, sticky='w')
        # self.newInstructions2.grid(row=1, column=0, sticky='w')
        #
        # self.newTourneyPanel = tk.LabelFrame(self,
        #                                      text='New Tourney',
        #                                      padx=10, pady=10,
        #                                      height=10, width=10, bd=2, relief='sunken')
        # self.newTourneyPanel.grid(row=1,column=1,sticky='nw')
        #
        # self.newHelpPanel = tk.LabelFrame(self,
        #                                   text='Create Help',
        #                                   padx=10, pady=10, height=10, width=8, bd=2, relief=tk.GROOVE)
        # self.newHelpPanel.grid(row=2, column=1, columnspan=2, sticky='nw')
        # self.newHelpDuplicateNumber = tk.Label(self.newHelpPanel,
        #                                        text='New number cannot duplicate existing tourney number')
        # self.newHelpDuplicateNumber.grid(sticky='w')
        # self.newHelpDuplicateDate = tk.Label(self.newHelpPanel,
        #                                      text='New date cannot duplicate existing tourney date')
        # self.newHelpDuplicateDate.grid(sticky='w')
        # self.newHelpBadFormatField = tk.Label(self.newHelpPanel,
        #                                       text='Missing field or format error')
        # self.newHelpBadFormatField.grid(sticky='w')
        #
        # #[edit tourney section]
        # self.tourneyMaintenance = tk.LabelFrame(self,
        #                                         text="Manage Tourneys",
        #                                         height=10, width=7, bd=2, relief='sunken')
        # self.tourneyMaintenance.grid(row=0, column=1, sticky='nw')
        #
        # self.editInstructionsPanel = tk.Frame(self.tourneyMaintenance, padx=10, pady=10, relief='flat')
        # self.editInstructionsPanel.grid(row=0, column=0, sticky='w')
        # self.editNotesPanel = tk.Frame(self.tourneyMaintenance, padx=10, pady=10, relief='flat')
        # self.editNotesPanel.grid(row=0, column=1, sticky='nw')
        # self.editHelpPanel = tk.LabelFrame(self,
        #                                    text='Edit Help',
        #                                    padx=10, pady=10, height=10, width=7, bd=2, relief=tk.GROOVE)
        # self.editHelpPanel.grid(row=2, column=1, columnspan=2, sticky='nw')
        #
        # self.editInstructions1 = tk.Label(self.editInstructionsPanel,
        #                                  text='Change the selected fields')
        # self.editInstructions2 = tk.Label(self.editInstructionsPanel,
        #                                        text='Then F10 to save or Esc to cancel')
        # self.editInstructions1.grid(row=0, column=0, sticky='nw')
        # self.editInstructions2.grid(row=1, column=0, sticky='nw')
        # self.editNotes1 = tk.Label(self.editNotesPanel,
        #                            text='You can change tourney number and/or date.')
        # self.editNotes2 = tk.Label(self.editNotesPanel,
        #                            text='Entered data cannot duplicate existing number or date.')
        # self.editNotes1.grid(row=0, column=0, sticky='nw')
        # self.editNotes2.grid(row=1, column=0, sticky='nw')
        #
        # # [existing tourneys section]
        # self.editTourneyOrganizer = tk.Frame(self,
        #                                      relief='flat')
        # self.editTourneyOrganizer.grid(row=1, column=1, sticky='nw')
        # self.existingTourneyPanel = tk.LabelFrame(self.editTourneyOrganizer,
        #                                           text='Existing Tourney',
        #                                           height=10, width=10, bd=2, relief='sunken')
        # self.existingTourneyPanel.grid(row=0, column=0, sticky='nw')
        # self.existingTourneyNumberLabel =tk.Label(self.existingTourneyPanel,
        #                                           text = 'Trny No: ')
        # self.existingTourneyNumberEntry = tk.Entry(self.existingTourneyPanel,
        #                                            textvariable=self.existingTourneyNumber,
        #                                            width = 4, state=tk.DISABLED)
        # self.existingTourneyDateLabel = tk.Label(self.existingTourneyPanel,
        #                                          text = 'Trny Date:  ')
        # self.existingTourneyDateEntry = tk.Entry(self.existingTourneyPanel,
        #                                          textvariable=self.existingTourneyDate,
        #                                          width = 10, state=tk.DISABLED)
        # self.existingTourneyNumberLabel.grid(row = 0, column = 0, sticky='w')
        # self.existingTourneyNumberEntry.grid(row = 0, column = 1, sticky='w')
        # self.existingTourneyDateLabel.grid(row = 1, column = 0, sticky='w')
        # self.existingTourneyDateEntry.grid(row = 1, column = 1, sticky='w')
        # self.editTourneyPanel = tk.LabelFrame(self.editTourneyOrganizer,
        #                                       text = 'Updated Tourney',
        #                                       height = 10, width = 10, borderwidth = 2, relief = 'sunken')
        # self.editTourneyPanel.grid(row = 0, column = 1, sticky = 'nw')
        # self.editTourneyNumberLabel =tk.Label(self.editTourneyPanel,
        #                                        text = 'Trny No:  ')
        # self.editTourneyNumberEntry = tk.Entry(self.editTourneyPanel,
        #                                       textvariable = self.editTourneyNumber,
        #                                       width = 4)
        # self.editTourneyDateLabel = tk.Label(self.editTourneyPanel,
        #                                       text = 'Trny Date:  ')
        # self.editTourneyDateEntry = tk.Entry(self.editTourneyPanel,
        #                                      textvariable = self.editTourneyDate,
        #                                      width = 10)
        # self.editTourneyEditError = tk.Label(self.editTourneyPanel,
        #                                      text='Update has errors',
        #                                      fg='red',
        #                                      font=('Helvetica', '9', 'bold'))
        # self.editTourneyNumberLabel.grid(row = 0, column = 0, sticky='w')
        # self.editTourneyNumberEntry.grid(row = 0, column = 1, sticky='w')
        # self.editTourneyDateLabel.grid(row = 1, column = 0, sticky='w')
        # self.editTourneyDateEntry.grid(row = 1, column = 1, sticky='w')
        # self.editTourneyEditError.grid(row = 2, column = 0, sticky='w')
        # self.editTourneyEditError.grid_remove() # hide until we have an error
        #
        # # Create new tournament panels
        # self.newTourneyNumberLabel = tk.Label(self.newTourneyPanel,
        #                                   text = 'New tourney Number: ')
        # self.newTourneyNumberLabel.grid(row = 0, column = 0, sticky = 'w')
        # self.newTourneyNumberEntry = tk.Entry(self.newTourneyPanel,
        #                                       textvariable = self.newTourneyNumber,
        #                                       width = 3)
        # # self.setNumberEntryHandler(self.newTourneyNumberEntry)
        # self.newTourneyNumberEntry.grid(row = 0, column = 1, sticky = 'w')
        # self.newTourneyDateLabel = tk.Label(self.newTourneyPanel,
        #                                  text='New Tourney Date:  ')
        # self.newTourneyDateLabel.grid(row=1, column=0,sticky='w')
        # self.newTourneyDateEntry = tk.Entry(self.newTourneyPanel,
        #                                     width = 12,
        #                                 textvariable = self.newTourneyDate)
        # self.newTourneyDateEntry.grid(row = 1, column = 1,sticky='w')
        #
        # # [existing tournaments list section]
        # self.tournamentsPanel = tk.LabelFrame(self,
        #                                       text='Existing Tournaments',
        #                                       height=10, width=5, bd=2, relief='sunken')
        # self.tournamentsPanel.grid(row=1,column=0,sticky='w', rowspan=2)
        # self.existingTourneysLabel = tk.Label(self.tournamentsPanel,
        #                                   text = 'Trny                 Trny')
        # self.existingTourneysLabel.grid(row=0, column=0, sticky='w')
        # self.existingLabelLine2 = tk.Label(self.tournamentsPanel,
        #                                    text = ' No.   Data       Date')
        # self.existingLabelLine2.grid(row=1, column=0, sticky='w')
        #
        # # [delete tournament section]
        # self.deletePanel = tk.LabelFrame(self,
        #                                  text='Delete a Tourney',
        #                                  height=10, width=5, bd=2, relief='sunken')
        # self.deletePanel.grid(row=0, column=1, sticky='nw')
        # self.deleteInstructionsPanel = tk.Frame(self.deletePanel, padx=10, pady=10, relief='flat')
        # self.deleteNotesPanel = tk.Frame(self.deletePanel, padx=10, pady=10,relief='flat')
        # self.deleteInstructionsPanel.grid(row=0, column=0, sticky='nw')
        # self.deleteNotesPanel.grid(row=0, column=1, sticky='nw')
        # self.deleteTourneyPanel = tk.LabelFrame(self,
        #                                         text='DeleteTourney',
        #                                         padx=10, pady=10,
        #                                         height=10, width=10, bd=2, relief='sunken')
        # self.deleteTourneyPanel.grid(row=1, column=1, sticky='nw')
        # self.deleteNumberLabel = tk.Label(self.deleteTourneyPanel,
        #                                   text='Tourney Number')
        # self.deleteNumberEntry = tk.Entry(self.deleteTourneyPanel,
        #                                   textvariable=self.deleteNumber,
        #                                   width=2)
        # self.deleteDateLabel = tk.Label(self.deleteTourneyPanel,
        #                                 text='Tourney Date  ')
        # self.deleteDateEntry = tk.Entry(self.deleteTourneyPanel,
        #                                 textvariable=self.deleteDate,
        #                                 width=14)
        # self.deleteNumberLabel.grid(row=0, column=0, sticky='nw')
        # self.deleteDateLabel.grid(row=1, column=0, sticky='nw')
        # self.deleteNumberEntry.grid(row=0, column=1, sticky='nw')
        # self.deleteDateEntry.grid(row=1, column=1, sticky='nw')
        # self.deleteInstructions1 = tk.Label(self.deleteInstructionsPanel,
        #                                     text='Enter both number and date field for delete')
        # self.deleteInstructions2 = tk.Label(self.deleteInstructionsPanel,
        #                                     text='Both fields must match for a successful delete.')
        # self.deleteInstructions1.grid(row=0, column=0, sticky='nw')
        # self.deleteInstructions2.grid(row=1, column=0, sticky='nw')
        # self.deleteNotes1 = tk.Label(self.deleteNotesPanel,
        #                              text='Avoid deleting tourneys with results.')
        # self.deleteNotes2 = tk.Label(self.deleteNotesPanel,
        #                              text='Otherwise you will have to rerun lots of reports.')
        # self.deleteNotes1.grid(row=0, column=0, sticky='nw')
        # self.deleteNotes2.grid(row=1, column=0, sticky='nw')
        # self.deleteHelpPanel = tk.LabelFrame(self,
        #                                      text='Delete Help',
        #                                      padx=10,pady=10, height=10, width=8, bd=2, relief=tk.GROOVE)
        # self.deleteHelpPanel.grid(row=2, column=1,sticky='nw')
        # self.deleteHelpBadFormatField = tk.Label(self.deleteHelpPanel,
        #                                          text='Number or date field bad format')
        # self.deleteHelpBadFormatField.grid(sticky='w')
        # self.deleteHelpNoMatch = tk.Label(self.deleteHelpPanel,
        #                                   text='No record with this number & date - cannot delete.')
        # self.deleteHelpNoMatch.grid(sticky='w')
        # self.deleteHelpTourneyData = tk.Label(self.deleteHelpPanel,
        #                                       text='Selected tourney has entered data')
        # self.deleteHelpTourneyData.grid(sticky='w')
        # self.deleteReportHelpProblems = tk.Label(self.deleteHelpPanel,
        #                               text='You may have to rerun lots of reports.')
        # self.deleteHelp1 = tk.Label(self.deleteHelpPanel,
        #                               text='Delete Help')
        # self.deleteHelp1.grid(row=0, column=0, sticky='nw')
        # self.hideDeleteHelp()
        # # [hide widgets]
        # self.hideEditTourney()
        # self.hideCreateTourney()
        #
        # # Simplify by having just a single list box
        # self.vsb= tk.Scrollbar(self.tournamentsPanel)
        # self.vsb.grid(row=2, column=3, sticky='wns')
        #
        # self.existingTourneys = tk.Listbox(self.tournamentsPanel,
        #                                    yscrollcommand=self.vsb.set,
        #                                    width = 28, height = 18,selectmode = 'single', exportselection = 0)
        # self.existingTourneys.grid(row=2, column=0)
        # self.vsb['command'] = self.existingTourneys.yview
        #
        #   End of tkinter GUI definitions
        ########################################################################################
        #
        #   [BINDING] to be replaced by Signal/Slot definitions
        # # # [binding section]
        # self.editTourneyDateEntry.bind('<F1>', self.showContextHelp)
        # self.newTourneyNumberEntry.bind('<F1>', self.showContextHelp)
        # self.newTourneyDateEntry.bind('<F1>', self.showContextHelp)
        # self.existingTourneys.bind('<F2>', self.editSelectedTourney)
        # self.existingTourneys.bind('<F3>', self.createNewTourney)
        # self.existingTourneys.bind('<F6>', self.enterResults)
        # self.existingTourneys.bind('<F9>', self.deleteTourney)
        # self.newTourneyNumberEntry.bind('<F10>', self.addNewTourney)
        # self.newTourneyDateEntry.bind('<F10>', self.addNewTourney)
        # self.editTourneyDateEntry.bind('<F10>', self.saveEditedTourney)
        # self.editTourneyNumberEntry.bind('<F10>', self.saveEditedTourney)
        # self.deleteNumberEntry.bind('<F10>', self.doDeleteTourney)
        # self.deleteDateEntry.bind('<F10>', self.doDeleteTourney)
        # self.editTourneyDateEntry.bind('<Escape>', self.cancelEdit)
        # self.editTourneyNumberEntry.bind('<Escape>', self.cancelEdit)
        # self.newTourneyNumberEntry.bind('<Escape>', self.cancelCreate)
        # self.newTourneyDateEntry.bind('<Escape>', self.cancelCreate)
        # self.deleteNumberEntry.bind('<Escape>', self.cancelDelete)
        # self.deleteDateEntry.bind('<Escape>', self.cancelDelete)
        #
        # self.existingTourneys.bind('<Up>', self.listBoxUpDown)
        # self.existingTourneys.bind('<Down>', self.listBoxUpDown)
        # End of tkinter bindings section
        ######################################################################################
        # self.startOver()

    @qtc.Slot(str)
    def setTourneyNumberEntry(self, value):
        self.tourneyNumberEntry.myValue = value

    @qtc.Slot(str)
    def setTourneyDateEntry(self, value):
        self.tourneyDateEntry.myValue = value

    def buildActivityPanel(self):
            # start by wiping any prior entries
            # Don't do this with stackedWidget solution
            # MasterScreen.wipeActivityPanel()
            # make the appropriate stacked widget current
            self.widgetIndex = cfg.stackedActivityDict['tourneysactivitypanel']
            cfg.screenDict['activitystack'].setCurrentIndex(self.widgetIndex)

        # self.mtp = cfg.screenDict['activity']
        # self.keyF1 = tk.Label(self.mtp, text = 'F1   Get help with this activity')
        # self.keyF2 = tk.Label(self.mtp, text = 'F2   Edit currently selected tourney')
        # self.keyF3 = tk.Label(self.mtp, text = 'F3   Create new tourney')
        # self.keyF9 = tk.Label(self.mtp, text = 'F9   Delete selected tourney')
        # self.keyF10 = tk.Label(self.mtp, text='F10  Save updates')
        # self.keyEsc = tk.Label(self.mtp, text = 'Esc  Quit current activity')
        # self.keyF1.grid(sticky='w')
        # self.keyF2.grid(sticky='w')
        # self.keyF3.grid(sticky='w')
        # self.keyF9.grid(sticky='w')
        # self.keyF10.grid(sticky='w')
        # self.keyEsc.grid(sticky='w')

    def tabChange(self):
        # no longer event driven
        # tabchanged signal caught in MasterScreen
        #
        # if no tournaments, then must request at least one to be created
        #
        self.buildActivityPanel()
        # self.main.tourneysTabPanel.setFocus()
        if cfg.at.countTourneysForSeason(cfg.season) < 1:
            self.createNewTourney()
        else:
            self.populateExistingTourneys()
            # self.showWidget((self.newTourneyPanel))

    def populateExistingTourneys(self):
        if cfg.debug:
            print('Populate existing tourneys')
        self.clearListBoxes()
        self.unsortedTourneys = cfg.at.allTourneysForClubBySeason(cfg.clubRecord, cfg.season)
        for t in self.unsortedTourneys:
            print (t.TourneyNumber)
        # show youngest tourneys first - with lowest date & tourney number
        self.tourneysByNumber = sorted(self.unsortedTourneys, key = lambda Tourney: Tourney.TourneyNumber)
        self.tourneysByDate = sorted(self.unsortedTourneys, key = lambda Tourney: Tourney.Date)
        # show tourneys by date list
        if cfg.debug and cfg.tourneysdebug:
            print ('Tourneys by date: ')
            print (self.tourneysByDate)
            print ('Tourneys by number:')
            print (self.tourneysByNumber)
        # change to use listbox.insert(posn, value) method
        # print ('Sorted tourney numbers')
        self.tourneysInDbms = []
        for x in self.tourneysByNumber:
            # single listbox version with concatenated fields

            if cfg.debug and cfg.tourneysdebug:
                print (x.TourneyNumber)

            tno = str(x.TourneyNumber)
            tno = tno.rjust(3) if x.TourneyNumber < 10 else tno
            tno = tno + '    '
            d ='|      ' + x.Entered + '      |' if x.Entered == '*' else'|              |'
            if cfg.debug and cfg.tourneysdebug:
                print(d)
                myDate = self.makeUSDate(x.Date)
                print(type(myDate))

            # build up the list of items
            tourneyLine = tno + d + '    ' + self.makeUSDate(x.Date)
            self.tourneysInDbms.append(tourneyLine)

        self.main.lw_listOfTourneys.addItems(self.tourneysInDbms)
            # self.existingNumbers.insert(tk.END, x.TourneyNumber)
            # self.existingValues.insert(tk.END, x.Entered)
            # self.existingDates.insert(tk.END, self.makeUSDate(x.Date))
        self.main.lw_listOfTourneys.setCurrentItem(self.main.lw_listOfTourneys.item(0))
        if cfg.debug and cfg.tourneysdebug:
            print ('Setting focus and activate')


        # set focus to first row
        self.main.lw_listOfTourneys.setCurrentRow(0)
        self.main.lw_listOfTourneys.setFocus()
        # self.existingTourneys.activate(0)
        # self.existingTourneys.focus_force()
        # self.existingTourneys.update()
        # self.existingTourneys.focus_force()
        # self.existingTourneys.update()
        # self.existingTourneys.activate(0)
        # self.existingTourneys.update()
        # self.existingTourneys.selection_set(0)
        # self.existingTourneys.activate(0)
        # self.existingTourneys.see(0)
        # self.existingTourneys.focus_force()
    def clearListBoxes(self):
        self.main.lw_listOfTourneys.clear()
        # self.existingTourneys.delete(0, tk.END)

    @qtc.Slot()
    def listBoxUpDown(self,row):
        # selection = event.widget.curselection()[0]
        if cfg.debug and cfg.tourneysdebug:
            print('Row/Item change signal')
        # self.main.lw_listOfTourneys.setCurrentRow(new)
        if cfg.debug and cfg.tourneysdebug:
            print ('Row: ' + str(row))
            # print(self.main.lw_listOfTourneys.item(row).text())    # show row contents
            # throws None Type has no attribute 'text' error
        # if event.keysym == 'Up':
        #     selection += -1
        # if event.keysym == 'Down':
        #     selection += 1
        # if 0 <= selection < event.widget.size():
        #     event.widget.selection_clear(0, tk.END)
        #     event.widget.selection_set(selection)
    def createNewTourney (self):
        # show the new tourney panel and Add/Cancel buttons
        # set editState
        # now receives slot call
        self.editingState = 1       # show we are creating - for context help
        if cfg.debug and cfg.tourneysdebug:
            print('Create new tourney')
        self.main.newTourneyFrameLabel.setText('New Tourney')
        self.tourneyNumberEntry.myValue = ' '
        self.tourneyDateEntry.myValue = ' '
        self.main.le_tourneyNumberEntry.setFocus()
        # return
        # # self.hideAll()
        # self.showCreateTourney()
    def enterResults(self):
        print('Enter results')
        # TODO Change to reference current row for listOfTourneys
        # self.listBoxIndex = event.widget.curselection()[0]  # tourney to enter results for
        self.listBoxIndex = self.main.lw_listOfTourneys.currentRow()
        cfg.tourneyRecord = self.tourneysByNumber[self.listBoxIndex]
        cfg.tourneyRecordId = cfg.tourneyRecord.id
        cfg.tourneyDate = self.makeUSDate(cfg.tourneyRecord.Date)
        cfg.tourneyNumber = cfg.tourneyRecord.TourneyNumber
        # cfg.tourneyDate = self.existingDates.get(self.existingDates.curselection())
        # cfg.tourneyNumber = int(self.existingNumbers.get(self.existingDates.curselection()))

        # if cfg.debug and cfg.tourneysdebug:
        #     print ('Selected tourney for results: ', cfg.tourneyRecord)
        #     print ('Tourney id:', cfg.tourneyRecordId)
        #     print ('Switch to results tab')
        self.main.tabWidget.setCurrentIndex(2)       # select tab 2 which is for results

    def cancelEdit(self):
        print ('Cancel the edit - save nothing')
        self.editingState = 0       # not in any state
        # self.hideEditTourney()
        # self.hideCreateTourney()
        # self.hideDeleteTourney()
        self.startOver()

    def cancelCreate(self, event):
        print ('Cancel the create - save nothing')
        exit()
        self.cancelEdit(event)
    def cancelDelete(self, event):
        print ('Cancel the delete - save nothing')
        exit()
        self.clearDeleteEntryFields()
        self.hideDeleteTourney()
        self.startOver()
    def clearDeleteEntryFields(self):
        exit()
        self.deleteNumber.set('')
        self.deleteDate.set('')
    def startOver(self):
        print('startOver')
        # exit()
        self.resetTourneyInformation()
        self.populateExistingTourneys()
        # self.existingTourneys.selection_set(0)
        # self.existingTourneys.activate((0))
        # self.existingTourneys.focus_force()
        # self.hideAll()
        # self.tourneyToDelete = ''       # remove tourney record to delete
        # self.buildActivityPanel()


    def resetTourneyInformation(self):
        # sets a clean slate for any tourney related work
        self.main.lb_tourneyNumberEntry.setText(' ')
        self.main.lb_tourneyDateEntry.setText(' ')
        self.tourneyNumberEntry.myValue = ' '
        self.tourneyDateEntry.myValue = ' '
        self.resetErrorHiLite(self.main.lb_tourneyNumberEntry)
        self.resetErrorHiLite(self.main.lb_tourneyDateEntry)
        self.main.lw_listOfTourneys.setCurrentRow(0)
        self.main.lw_listOfTourneys.setFocus()
    def recycleDelete(self):
        self.tourneyToDelete = ''       # clear delete record
        exit()
        self.startOver()
        # this is an event handler - there is nothing to pass on from the event
        print ('Save new tourney')
        self.addTourney()
    def addOrEditTourney(self):
        print ('addOrEdit')
        # no longer have signal from different entry fields...
        match self.editingState:
            case 1:
                self.addNewTourney()
            case 2:
                self.saveEditedTourney()
            case _:
                self.showNothingToSave()
        # if self.editingState == 1:
        #     self.addNewTourney()
        # elif self.editingState == 2:
        #     self.saveEditedTourney()
        # else:
        #     self.showNothingToSave()

    def showNothingToSave(self) -> None:
        # result = QMessageBox.question(None, 'Use this database?', cfg.dbmsName)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('Not New or Edit Tourney')
        msgBox.setWindowTitle('Unrecognized Edit Mode')
        msgBox.setStandardButtons(QMessageBox.Ok )

        result = msgBox.exec()
        if cfg.debug and cfg.tourneysdebug:
            print('No Tourney info to handle')

    def addNewTourney (self):
        # On F10 build a new Tourney and add it to the data base
        # and reshow
        print('Add new tourney')
        # strip off extraneous characters
        self.tourneyNumberEntry.myValue = self.tourneyNumberEntry.myValue.strip()
        self.tourneyDateEntry.myValue = self.tourneyDateEntry.myValue.strip()
        self.validNumber = (self.validateEntryField('number', self.tourneyNumberEntry.myValue, self.main.le_tourneyNumberEntry))
        self.validDate =  (self.validateEntryField('date', self.tourneyDateEntry.myValue, self.main.le_tourneyDateEntry))
        if not ((self.validateEntryField('number', self.tourneyNumberEntry.myValue, self.main.le_tourneyNumberEntry)) and \
            (self.validateEntryField('date', self.tourneyDateEntry.myValue, self.main.le_tourneyDateEntry))):
            # self.showWidget(self.newHelpBadFormatField)
            self.main.lb_tourneyNumberEntry.setFocus()
            return
        # check for duplicates of number or date
        if self.duplicateNewNumber() or self.duplicateNewDate():
            # self.showNewHelpPanel()
            self.showNewNumberError()
            self.showNewDateError()
            return
        try:
            print ('Try new tourney add')
            Tourney(TourneyNumber = int(self.tourneyNumberEntry.myValue),
                    Date = self.makeIsoDate(self.tourneyDateEntry.myValue),
                    Club = cfg.clubRecord, Season = cfg.season
                    )
            # repopulate tourney on-screen list
            self.populateExistingTourneys()
            self.tourneyNumberEntry.myValue = ' '
            self.tourneyDateEntry.myValue = ' '
            # self.newTourneyDate.set('')
            # self.newTourneyNumber.set('')
            # self.hideAll()
            # self.existingTourneys.focus_force()
            # self.existingTourneys.selection_set(0)
            # self.hideWidget(self.newTourneyPanel)
            # self.hideNewHelpPanel()exe
            # self.showWidget(self.manageTourneyPanel)
            # self.showCreateButtons()
        except dberrors.DuplicateEntryError:
            if cfg.debug and cfg.tourneysdebug:
                print('Duplicate tourney date or Number')
            self.errorHiLite(self.main.lb_tourneyNumberEntry)
            self.errorHiLite(self.main.lb_tourneyDateEntry)
            if mbx.askretrycancel('Duplicate number or date','Retry/edit or Cancel',parent = self):
                # set focus and let user retry the date
                self.main.lb_tourneyNumberEntry.setFocus()
            else:
                # clear out entry fields
                self.resetErrorHiLite(self.newTourneyDateEntry)
                self.resetErrorHiLite((self.newTourneyNumberEntry))
                self.startOver()
    def duplicateNewNumber(self):
        # exit()
        # already validated as a number
        # if int(self.newTourneyNumber.get()) in cfg.tourneyXref:
        #     self.errorHiLite(self.newTourneyNumberEntry)
        #     self.showNewNumberError()
        #     return True;
        if self.duplicateNumber( self.tourneyNumberEntry.myValue):
            self.errorHiLite(self.main.le_tourneyNumberEntry)
            self.showNewNumberError()
            return True
        return False
        # return False
    def duplicateNewDate(self):
        # exit()
        # already validated as a date
        # SQLObject datecol returns datetime.date objects, so dow makeIsoDate so then can be compared
        newDate = self.makeIsoDate(self.tourneyDateEntry.myValue)
        if self.duplicateDate(newDate):
            self.errorHiLite(self.main.le_tourneyDateEntry)
            self.showNewDateError()
            return True
        return False
        # return self.duplicateDate(newDate)
        #
        # newDate = self.makeIsoDate(self.newTourneyDateEntry.get())
        # tdates = []
        # for tny in self.tourneysByDate:
        #     tdates.append(tny.Date)
        # if newDate in tdates:
        #     self.errorHiLite(self.newTourneyDateEntry)
        #     self.showNewDateError()
        #     return True
        # return False
    def duplicateNumber(self, value):
        # exit()
        # receives string valued from entry field
        if int(value) in cfg.tourneyXref:
            return True;
        return False
    def duplicateDate(self, value):
        # exit()
        # value should be an isoformat date object
        tdates = []
        for tny in self.tourneysByDate:
            tdates.append(tny.Date)
        if value in tdates:
            return True
        return False

    def makeIsoDate(self, USDate):
        # exit()
        # take date in US format and turn into ISO8601 format data object
        # date format aleadys validate by validateNewTourneyDate
        # mon, day, yr = USDate.split(sep = '/')
        # SQLObject DateCol returns date objects
        return dateparser.parse(USDate).date()
    def makeUSDate(self, ISODate):
        # presumes the incoming ISODate is valid
        return  ISODate.strftime('%m/%d/%Y')

    def validateTourneyNumber(self, value, w):
        # incoming value is a string
        if cfg.debug and cfg.tourneysdebug:
            print ('Number value: ', value)
        # exit()
        self.resetErrorHiLite(w)
        if not value.isnumeric():
            print ('Not numeric')
            self.errorHiLite(w)
            return False
        if int(value) < 1 or int(value) > 45:
            print ('Out of range')
            self.errorHiLite(w)
            return False
        return True
    def validateTourneyDate(self, value, w):
        # exit()
        # uses the parser function to create a datetime.date object - or None
        if not dateparser.parse(value):
            # bad date
            self.errorHiLite(w)
            return False
        else:
            self.resetErrorHiLite(w)
            return True
        return True
    def badTourneyForResults(self):
        exit()
        # msg box and retry or cancel for missing tourney selection for results entry
        return mbx.askretrycancel('Invalid Tourney Date Selection',
                                  'Select a Tourney before using Right Arrow',
                                  icon=mbx.Error)
    def validateEntryField(self, field, input, w):
        # exit()
        # use new python match statement
        match field:
            case 'number':
                return self.validateTourneyNumber(self.tourneyNumberEntry.myValue,w)
            case 'date':
                return self.validateTourneyDate(self.tourneyDateEntry.myValue,w)

        # # invokes appropriate validation field
        # switcher = {
        #     'number': self.validateTourneyNumber,
        #     'date': self.validateTourneyDate
        # }
        # return switcher.get(field)(input, w)

    # def setNumberEntryHandler(self, w):
    #     exit()
    #     # pass in extra parameters to event handler
    #     def entryHandler(event, self = self, ):
    #         return self.numberInputValidation(event)
    #     w.bind('<KeyPress>', entryHandler)
    # def setDateEntryHandler(self, w):
    #     exit()
    #     # pass in extra parameters to event handler
    #     def entryHandler(event, self = self):
    #         return self.dateInputValidation(event)
    #     w.bind('<KeyPress>', entryHandler)
    # def numberInputValidation(self, event):
    #     if event.keysym == 'Return' or event.keysym == 'Tab':
    #         # self.validateNewTourneyNumber(self.newTourneyNumberEntry.get())
    #         # advance to date input
    #         self.newTourneyDateEntry.focus_force()
    # def dateInputValidation(self, event):
    #     exit()
    #     if event.keysym == 'Return' or event.keysym == 'Tab':
    #         # self.validateNewTourneyDate(self.newTourneyDateEntry.get())
    #         self.addTourney()
    # def cancelUpdate(self):
    #     # go back to starting status
    #     self.hideEditButtons()
    #     self.hideWidget(self.editTourneyPanel)
    #     self.showCreateButtons()
    # def forgetIt(self, event):
    #     # forget Tourney update or delete
    #     exit()
    #     self.tourneyDate.set('')
    #     self.newTourneyDate.focus_set()
    #     self.hideWidget(self.Cancel)
    #     self.hideWidget(self.updateTourney)
    #     self.hideWidget(self.deleteTourney)
    #     self.showWidget(self.addTourney)
    # # def editByDate(self, event):
    #     # this is activated by DoubleClick-1 :
    #     self.beingEdited = self.existingDates.curselection()[0]
    #     self.editSelectedTourney(self.beingEdited)
    # def editByNumber(self, event):
    #     # this is activated by DoubleClick-1
    #     self.beingEdited = self.existingNumbers.curselection()[0]
    #     self.editSelectedTourney(self.beingEdited)
    def editSelectedTourney(self):
        print('edit selected tourney')
        # this is activated by F2
        self.editingState = 2       # show we are editing - for context help
        self.main.newTourneyFrameLabel.setText('Edit Tourney')
        self.splitRow = self.main.lw_listOfTourneys.currentItem().text().split()
        if cfg.debug and cfg.tourneysdebug:
            print ('Edit split row: ' + str(self.splitRow))
        self.tourneyNumberEntry.myValue = self.splitRow[0].strip()
        self.tourneyDateEntry.myValue = self.splitRow[len(self.splitRow)-1].strip()
        #
        # test hi-lighting for pyqt
        #
        # parse current row data and initialize
        # self.listBoxIndex = event.widget.curselection()[0]  # always get a tuple even on single select
        # print('Tourney number: ',self.existingNumbers.get(listBoxIndex))
        # print('Tourney date: ', self.existingDates.get(listBoxIndex))
        # self.showEditPanels(self.existingTourneys.curselection())
        # capture tourney record being edited.
        self.tourneyUnderEdit = self.tourneysByNumber[self.main.lw_listOfTourneys.currentRow()]
        # print('tourney to edit', self.tourneyUnderEdit)
        # print('Tourney under edit: ', self.tourneyUnderEdit)
        # save original parameters in case user user cancels or forgets the edits

        self.editTourneyOriginalDate = self.tourneyUnderEdit.Date
        self.editTourneyOriginalNumber = self.tourneyUnderEdit.TourneyNumber
        if cfg.debug and cfg.tourneysdebug:
            print('Tourney under edit number: ' + str(self.editTourneyOriginalNumber))
            print('Tourney under edit date: ' + str(self.editTourneyOriginalDate))

        # self.tourneyDate.set(eval(self.existingTourneyDates.get()))self.listBoxIndex[0]))
        # self.hideAll()
        # self.showEditPanels(self.listBoxIndex)
        # populate the existing selected tourney params
        self.populateEditFields()
        if cfg.debug and cfg.tourneysdebug:
            print('Set focus to tourneyNumberEntry')
        self.main.lb_tourneyNumberEntry.setFocus()

    def populateEditFields(self):
        # exit()
        # self.existingTourneyNumber.set(self.tourneyUnderEdit.TourneyNumber)
        # self.editTourneyNumber.set(self.tourneyUnderEdit.TourneyNumber)
        # self.existingTourneyDate.set(self.makeUSDate(self.tourneyUnderEdit.Date))
        # self.editTourneyDate.set(self.makeUSDate(self.tourneyUnderEdit.Date))
        self.main.lb_tourneyNumberEntry.setText(str(self.tourneyNumberEntry.myValue))
        self.main.lb_tourneyDateEntry.setText(str(self.tourneyDateEntry.myValue))

    def saveEditedTourney(self):
        print('save tourney')
        # validate date entered then save if ok
        if not ((self.validateEntryField('number', self.tourneyNumberEntry.myValue, self.main.lb_tourneyNumberEntry)) and \
             (self.validateEntryField('date', self.tourneyDateEntry.myValue, self.main.lb_tourneyDateEntry))):
            # bad entry fields
            self.showBadEditEntry()
            self.main.lb_tourneyNumberEntry.setFocus()
            return
        # if we drop through we have a viable edit to try for Existing Tourney
        try:
            print ('tourneyNumber: ', self.tourneyNumberEntry.myValue)
            print ('tourneyDate: ', self.tourneyDateEntry.myValue)
            self.tourneyUnderEdit.set(TourneyNumber = int(self.tourneyNumberEntry.myValue), \
                                      Date = self.makeIsoDate(self.tourneyDateEntry.myValue))
        except (dberrors.DuplicateEntryError, dberrors.IntegrityError, dberrors.DataError):
            print ('Tourney update failed with error: ', sys.exc_info()[0])
            # TODO: highlight error fields and reposition at number entry field
            # TODO: show help messages
            return
        finally:
            self.startOver()        # always go around
    def showContextHelp(self, event):
        print ('Check editingState for which help to show')
        exit()
        if self.editingState == 1:
            self.showWidget(self.newHelpPanel)
        elif self.editingState == 2:
            self.showWidget(self.editHelpPanel)

    def updateTourney(self):
        # first validate the user's update input
        print ('In updateTourney')
        exit()
        if not self.validateEntryField('number', self.editTourneyNumberEntry.get(),
                                       self.editTourneyNumberEntry):
            self.editTourneyNumberEntry.focus_force()
            return
        elif not self.validateEntryField('date', self.editTourneyDateEntry.get(),
                                          self.editTourneyDateEntry):
            self.editTourneDateEntry.focus_force()
            return
        # otherwise try to replace current tourney entry with new information

        try:
            print ('Try update')
            self.tourneyUnderEdit.set(TourneyNumber = int(self.editTourneyNumberEntry.get()),
                                      Date = self.makeIsoDate(self.editTourneyDateEntry.get()))
            self.tourneyUnderEdit.syncUpdate()
        except dberrors.DuplicateEntryError:
            self.showWidget(self.editTourneyEditError)
            self.showEditErrors()
            return
        # self.editingRecordId = self.getRecordId(self.editTourneyOriginalDate)
        # t = Tourney.get(self.editingRecordId)
        # t.set(Date=self.tourneyDate.get())
        self.populateExistingTourneys()
        self.hideWidget(self.editTourneyPanel)
        self.showWidget(self.manageTourneyPanel)
        self.showCreateButtons()
    def deleteTourney(self, event):
        # delete the current tourney
        print ('delete selected tourney')
        exit()
        # TODO: should check we are not deletng a tourney for
        # which there are already results...this would be a
        # serious data integrity error.
        # self.dbmsSorterTourneys corresponds to listbox entries
        print ('Request to delete a tourney')
        self.hideAll()
        self.showDeleteTourney()
        self.hideDeleteHelp()   # always turn off delete help for next iteration
        self.deleteNumberEntry.focus_force()    # start with the  tourney number
    def doDeleteTourney(self, event):
        print ('check & execute delete')
        exit()
        if not (self.validateEntryField('number', self.deleteNumber.get(), self.deleteNumberEntry))or \
            not (self.validateEntryField('date', self.deleteDate.get(), self.deleteDateEntry)):
            self.showWidget(self.deleteHelpPanel)
            self.showWidget(self.deleteHelpBadFormatField)
            self.deleteNumberEntry.focus_force()
            return
        # next check that the referenced tournament exists
        if  not self.deleteTournamentExists():
            self.showWidget(self.deleteHelpPanel)
            self.showWidget(self.deleteHelpNoMatch)
            return
        # good format, actual tourney found, check for data
        if self.deleteTourneyHasResults():
            # self.showEnteredDataHelpWarning()
            if mbx.askyesno('Tourney has entered data', 'Do  you really want to delete?'):
                self.deleteChosenTourney()
            else:
                self.recycleDelete()  # go back to delete fields
        else:
            if mbx.askyesno('Empty tourney', 'Do you really want to delete?'):
                self.deleteChosenTourney()
            else:
                self.recycleDelete()
        # self.tourneyToDelete = Tourney.select(Tourney.q.TourneyNumber == int(self.deleteNumberEntry.get()))
    def deleteChosenTourney(self):
        print (self.tourneyToDelete)
        return
        # self.tourneyToDelete holds the record for this tourney
        try:
            self.tourneyToDelete.delete(self.tourneyToDelete.id)
            self.startOver()
        except:
            self.errorHiLite(self.deleteNumberEntry)
            self.errorHiLite(self.deleteDateEntry)
            # mbx.showwarning('Delete failed', 'Check input and try again')
            self.resetErrorHiLite(self.deleteNumberEntry)
            self.resetErrorHiLite(self.deleteDateEntry)
            self.hideDeleteHelp()
            self.startOver()
    def deleteTournamentExists(self):
        exit()
        if  not (self.deleteTournamentNumberExists() and self.deleteTournamentDateExists()):
            self.showWidget(self.deleteHelpPanel)
            self.showWidget(self.deleteHelpNoMatch)
            return False    # delete target number and/or date not found
        else:
            # now check that the actual target exists
            tourneyToDeleteList = list(Tourney.select(AND(Tourney.q.TourneyNumber == int(self.deleteNumber.get()), \
                                                      Tourney.q.Date == self.makeIsoDate(self.deleteDate.get()))))
            if len( tourneyToDeleteList) < 1:
                # there was no tourney to delete - list is empty
                return False
            else:
                self.tourneyToDelete = tourneyToDeleteList[0]
                return True # target tourney exists
    def deleteTournamentNumberExists(self):
        exit()
        # self.duplicateNumber takes the contral variable StringVar input
        return self.duplicateNumber( self.deleteNumber.get())
    def deleteTournamentDateExists(self):
        exit()
        deleteDate = self.makeIsoDate(self.deleteDate.get())
        return self.duplicateDate(deleteDate)
    def deleteTourneyHasResults(self):
        exit()
        if self.tourneyToDelete.Entered == '*':
            return True
        else:
            return False
    def getRecordId (self, date):
        print (date)
        exit()
        t = Tourney.select(Tourney.q.Date == date)
        l = list(t)
        print (l)
        print (l[0].id)
        return l[0].id
    def resetCreateFields(self):
        exit()
        # remove any prior input and error field flags
        self.newTourneyNumber.set('')
        self.newTourneyDate.set('')
        self.resetErrorHiLite(self.newTourneyNumberEntry)
        self.resetErrorHiLite(self.newTourneyDateEntry)
    def showNewNumberError(self):
        exit()
        self.showNewHelpPanel()
        self.showWidget(self.newHelpDuplicateNumber)
    def showNewDateError(self):
        exit()
        self.showNewHelpPanel()
        self.showWidget(self.newHelpDuplicateDate)
    def showNewHelpPanel(self):
        exit()
        self.showWidget(self.newHelpPanel)
    def hideNewHelpPanel(self):
        exit()
        self.hideWidget(self.newHalpPanel)
    def showCreateTourney(self):
        self.editingState = 1       # create state

        # self.hideEditTourney()
        # self.resetNewHelpFields()
        # self.hideDeleteTourney()
        self.showCreatePanel()
    def resetNewHelpFields(self):
        exit()
        self.hideWidget(self.newHelpPanel)
        self.hideWidget(self.newHelpDuplicateDate)
        self.hideWidget(self.newHelpDuplicateNumber)
        self.hideWidget(self.newHelpBadFormatField)
    def showCreatePanel(self):
        if cfg.debug and cfg.tourneysdebug:
            print('In create tourney panel')
        self.main.newTourneyFrameLabel.setText('New Tourney')
        self.main.newTourneyNumberEntry.setFocus()
        # self.showWidget(self.tourneyCreationPanel)
        # self.showWidget(self.newTourneyPanel)
        # # position focus on first entry field
        # self.newTourneyNumberEntry.focus_force()
        # self.showWidget(self.newHelpPanel)
        # self.hideWidget(self.newHelpDuplicateNumber)
        # self.hideWidget(self.newHelpDuplicateDate)
    def showEditTourney(self):
        exit()
        self.editingState = 2       # edit state
        self.hideCreateTourney()
        self.hideDeleteTourney()
        self.showEditPanels()
    def showDeleteTourney(self):
        exit()
        self.editingState = 3       # delete state
        self.hideCreateTourney()
        self.hideEditTourney()
        self.showDeletePanels()
    def showDeletePanels(self):
        exit()
        self.showWidget(self.deletePanel)
        self.showWidget(self.deleteTourneyPanel)
        self.showWidget(self.deleteHelpPanel)
    def showTourneyHasDataWarning():
        # exit()
        self.showWidget(self.deleteHelpTourneyData)
        self.showWidget(self.deleteReportHelpProblems)
    def showEditPanels(self, index):
        exit()
        print ('lb index to edit', index)
        self.showWidget(self.tourneyMaintenance)
        self.showWidget(self.editInstructionsPanel)
        self.showWidget(self.editNotesPanel)
        self.showWidget(self.existingTourneyPanel)
        self.showWidget(self.editTourneyPanel)
        self.showWidget(self.editHelpPanel)
    def showBadEditEntry(self):
        # bad fields hilited and error messages set by validations routines
        return
    def hideCreateTourney(self):
        self.resetTourneyEntry()
        # self.hideWidget(self.tourneyCreationPanel)
        # self.hideWidget(self.newTourneyPanel)
        # self.hideCreateHelp()
        # self.resetCreateFields()
    def resetTourneyEntry(self):
        self.main.newTourneyFrameLabel.setText('New Tourney')
        self.main.lb_tourneyNumberEntry.setText('')
        self.main.lb_tourneyDateEntry.setText('')
        self.tourneyNumberEntry.myValue = ' '
        self.tourneyDateEntry.myValue = ' '
        self.main.lb_tourneyNumberEntry.setText('')
        self.main.lb_tourneyDateEntry.setText('')
        self.main.lb_tourneyNumberEntry.setFocus()
    # def hideCreateHelp(self):
    #     exit()
    #     self.hideWidget(self.newHelpPanel)
    #     self.hideWidget(self.newHelpDuplicateDate)
    #     self.hideWidget(self.newHelpDuplicateNumber)
    def hideEditTourney(self):
        # exit()
        self.hideWidget(self.tourneyMaintenance)
        self.hideWidget(self.editInstructionsPanel)
        self.hideWidget(self.editNotesPanel)
        self.hideWidget(self.existingTourneyPanel)
        self.hideWidget(self.editTourneyPanel)
        self.hideWidget(self.editHelpPanel)
    def hideDeleteTourney(self):
        exit()
        self.hideWidget(self.deletePanel)
        self.hideWidget(self.deleteTourneyPanel)
        self.hideDeleteHelp()
    def hideDeleteHelp(self):
        exit()
        self.hideWidget(self.deleteHelpPanel)
        self.hideWidget(self.deleteHelpBadFormatField)
        self.hideWidget(self.deleteHelpTourneyData)
        self.hideWidget(self.deleteReportHelpProblems)
        self.hideWidget(self.deleteHelp1)
        self.hideWidget(self.deleteHelpNoMatch)
    def hideAll(self):
        self.editingState = 0
        self.resetTourneyEntry()
    def hideWidget(self, w):
        # exit()
        w.hide()
    def showWidget(self, w):
        # exit()
        w.show()
    def errorHiLite(self, w):
        # PyQt color change
        # does not work if separated
        # self.pinkBackground(w)
        # self.blackText(w)
        w.setStyleSheet('background-color: pink; color: black')
        # exit()
        # # print ('Entry config: ', w.config())
        # exit()
        # w.config(background = 'pink', foreground = 'black')
    def resetErrorHiLite(self, w):
        # exit()
        w.setStyleSheet('background-color: white; color: black')
    def redText(self, w):
        w.setStyleSheet('color: red')
        # exit()
        # w.config(foreground='red')
    def blackText(self, w):
        w.setStyleSheet('color: black')
        # exit()
        # w.config(foreground='black')
    def pinkBackground(self,w):
        w.setStyleSheet('background-color: pink')
    def whiteBackground(self,w):
        w.setStyleSheet('background-color: white')
    def installTourneysActivity(self):
        # MasterScreen.wipeActivityPanel()
        print ('install tourneys activity panel')
        # have to add this into the master activity stacked widget
        self.widx = cfg.screenDict['activitystack'].addWidget(self)
        # remember this index
        cfg.stackedActivityDict['tourneysactivitypanel'] = self.widx

        # self.tourneysActivity.tourneysActivityPanel.show()
        # self.tourneysActivity.tourneysActivityPanel.activateWindow()
        # self.tourneysActivity.tourneysActivityPanel.raise_()

