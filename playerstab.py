# playerstab.py
# 7/21/2020 update to cribbageconfig
#
# Nov 2024 replace tkinter with PySide6
#
#####################################################################
#
#   Creates tab screen for handling players
#   Will self-register in notebook found in screenDict of cfg
#   Version 1.0 name was ManagePlayers.py
#
#####################################################################
# from operator import truediv

from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import  QIntValidator

# TODO: When a new player is added or change need to rebuild the xref tables in cfg -
#  use CribbageStartUp.createPlayersXref()
# TODO: Set active player count in cfg and link to hdr field
# TODO: Update cfg active count after every player action
# TODO: When a new player is added, refresh the in-memory list of players
# TODO: Add new player confirms that add but does not clear the screen
# TODO: Edit player does not clear screen on F10 - have to use esc to quit edit
# TODO: Cannot escape from edit screen
# TODO: Provide option for hiding inactive players from list of players
# TODO: Allow players to be marked for inclusion in results
# TODO: Allow soft delete of especially deceased players and moved away.
# TODO: Support for selection by alpha string.

# System imports

# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox as mbx
# from tkinter import filedialog as fdg

from sqlobject import *

import sys as sys
import os as os

import datetime
import dateparser


from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtCore import Slot, QEvent
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import Qt, QShortcut, QKeySequence
from PySide6.QtWidgets import QListWidgetItem, QMessageBox


# Personal imports
import cribbageconfig as cfg
from playersActivityPanel import Ui_playersactivitypanel
from ctrlVariables import StringVar, IntVar, BoolVar
from club import Club
from player import Player
from cribbagestartup import CribbageStartup

# from masterscreen import MasterScreen

class PlayersTab (qtw.QWidget, Ui_playersactivitypanel):

    #************************************************************   
    #   
    #   sets up tab for managing players & register with 'notebook' frame
    #
    def __init__ (self, parent=None):
        if cfg.debug and cfg.playersdebug:
            print('starting playerstab')

        super().__init__()
        self.setupUi(self)
        self.main = cfg.screenDict['masterwindow']

        self.installPlayersActivity()

        cfg.screenDict['ptab'] = self

        self.main.listOfPlayers.setEnabled(True)
        self.main.listOfPlayers.itemDoubleClicked.connect(self.togglePlayer)
        # show all/active state button
        self.main.showAllPlayers.stateChanged.connect(self.displayExistingPlayers)

        self.main.listOfPlayers.itemSelectionChanged.connect(self.trackSelectedPlayer)
        # QObject control variables
        #
        # Player relevant ctrlVars now here, not in masterscreen


    #     super().__init__(parent)
    #     self.grid()
    #
    #     # control variables for new player form
    #
    #     self.fname = tk.StringVar()
    #     self.lname = tk.StringVar()
    #     self.street = tk.StringVar()
    #     self.city = tk.StringVar()
    #     self.zip = tk.StringVar()
    #     self.phone = tk.StringVar()
    #     self.email = tk.StringVar()
    #     self.accno = tk.StringVar()
    #     self.expiration = tk.StringVar()
    #     self.joined = tk.StringVar()
    #     self.active =tk.IntVar()
    #     self.showAllPlayers = tk.IntVar()
    #     self.showAllPlayers.set(1)
    #
    #     # control variable for existing players
    #     self.players=tk.StringVar()
    #
    #
    #
    #     # build out tab and register with notebook
    #
    #     self.config(padx = '2', pady = '2')
    #     parent.add(self,text='Players')
    #
    #     # perform self-registration under notebook
    #
    #     cfg.screenDict['ptab'] = self
    #
    #     print('Register ptab')
    #
    #     self.oldPlayerPanel = tk.LabelFrame(self,
    #                                          height='10c',
    #                                          width='5c',
    #                                          borderwidth='1c',
    #                                          relief='flat',
    #                                          text='Existing Players'
    #                                          )
    #     self.oldPlayerPanel.columnconfigure(3, weight = 1, uniform='a')
    #     self.oldPlayerPanel.rowconfigure(2,weight=1, uniform='a')
    #     self.oldPlayerPanel.grid(row=0, column=0)
    #
    #     self.asteriskLabel = ttk.Label(self.oldPlayerPanel,
    #                                    text = "* = Active")
    #     self.asteriskLabel.grid(row=0, column=0, sticky='w')
    #
    #     # choose what to show
    #     self.showAll = ttk.Checkbutton(self.oldPlayerPanel,
    #                                    text = 'Show All',
    #                                    on = 1,
    #                                    off = 0,
    #                                    command = self.displayExistingPlayers,
    #                                    variable=self.showAllPlayers)
    #     self.showAll.grid(row=0, column=1)
    #     # for testing
    #     self.showAllPlayers.set(1)
    # #*****************************************************
    # #       list box that shows players
    # #
    #     self.exp = tk.Listbox(self.oldPlayerPanel,
    #                           listvariable=self.players,
    #                           height=20
    #                           )
    #     self.exp.grid(row=1, column=0, columnspan=2)
    #
    #     self.scrollbar = tk.Scrollbar(self.oldPlayerPanel)
    #     self.scrollbar.grid(row=1, column=2, sticky='ns')
    #     self.exp.config(yscrollcommand=self.scrollbar.set)
    #     self.scrollbar.config(command=self.exp.yview)
    #
    #     #
    #     # allow ListBox entry to respond to double click for editing
    #     #
    #     # TODO: F2 will edit player, F3 to create new player, F9 to toggle active status
    #
    #     # # [binding section]
    #     # Do this binding everytime we recreate the listbox of players
    #     self.exp.bind('<F2>', self.editSelectedPlayer)
    #     self.exp.bind('<F3>', self.createPlayer)
    #     self.exp.bind('<F9>', self.toggleAPlayer)
    #     self.noPlayers = tk.Label(self.oldPlayerPanel,
    #                                text='There are no existing players',
    #                                relief='raised',
    #                                borderwidth='4'
    #                                )
    #     self.noPlayers.grid(row=0,
    #                         column=0,
    #                         sticky='ewns')
    #     self.hideWidget(self.noPlayers)
    #
    #     self.newPlayerPanel = tk.LabelFrame(self,
    #                                          height='10c',
    #                                          width='5c',
    #                                          borderwidth='2',
    #                                          relief='sunken',
    #                                          text='New Player'
    #                                          )
    #     self.newPlayerPanel.grid(row=0, column=1, sticky = 'ns')
    #     self.hideWidget(self.newPlayerPanel)
    #
    #     self.editPlayerPanel = tk.LabelFrame(self,
    #                                     height='10c',
    #                                     width = '5c',
    #                                     borderwidth='2',
    #                                     relief = 'sunken',
    #                                     fg = 'red',
    #                                     text = 'Edit Player'
    #                                     )
    #     self.editPlayerPanel.grid(row = 0, column = 1, sticky = 'ns')
    #     self.hideWidget(self.editPlayerPanel)
    #
    #
    #     # [error panel area]
    #     self.dateErrorPanel = tk.LabelFrame(self,
    #                                         height='10c',
    #                                         width = '5c',
    #                                         borderwidth='2',
    #                                         relief = 'sunken',
    #                                         fg = 'red',
    #                                         text = 'Bad Date Format'
    #                                         )
    #     self.dateErrorPanel.grid(row = 0, column = 2, sticky = 'ns')
    #     self.hideWidget(self.dateErrorPanel)
    #     self.dateErrorLabel1 = tk.Label(self.dateErrorPanel,
    #                                    text = 'The date must be in mm/dd/yyyy US format,')
    #     self.dateErrorLabel1.grid(row = 0, column = 0)
    #     self.dateErrorLabel2 = tk.Label(self.dateErrorPanel,
    #                                     text = 'Press F5 to correct and try again.')
    #     self.dateErrorLabel2.grid(row=1, column = 0)
    #     # put the instructions into the Activity panel
    #
    #     self.newPlayerForm(self.newPlayerPanel)
    #     self.buildActivityPanel()
    #     self.displayExistingPlayers()

    #   setup signals for responding to user requests per activity panel

        # [ KEY HANDLER SECTION ]
        self.F2_shortcut = QShortcut(QKeySequence(Qt.Key_F2),self.main.existingPlayersPanel)
        self.F2_shortcut.activated.connect(self.editSelectedPlayer)

        self.F3_shortcut = QShortcut(QKeySequence(Qt.Key_F3), self.main.playerTabPanel)
        self.F3_shortcut.activated.connect(self.createPlayer)

        self.F9_shortcut = QShortcut(QKeySequence(Qt.Key_F9), self.main.existingPlayersPanel)
        self.F9_shortcut.activated.connect(self.togglePlayer)

        self.F10_shortcut = QShortcut(QKeySequence(Qt.Key_F10), self.main.newPlayerFrame)
        self.F10_shortcut.activated.connect(self.handlePlayer)

        self.Esc_shortcut = QShortcut(QKeySequence(Qt.Key_Escape),self.main.playerTabPanel)
        self.Esc_shortcut.activated.connect(self.cancelActivity)

        # edit mode: 0 undef; 1 new player; 2 edit player
        self.pl_editMode = IntVar()

        # [PLAYER SECTION]
        # [PLAYER ctrlVars]
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

        # [PLAYER UI signals]
        self.main.le_firstNameEntry.textChanged.connect(self.pl_firstName.acceptStr)
        self.main.le_lastNameEntry.textChanged.connect(self.pl_lastName.acceptStr)
        self.main.le_streetEntry.textChanged.connect(self.pl_street.acceptStr)
        self.main.le_cityEntry.textChanged.connect(self.pl_city.acceptStr)
        self.main.le_stateEntry.textChanged.connect(self.pl_state.acceptStr)
        self.main.le_zipEntry.textChanged.connect(self.pl_zip.acceptStr)
        self.main.le_phoneEntry.textChanged.connect(self.pl_phone.acceptStr)
        self.main.le_emailEntry.textChanged.connect(self.pl_email.acceptStr)
        self.main.le_accNumberEntry.textChanged.connect(self.pl_ACCNumber.acceptStr)
        self.main.le_joinedEntry.textChanged.connect(self.pl_joined.acceptStr)
        self.main.le_expiresEntry.textChanged.connect(self.pl_expires.acceptStr)
        self.main.le_activeEntry.textChanged.connect(self.pl_active.acceptIntAsStr)

        # [PLAYER ctrlvar signals
        self.pl_firstName.strValueChanged.connect(self.main.le_firstNameEntry.setText)
        self.pl_lastName.strValueChanged.connect(self.main.le_lastNameEntry.setText)
        self.pl_street.strValueChanged.connect(self.main.le_streetEntry.setText)
        self.pl_city.strValueChanged.connect(self.main.le_cityEntry.setText)
        self.pl_state.strValueChanged.connect(self.main.le_stateEntry.setText)
        self.pl_zip.strValueChanged.connect(self.main.le_zipEntry.setText)
        self.pl_phone.strValueChanged.connect(self.main.le_phoneEntry.setText)
        self.pl_ACCNumber.strValueChanged.connect(self.main.le_accNumberEntry.setText)
        self.pl_expires.strValueChanged.connect(self.main.le_expiresEntry.setText)
        self.pl_joined.strValueChanged.connect(self.main.le_joinedEntry.setText)
        self.pl_active.intValueAsStringChanged.connect(self.main.le_activeEntry.setText)


        # [Player validators]
        self.pl_active_validator = QIntValidator(0,1,self)
        self.main.le_activeEntry.setValidator(self.pl_active_validator)

        self.resetErrorMessages()
    # ************************************************************
    #   build out activity panel entries
    def buildActivityPanel(self):

        self.widgetIndex = cfg.stackedActivityDict['playersactivitypanel']
        cfg.screenDict['activitystack'].setCurrentIndex(self.widgetIndex)

        # self.ap = cfg.screenDict['activity']    # get activity panel widget
        # self.keyF1 = tk.Label(self.ap, text = 'F1    Get help with this activity')
        # self.keyF2 = tk.Label(self.ap, text = 'F2    Edit player selected in listbox')
        # self.keyF3 = tk.Label(self.ap, text = 'F3    Create a new player')
        # self.keyF9 = tk.Label(self.ap, text = 'F9    Toggle active status for player selected in listbox')
        # self.keyF10 = tk.Label(self.ap, text = 'F10   Save all current changes')
        # self.keyEsc = tk.Label(self.ap, text = 'Esc   Quit current activity')
        # self.dClick = tk.Label(self.ap, text = 'Double Click to toggle active')
        # self.keyF1.grid(row=1, column=0, sticky='w')
        # self.keyF2.grid( column=0, sticky='w')
        # self.keyF3.grid( column=0, sticky='w')
        # self.keyF9.grid( column=0, sticky='w')
        # self.keyF10.grid( column=0, sticky='w')
        # self.keyEsc.grid( column=0, sticky='w')
        # self.dClick.grid( column=0, sticky='w')

    # ************************************************************
    #   handle tab change by refreshing players
    def tabChange(self):
        # no longer event driven
        # tabchanged signal caught in MasterScreen
        #
        # always refreshes the list of existing players
        self.editMode = 0   # not in any mode
        self.main.lb_newPlayerLabel.show()
        # start clean
        self.resetAllErrorHiLites()
        self.resetErrorMessages()
        self.buildActivityPanel()
        # self.main.listOfPlayers.setEnabled(True)
        self.displayExistingPlayers()

    #************************************************************
    #   build a display of existing players on file

    @qtc.Slot()
    def displayExistingPlayers(self):
        # list out existing players
        # let's add and item or two to the listwidget
        # self.main.listOfPlayers.clear()
        # self.ql0 = QListWidgetItem("Bowers, Yvonne")
        # self.ql1 = QListWidgetItem('Charkarian, Aram')
        # self.main.listOfPlayers.insertItem(0,self.ql0)
        # self.main.listOfPlayers.insertItem(1,self.ql1)
        # self.main.listOfPlayers.insertItem(2,'label')
        # return

        # self.hideWidget(self.noPlayers)
        if Player.select().count() == 0:
            self.main.existingPlayersLabel.setText('No Players!')
        else:
#           print('Get and print players')
#           remove any No Players message
            self.main.existingPlayersLabel.setText('Existing Players')
            # self.hideWidget(self.noPlayers)
            # self.showWidget(self.oldPlayerPanel)

            if self.main.showAllPlayers.isChecked() :
                self.main.existingPlayersLabel.setText('All Players')
                self.existingPlayers = cfg.ap.playersByLastName(cfg.clubRecord)
            else:
                self.main.existingPlayersLabel.setText('Active Players')
                self.existingPlayers = cfg.ap.allActivePlayers(cfg.clubRecord)

            # print ('Show all players retrieved')
            # print (self.existingPlayers)
            # self.existingPlayers = list(Player.select().orderBy('FirstName'))
#            print (self.existingPlayers)
            self.playersInDbms = []
#            print (self.existingPlayers[0].FirstName)
            # always leave room for the active asterisk

            self.main.listOfPlayers.clear()

            for p in self.existingPlayers:
                if p.Active > 0:
                    self.playersInDbms.append(' * ' + p.LastName + ', ' +p.FirstName)
                else:
                    self.playersInDbms.append('   ' + p.LastName + ', ' + p.FirstName)

            self.main.listOfPlayers.insertItems(0,self.playersInDbms)
            # build listbox
            # self.players.set(self.playersInDbms)
            # self.exp = tk.Listbox(self.oldPlayerPanel,
            #                       listvariable=self.players,
            #                       height = 20
            #                       )
            # self.exp.grid(row = 1, column = 0, columnspan = 2)
            #
            # self.scrollbar = tk.Scrollbar(self.oldPlayerPanel)
            # self.scrollbar.grid(row=1, column=2, sticky ='ns')
            # self.exp.config(yscrollcommand=self.scrollbar.set)
            # self.scrollbar.config(command=self.exp.yview)
            #
            # #
            # # allow ListBox entry to respond to double click for editing
            # #
            # # TODO: F2 will edit player, F3 to create new player, F9 to delete player
            #
            # # [binding section]
            # Do this binding everytime we recreate the listbox of players
            # self.exp.bind('<F2>', self.editSelectedPlayer)
            # self.exp.bind('<F3>', self.createPlayer)
            # self.exp.bind('<F9>', self.toggleAPlayer)
            # self.exp.bind('<Double-1>',self.togglePlayer)
        # set focus and selection for listbox
        # self.exp.selection_set(0)
        # self.exp.focus_force()

    # ***********************************************************
    #   handler for double-click player state toggle
    @qtc.Slot(QListWidgetItem)
    def togglePlayer(self,expName):     # DoubleClick handler
        # convert the double-click position into a selection
        # print('togge player active state with stub')
        # return
        # self.exp.selection_clear(0,tk.END)     # clear any current selection
        # self.lbIndex = self.exp.nearest(event.y)
        # self.playerInExpName = self.exp.activate(self.lbIndex)
        # strip any * then trim blanks from name
        self.lbText = expName.text()
        # print ('Selected ' + self.lbText)
        # print ('Cleaned up <' + self.lbText.replace('*',' ').strip() + '>')
        # print('Player pid:= ' + str(cfg.playerRefx[self.lbText.replace('*',' ').strip()]))
        self.playerToToggle = cfg.ap.getPlayerById(str(cfg.playerRefx[self.lbText.replace('*',' ').strip()]))
        # print(self.playerToToggle.LastName + ' Active:= ' + str(self.playerToToggle.Active))
        # toggle the active status - 0 is inactive; <>0 is active
        if self.playerToToggle.Active == 0:
            self.playerToToggle.Active = 1
        else:
            self.playerToToggle.Active = 0
        # print ('Post Toggle ' + self.playerToToggle.LastName + ' Active:= ' + str(self.playerToToggle.Active))
        # and refresh the list of players
        self.displayExistingPlayers()

    #************************************************************
    #
    def submitNewPlayer(self):
        print('Validate and add new player stub')

        #validate the required fields
        print ('len(fname): ' , len(self.pl_firstName.myValue))
        print ('len(lname): ' , len(self.pl_lastName.myValue))
        print ('fname: ' , self.pl_firstName.myValue)
        print ('lname: ' , self. pl_lastName.myValue)
        print ('active: ', str(self.pl_active.myValue))

        #
        # at a minimum must have first and last name
        #
        # print (self.fname.get())
        # print (self.lname.get())

        if (len(self.pl_firstName.myValue )< 1 or
            len(self.pl_lastName.myValue)< 1):
            # self.redText(self.fnameLabel)
            self.main.lb_missingNames.show()
            self.showNewPlayerError()
            return

        # try adding to the data base and catching any errors

        # if self.checkForNameDup (self.fname.get(), self.lname.get()):
        if self.checkForNameDup (
            self.pl_firstName.myValue,
            self.pl_lastName.myValue
            ):
            self.duplicateName()
            self.showNewPlayerError()
        else:
            # validate any date fields for new player


            try:
                if cfg.debug and cfg.playersdebug:
                    print('First Name: ',self.pl_firstName.myValue)
                    print('Last Name: ',self.pl_lastName.myValue)
                    print('Phone: ',self.pl_phone.myValue)
                    print('Email: ',self.pl_email.myValue)
                    print('ACC No: ',self.pl_ACCNumber.myValue)
                    print('Joined Date: ',self.pl_joined.myValue)
                    print('Club Id: ',str(cfg.clubId))

                    if (not self.pl_active.myValue == 0 or
                        self.pl_active.myValue == 1):
                        self.pl_active.myValue = 0


                # Create a new player - let date field default for now
                # Handle blank active field
                # this is taken care of inside ctrlVariable
                # if not (self.active.get() == 0 or self.active.get() == 1):
                #     self.active.set(0)
                # Replace with values stored in ctrlVariables
                # self.newPlayer = Player(FirstName  =   self.fname.get(),
                #                      LastName   =   self.lname.get(),
                #                      Street     =   self.street.get(),
                #                      City       =   self.city.get(),
                #                      Zip        =   self.zip.get(),
                #                      Phone      =   self.phone.get(),
                #                      Email      =   self.email.get(),
                #                      ACCNumber  =   self.accno.get(),
                #                      # Joined     =   self.joined.get(),
                #                      # ACCExpiration = self.expiration.get(),
                #                      Active     =   self.active.get(),
                #                      Club       =   cfg.clubId
                #                      )
                # defer handling of missing dates
                # if self.pl_expires.myValue == None:
                #     self.pl_expires.myValue = ' '
                # if self.pl_joined.myValue == None:
                #     self.pl_joined.myValue = ' '

                # defer sorting out dates until after player added
                self.newPlayer = Player(
                    FirstName = self.pl_firstName.myValue,
                    LastName = self.pl_lastName.myValue,
                    Street = self.pl_street.myValue,
                    City = self.pl_city.myValue,
                    Zip = self.pl_zip.myValue,
                    Phone = self.pl_phone.myValue,
                    Email = self.pl_email.myValue,
                    ACCNumber = self.pl_ACCNumber.myValue,
                    # Joined = self.makeIsoDate(self.pl_joined.myValue),
                    # ACCExpiration = self.makeIsoDate(self.pl_expires.myValue),
                    Active = self.pl_active.myValue,
                    Club = cfg.clubId
                )
                # mbx.showinfo(('Player added successfully', 'Use F9 to make Active'))
                # must add any new player to the xrefs
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText('Player '
                                + self.pl_firstName.myValue
                                +' ' + self.pl_lastName.myValue
                                + ' added.'
                               )
                msgBox.setWindowTitle('New Player Added')
                msgBox.setStandardButtons(QMessageBox.Ok)
                result = msgBox.exec()

                # this corrects a prior bug
                self.reBuildXrefs()
                # TODO: special handling required for date fields and blank active field
                # now check date input and format for sqlite
                if (
                    self.pl_expires.myValue != ' ' or
                    self.pl_expires.myValue != None
                    ):
                    if not self.validateADate(
                                self.pl_expires.myValue,
                                self.main.le_expiresEntry):
                        self.showWidget(self.main.lb_badPlayerDateError)
                if (
                    self.pl_joined.myValue != ' ' or
                    self.pl_joined.myValue != None
                    ):
                    if not self.validateADate(
                                self.pl_joined.myValue,
                                self.main.le_joinedEntry):
                        self.showWidget((self.main.lb_badPlayerDateError)
                    )
                if self.main.lb_badPlayerDateError.isVisible():
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText('Esc to quite New then edit date field')
                    msgBox.setWindowTitle('Invalid Dates')
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    result = msgBox.exec()
                    self.setFocus(self.main.le_expiresEntry)
                    return      # leave processing

            except dberrors.DuplicateEntryError:
               # this will only trigger for duplicate ACC nos in the future
               # problem is unique constraint triggers with blanks
                if self.duplicateACCno(): # true means retry
                    # leave the labels red 
                    self.fnameEntry.focus_set()
                else:
                    self.resetForm()

    #************************************************************   
    #   build new player form inside newPlayerPanel
    #
    #   no longer in use...pre-built in masterScreen
    #
    def buildPlayerForm(self, parent):
        pass
        # self.fnameLabel = tk.Label(parent, text='First Name')
        # self.fnameLabel.grid(row=0,column=0)
        # self.lnameLabel = tk.Label(parent, text='Last Name')
        # self.lnameLabel.grid(row=1,column=0)
        # self.streetLabel = tk.Label(parent, text='Street')
        # self.streetLabel.grid(row=2,column=0)
        # self.cityLabel = tk.Label(parent, text='City')
        # self.cityLabel.grid(row=3,column=0)
        # self.zipLabel = tk.Label(parent, text='Zip')
        # self.zipLabel.grid(row=4,column=0)
        # self.phoneLabel = tk.Label(parent, text='Phone')
        # self.phoneLabel.grid(row=5,column=0)
        # self.emailLabel = tk.Label(parent, text='Email')
        # self.emailLabel.grid(row=6,column=0)
        # self.accnoLabel = tk.Label(parent, text='ACC Number')
        # self.accnoLabel.grid(row=7,column=0)
        # self.expirationLabel = tk.Label(parent, text='Expires')
        # self.expirationLabel.grid(row=8,column=0)
        # self.joinedLabel = tk.Label(parent, text='Joined')
        # self.joinedLabel.grid(row=9,column=0)
        # self.activeLabel = tk.Label(parent, text='Active')
        # self.activeLabel.grid(row=10,column=0)
        # self.fnameEntry = tk.Entry(parent, textvariable=self.fname)
        # self.fnameEntry.grid(row=0,column=1)
        # self.lnameEntry = tk.Entry(parent, textvariable=self.lname)
        # self.lnameEntry.grid(row=1, column=1)
        # self.streetEntry = tk.Entry(parent, textvariable=self.street)
        # self.streetEntry.grid(row=2, column=1)
        # self.cityEntry = tk.Entry(parent, textvariable=self.city)
        # self.cityEntry.grid(row=3, column=1)
        # self.zipEntry = tk.Entry(parent, textvariable=self.zip)
        # self.zipEntry.grid(row=4, column=1)
        # self.phoneEntry = tk.Entry(parent, textvariable=self.phone)
        # self.phoneEntry.grid(row=5, column=1)
        # self.emailEntry = tk.Entry(parent, textvariable=self.email)
        # self.emailEntry.grid(row=6, column=1)
        # self.accnoEntry = tk.Entry(parent,textvariable=self.accno)
        # self.accnoEntry.grid(row=7, column=1)
        # self.expirationEntry = tk.Entry(parent, textvariable=self.expiration)
        # self.expirationEntry.grid(row=8, column=1)
        # self.joinedEntry = tk.Entry(parent, textvariable=self.joined)
        # self.joinedEntry.grid(row=9, column=1)
        # self.activeEntry = tk.Entry(parent, textvariable=self.active)
        # self.activeEntry.grid(row=10, column=1)
        #
        # # navigation key binding
        # self.fnameEntry.bind('<Key-Down>',self.handleDownKey)
        # self.lnameEntry.bind('<Key-Down>', self.handleDownKey)
        # self.streetEntry.bind('<Key-Down>', self.handleDownKey)
        # self.cityEntry.bind('<Key-Down>', self.handleDownKey)
        # self.zipEntry.bind('<Key-Down>', self.handleDownKey)
        # self.phoneEntry.bind('<Key-Down>', self.handleDownKey)
        # self.emailEntry.bind('<Key-Down>', self.handleDownKey)
        # self.accnoEntry.bind('<Key-Down>', self.handleDownKey)
        # self.expirationEntry.bind('<Key-Down>', self.handleDownKey)
        # self.joinedEntry.bind('<Key-Down>', self.handleDownKey)
        #
        #
        # self.lnameEntry.bind('<Key-Up>', self.handleUpKey)
        # self.streetEntry.bind('<Key-Up>', self.handleUpKey)
        # self.cityEntry.bind('<Key-Up>', self.handleUpKey)
        # self.zipEntry.bind('<Key-Up>', self.handleUpKey)
        # self.phoneEntry.bind('<Key-Up>', self.handleUpKey)
        # self.emailEntry.bind('<Key-Up>', self.handleUpKey)
        # self.accnoEntry.bind('<Key-Up>', self.handleUpKey)
        # self.expirationEntry.bind('<Key-Up>', self.handleUpKey)
        # self.joinedEntry.bind('<Key-Up>', self.handleUpKey)
        # self.activeEntry.bind('<Key-Up>', self.handleUpKey)
        #
        # # always position at first entry field.
        # self.fnameEntry.focus_force()
    # ************************************************************
    #
    @qtc.Slot()
    # determine where to route F10
    def handlePlayer(self):
        # reset all error fields before try/retry
        self.resetAllErrorHiLites()
        self.resetErrorMessages()
        if self.pl_editMode.myValue == 1:
            self.submitNewPlayer()
        elif self.pl_editMode.myValue == 2:
            self.editAPlayer()
        elif self.pl_editMode.myValue == 0:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Need to use F2 or F3 first')
            msgBox.setWindowTitle('New/Edit not selected')
            msgBox.setStandardButtons(QMessageBox.Ok )
            result = msgBox.exec()
            self.main.lb_newPlayerLabel.setText('Edit F2 - New F3')
            return      # do nothing


    def createPlayer(self):
        print ('create player stub')
        self.pl_editMode.myValue = 1       # show new player mode
        self.resetForm()
        self.main.lb_newPlayerLabel.setText('New Player')
       # clear out the input form
        self.main.le_firstNameEntry.setFocus()
        # self.hideWidget(self.editPlayerPanel)
        # self.showWidget(self.newPlayerPanel)
        # self.resetAllErrorHiLites()
        # self.fnameEntry.focus_force()
        # self.fnameEntry.select_range(0, tk.END)
    #************************************************************
    #
    def newPlayerForm(self, parent):
        self.buildPlayerForm(parent)
        # all key binding happens in __init__ at the panel level
        # # [newplayer form binding section]
        # self.fnameEntry.bind('<F10>', self.submitNewPlayer)
        # self.lnameEntry.bind('<F10>', self.submitNewPlayer)
        # self.streetEntry.bind('<F10>', self.submitNewPlayer)
        # self.cityEntry.bind('<F10>', self.submitNewPlayer)
        # self.zipEntry.bind('<F10>', self.submitNewPlayer)
        # self.phoneEntry.bind('<F10>', self.submitNewPlayer)
        # self.emailEntry.bind('<F10>', self.submitNewPlayer)
        # self.accnoEntry.bind('<F10>', self.submitNewPlayer)
        # self.expirationEntry.bind('<F10>', self.submitNewPlayer)
        # self.activeEntry.bind('<F10>', self.submitNewPlayer)
        # self.joinedEntry.bind('<F10>', self.submitNewPlayer)
        # self.activeEntry.bind('<F10>', self.submitNewPlayer)
        # self.fnameEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.lnameEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.streetEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.cityEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.zipEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.phoneEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.emailEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.accnoEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.expirationEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.activeEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.joinedEntry.bind('<Escape>', self.cancelNewPlayer)
        # self.activeEntry.bind('<Escape>', self.cancelNewPlayer)

    #************************************************************
    #
    def setUpEditPlayerPanel (self):
        #this where we put the selected player info into the edit form
        self.resetAllErrorHiLites()     # just in case entry form was not cleaned up
        self.resetErrorMessages()
        # self.hideWidget(self.newPlayerPanel)
        # self.showWidget(self.editPlayerPanel)
        self.main.lb_newPlayerLabel.setText('Edit Player')
        self.editPlayerForm()
        # self.setFocus(self.fnameEntry)
        # self.showSelected(self.fnameEntry)
   
    #************************************************************
    #
    #
    #   ui fields longer required - pre-built in masterscreen
    #
    def editPlayerForm(self):
    #     print ('Build edit player widgets')
    #     # joinedOn = self.existingPlayers[self.ListBoxIndex].Joined
    #     # ACCExpiresOn = self.existingPlayers[self.ListBoxIndex].ACCExpiration
    #     # print ('joineOn ', joinedOn)
    #     # print ('ACCExpiresOn ', ACCExpiresOn)
    #     # self.buildPlayerForm(parent)
    #     # print ('Player to be edited')
    #     # print (self.existingPlayers[self.ListBoxIndex])
    #     # self.fname.set(self.existingPlayers[self.ListBoxIndex].FirstName)
    #     # self.lname.set(self.existingPlayers[self.ListBoxIndex].LastName)
    #     # self.street.set(self.existingPlayers[self.ListBoxIndex].Street)
    #     # self.city.set(self.existingPlayers[self.ListBoxIndex].City)
    #     # self.zip.set(self.existingPlayers[self.ListBoxIndex].Zip)
    #     # self.phone.set(self.existingPlayers[self.ListBoxIndex].Phone)
    #     # self.email.set(self.existingPlayers[self.ListBoxIndex].Email)
    #     # self.accno.set(self.existingPlayers[self.ListBoxIndex].ACCNumber)
    #     # self.expiration.set(self.testDateIsNone(ACCExpiresOn))
    #     # self.joined.set(self.testDateIsNone(joinedOn))
    #     # self.active.set(self.existingPlayers[self.ListBoxIndex].Active)
    #     #


    #     # # [edit player form binding section]
    #     # self.fnameEntry.bind('<F10>', self.editAPlayer)
    #     # self.lnameEntry.bind('<F10>', self.editAPlayer)
    #     # self.streetEntry.bind('<F10>', self.editAPlayer)
    #     # self.cityEntry.bind('<F10>', self.editAPlayer)
    #     # self.zipEntry.bind('<F10>', self.editAPlayer)
    #     # self.phoneEntry.bind('<F10>', self.editAPlayer)
    #     # self.emailEntry.bind('<F10>', self.editAPlayer)
    #     # self.accnoEntry.bind('<F10>', self.editAPlayer)
    #     # self.expirationEntry.bind('<F10>', self.editAPlayer)
    #     # self.activeEntry.bind('<F10>', self.editAPlayer)
    #     # self.joinedEntry.bind('<F10>', self.editAPlayer)
    #     # self.fnameEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.lnameEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.streetEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.cityEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.zipEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.phoneEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.emailEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.accnoEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.expirationEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.activeEntry.bind('<Escape>', self.cancelPlayerEdit)
    #     # self.joinedEntry.bind('<Escape>', self.cancelPlayerEdit)

    #************************************************************
    #
        if cfg.debug and cfg.playersdebug:
            print ('Populate edit player form')
        # pull info from self.existingPlayers used to
        # populate list of players
        # rely on ctrlVars connected to ui fields
        # listBoxIndex is set in editSelectedPlayer
            print ('listBoxIndex: ', self.listBoxIndex)
            print ('firstName: ', self.existingPlayers[self.listBoxIndex].FirstName)
        self.pl_firstName.myValue = self.existingPlayers[self.listBoxIndex].FirstName
        self.pl_lastName.myValue = self.existingPlayers[self.listBoxIndex].LastName
        self.pl_street.myValue = self.existingPlayers[self.listBoxIndex].Street
        self.pl_city.myValue = self.existingPlayers[self.listBoxIndex].City
        self.pl_zip.myValue = self.existingPlayers[self.listBoxIndex].Zip
        self.pl_phone.myValue = self.existingPlayers[self.listBoxIndex].Phone
        self.pl_email.myValue = self.existingPlayers[self.listBoxIndex].Email
        self.pl_ACCNumber.myValue = self.existingPlayers[self.listBoxIndex].ACCNumber
        self.pl_expires.myValue = self.existingPlayers[self.listBoxIndex].ACCExpiration
        self.pl_joined.myValue = self.existingPlayers[self.listBoxIndex].Joined
        self.pl_active.myValue = self.existingPlayers[self.listBoxIndex].Active

        self.main.le_firstNameEntry.setFocus()

    def cancelPlayerEdit (self):
        # restore new Player panel
        print ('back to players panel')
        self.cancelActivity()
        # self.hideWidget(self.editPlayerPanel)
        # self.hideWidget(self.newPlayerPanel)
        # # self.editPlayerPanel.grid_remove()
        # self.resetForm()
        # self.displayExistingPlayers()
        self.resetForm()

    #************************************************************
    #
    #   see togglePlayer for doubleclick handler
    #   tested 1/31/2025
    #
    # def toggleAPlayer(self,item):
    #     print('toggle player active status with double click')
    #     pass
    #     self.ListBoxIndex = event.widget.curselection()[0]
    #     self.deleteMsg = """\tPlayer Toggle is a soft delete that marks player inactive.
    # \tInactive (aka deleted) players do not appear in any reports.
    # \tUndelete returns a player to active status.
    # \tAll results for deleted players are retained."""
        # mbx.showinfo('Toggle a Player', self.deleteMsg)
        # cfg.at.countTourneysForSeason(cfg.season)
        # cfg.ap.getPlayerById(1)
        # togglePlayer = cfg.ap.singlePlayerByFirstandLastNames(self.existingPlayers[self.ListBoxIndex].FirstName,
        #                                               self.existingPlayers[self.ListBoxIndex].LastName)
        # playerName = togglePlayer.FirstName + ' ' + togglePlayer.LastName
        # if togglePlayer.Active == 0:
        #     togglePlayer.Active = 1
        #     mbx.showinfo(playerName , 'is now Active')
        # else:
        #     togglePlayer.Active = 0
        #     mbx.showinfo(playerName, 'is no longer Active')
    # print (togglePlayer)

    #************************************************************
    #
    #   see editAPlayer
    #
    @qtc.Slot(QListWidgetItem)
    def listItemEntered(self, value):
        print ('Entered Item: ', value.text())
        self.main.listOfPlayers.setCurrentItem(value)
    @qtc.Slot()
    def trackSelectedPlayer(self):
        # print ('Row changed: ', newRow)
        # capture selection row change
        self.listBoxIndex = self.main.listOfPlayers.currentRow()
        # set focus to that item
        self.main.listOfPlayers.setCurrentItem(
                                self.main.listOfPlayers.item(self.listBoxIndex)
                                )

    def editSelectedPlayer(self):
        print ('Edit selected player from listbox')
        self.pl_editMode.myValue = 2    # edit mode
        self.resetForm()        # clear out the entry area
        #
        # replace NewPlayer panel with EditPlayer panel
        # print ('ListBoxIndex: ', self.ListBoxIndex)
        # # self.editEntry = self.exp.get(self.ListBoxIndex)
        # # print (self.editEntry)
        self.setUpEditPlayerPanel()

        
    #************************************************************
    #
    # This is now a slot that receives the QListWidgetItem directly
    #

    def editAPlayer (self):
        # value is QListWidgetItem currently with focus
        print ('Replace player entry')
        # return
        # this will return a player object for the player under edit
        # self.lbText = expName.text()
        changePlayer = cfg.ap.singlePlayerByFirstandLastNames(
                            self.existingPlayers[self.listBoxIndex].FirstName,
                            self.existingPlayers[self.listBoxIndex].LastName
                            )


        # changePlayer = cfg.ap.singlePlayerByFirstandLastNames(self.existingPlayers[self.ListBoxIndex].FirstName,
        #                                               self.existingPlayers[self.ListBoxIndex].LastName)
        # changePlayer = Player.select(Player.q.FirstName == (self.exp[self.ListBoxIndex].FirstName))[0]
        print ('ChangePlayer ', changePlayer)

        # # First we check out the date fields for any errors which need to be corrected.
        # # Turn off any prior errors
        self.resetErrorHiLite(self.main.le_joinedEntry)
        self.resetErrorHiLite(self.main.le_expiresEntry)

        if self.pl_expires.myValue != None:
        # self.hideWidget(self.dateErrorPanel)
        # if self.expiration.get() != 'None':
            if not (self.validateADate(self.pl_expires.myValue, self.main.le_expiresEntry)):
                # self.showDateErrorPanel()
                self.setFocus(self.main.le_expiresEntry)
                return  # leave, let user try again
        if self.pl_joined.myValue != 'None':
            if not (self.validateADate(self.pl_joined.myValue, self.main.le_joinedEntry)):
                # self.showDateErrorPanel()
                self.main.le_joinedEntry,setFocus()
                return      # leave, let user try again

        # changePlayer.FirstName  = self.fname.get()
        # changePlayer.LastName   = self.lname.get()
        # changePlayer.Street     = self.street.get()
        # changePlayer.City       = self.city.get()
        # changePlayer.Zip        = self.zip.get()
        # changePlayer.Phone      = self.phone.get()
        # changePlayer.Email      = self.email.get()
        # changePlayer.ACCNumber  = self.accno.get()
        # if self.expiration.get() != 'None':
        #     changePlayer.ACCExpiration = self.makeIsoDate(self.expiration.get())
        # # changePlayer.ACCExpiration = '' if self.expiration.get() == 'None' else self.makeIsoDate(self.expiration.get())
        # changePlayer.Active     = self.active.get()
        # if self.joined.get() != 'None':
        #     changePlayer.Joined = self.makeIsoDate(self.joined.get())
        # changePlayer.Joined     = '' if self.joined.get() == 'None' else self.makeIsoDate(self.joined.get())
    #************************************************************
    #
    def cancelActivity(self):
        print('Cancel player activity stub')
        # print('Player: ' + self.main.listOfPlayers.currentItem().text())
        # return
        self.resetForm()
        self.main.listOfPlayers.setCurrentItem(self.main.listOfPlayers.item(0))
        self.setFocus(self.main.listOfPlayers)

        # self.hideWidget(self.newPlayerPanel)
        # self.exp.selection_clear(0, self.exp.size()-1)
        # self.exp.selection_set(0)
        # self.exp.activate(0)
        # self.exp.focus_force()
        
    #************************************************************
    #
    def showNewPlayerError (self):
        if cfg.debug and cfg.playersdebug:
            print ('New Player input error')
        self.errorHiLite(self.main.le_firstNameEntry)
        self.errorHiLite(self.main.le_lastNameEntry)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('One or more new player errors')
        msgBox.setWindowTitle('New Player Errors')
        msgBox.setStandardButtons(QMessageBox.Ok )

        result = msgBox.exec()

        self.main.le_firstNameEntry.setFocus()
        # if result != QMessageBox.Ok:
        #     sys.exit('Wrong data base in use')
        # else:
        #     print('QMessageBox dropped thru')
        # return mbx.askretrycancel('Missing Name Input',
        #                                       'Retry Input or Quit?',
        #                                       parent = self.newPlayerPanel)
        #
        # check for missing input
        # if self.fname == '':
    #************************************************************
    #
    def checkForNameDup(self, fname, lname):
        dupPlayerTest = Player.select(
            AND(Player.q.FirstName == fname,
                Player.q.LastName == lname))
        if len(list(dupPlayerTest)) > 0:
            return True
        else:
            return False
            
    #************************************************************
    #
    def duplicateACCno(self):
        if cfg.debug and cfg.playersdebug:
            print ('Duplicate acc number error')
        self.errorHiLite(self.main.le_firstNameEntry)
        self.errorHiLite(self.main.le_lastNameEntry)
        self.errorHiLite(self.main.le_accNumberEntry)
        self.main.lb_duplicatePlayerNameError.show()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('Ouplicate ACC Number')
        msgBox.setWindowTitle('Player Already Exists')
        msgBox.setStandardButtons(QMessageBox.Ok )

        result = msgBox.exec()
        # just leave things alone for now so user can overtype
        # maybe just pop a std dialog asking try again or

        
        # retryPlayerEntry = mbx.askretrycancel('Duplicate ACC#',
        #                    'Retry Input or Quit?',
        #                    parent = self.newPlayerPanel)
        # return (retryPlayerEntry)

    #************************************************************
    #
    def duplicateName(self):
        self.errorHiLite(self.main.le_firstNameEntry)
        self.errorHiLite(self.main.le_lastNameEntry)
        self.main.lb_duplicatePlayerNameError.show()
        self.setFocus(self.main.le_firstNameEntry)
        # just leave things alone for now so user can overtype
        # maybe just pop a std dialog asking try again or
        # retryPlayerEntry = mbx.askretrycancel('Duplicate Name',
        #                    'Retry Input or Quit?',
        #                    parent = self.newPlayerPanel)
        # return (retryPlayerEntry)

    #************************************************************
    #
    #   change to PyQt field names.
    def resetForm(self):
        # blank out all form fields via text variables
        # pass
        self.main.le_firstNameEntry.setText('')
        self.main.le_lastNameEntry.setText('')
        self.main.le_streetEntry.setText('')
        self.main.le_cityEntry.setText('')
        self.main.le_stateEntry.setText('')
        self.main.le_zipEntry.setText('')
        self.main.le_phoneEntry.setText('')
        self.main.le_emailEntry.setText('')
        self.main.le_accNumberEntry.setText('')
        self.main.le_expiresEntry.setText('')
        self.main.le_joinedEntry.setText('')
        self.main.le_activeEntry.setText('')

        self.resetErrorMessages()
        self.resetAllErrorHiLites()


        self.main.lb_newPlayerLabel.setText('Edit F2 - New F3')
        # self.fname.set('')
        # self.lname.set('')
        # self.street.set('')
        # self.city.set('')
        # self.zip.set('')
        # self.phone.set('')
        # self.email.set('')
        # self.accno.set('')
        # self.expiration.set('')
        # self.active.set('')
        # self.joined.set('')
        # self.blackText(self.fnameLabel)
        # self.blackText(self.lnameLabel)
        # self.fnameEntry.focus_set()
        # self.blackText(self.fnameLabel)
        # self.blackText(self.lnameLabel)

    #************************************************************
    #
    # def addNewPlayer(self):
    #     self.resetForm()
    #
    # def handleDownKey(self, event):
    #     print ('Handle down key')
    #     # downDict = {
    #     #     self.fnameEntry:    self.lnameEntry,
    #     #     self.lnameEntry:    self.streetEntry,
    #     #     self.streetEntry:   self.cityEntry,
    #     #     self.cityEntry:     self.zipEntry,
    #     #     self.zipEntry:      self.phoneEntry,
    #     #     self.phoneEntry:    self.emailEntry,
    #     #     self.emailEntry:    self.accnoEntry,
    #     #     self.accnoEntry:    self.expirationEntry,
    #     #     self.expirationEntry: self.joinedEntry,
    #     #     self.joinedEntry:   self.activeEntry
    #     #     }
    #     downDict[event.widget].focus_force()
    #     downDict[event.widget].select_range(0, tk.END)
    #
    # def handleUpKey(self, event):
    #     print ('Handle Up Key')
    #     # upDict = {
    #     #     self.lnameEntry:    self.fnameEntry,
    #     #     self.streetEntry:   self.lnameEntry,
    #     #     self.cityEntry:     self.streetEntry,
    #     #     self.zipEntry:      self.cityEntry,
    #     #     self.phoneEntry:    self.zipEntry,
    #     #     self.emailEntry:    self.phoneEntry,
    #     #     self.accnoEntry:    self.emailEntry,
    #     #     self.expirationEntry: self.accnoEntry,
    #     #     self.joinedEntry:   self.expirationEntry,
    #     #     self.activeEntry:   self.joinedEntry
    #     # }
    #     upDict[event.widget].focus_force()
    #     upDict[event.widget].select_range(0, tk.END)

    def setFocus(self, target):
        target.setFocus()
    # def showSelected(self, w):
    #     w.select_range(0, tk.END)
    # def showDateErrorPanel(self):
    #     self.showWidget(self.dateErrorPanel)
    # def hideDateErrorPanel(self):
    #     self.hideWidget((self.dateErrorPanel))
    # #************************************************************
    # #
    # def hideWidget(self, w):
    #     w.grid_remove()
    # #************************************************************
    # #
    # def showWidget(self,w):
    #     w.grid()
    # #************************************************************
    #
    def redText(self,w):
        # w.config(foreground='red')
        w.setStyleSheet('color=red')
    #************************************************************
    #
    def blackText(self,w):
        w.setStyleSheet('color=black')
        # w.config(foreground='black')
    def errorHiLite(self, w):
        w.setStyleSheet('background-color=pink; color=black')
        # w.config(background = 'pink', foreground = 'black')
    def resetErrorHiLite(self, w):
        w.setStyleSheet('background-color=white; color=black')
        # w.config(background = 'white', foreground = 'black')
    def resetAllErrorHiLites(self):
        # cycle through any fields that might have been  highlighted
        # pass
        self.resetErrorHiLite(self.main.le_firstNameEntry)
        self.resetErrorHiLite(self.main.le_lastNameEntry)
        self.resetErrorHiLite(self.main.le_zipEntry)
        self.resetErrorHiLite(self.main.le_phoneEntry)
        self.resetErrorHiLite(self.main.le_emailEntry)
        self.resetErrorHiLite(self.main.le_accNumberEntry)
        self.resetErrorHiLite(self.main.le_expiresEntry)
        self.resetErrorHiLite(self.main.le_joinedEntry)
        self.resetErrorHiLite(self.main.le_activeEntry)
        # self.resetErrorHiLite(self.fnameEntry)
        # self.resetErrorHiLite(self.lnameEntry)
        # self.resetErrorHiLite(self.zipEntry)
        # self.resetErrorHiLite(self.activeEntry)
        # self.resetErrorHiLite(self.expirationEntry)
        # self.resetErrorHiLite(self.joinedEntry)
    def validateADate(self, value, w):
        # validate value as a good US data; errorlite widget w if wrong
        # use the parser funcion to create a datetime.date object - or None
        # TODO have to allow for an empty date field
        self.resetErrorHiLite(w)
        if not dateparser.parse(value):
            #bad date
            self.errorHiLite(w)
            self.main.lb_badPlayerDateError.show()
            return False
        else:
            self.resetErrorHiLite(w)
            return True
    def makeIsoDate(self, USDate):
        # take date in US format and turn into ISO8601 format for data object
        # print (dateparser.parser(USDate).date().isoformat())
        return dateparser.parse(USDate).date().isoformat()
    def makeUSDate(self, ISODate):
        # presumes incoming date is valid ISODate
        return ISODate.strftime('%m/%e/%Y')
    def testDateIsNone(self, dateValue):
        return dateValue  if dateValue is None else self.makeUSDate(dateValue)
    def reBuildXrefs(self):
        # cfg.playerXref = {p.id: p.LastName + ', ' + p.FirstName for p in list(Player.select())}
        CribbageStartup.createPlayersXRef()

    def installPlayersActivity(self):
        print ('install players activity panel')

        # have to add insert the master activity stacked widget
        self.widx = cfg.screenDict['activitystack'].addWidget(self)
        # remember this index
        cfg.stackedActivityDict['playersactivitypanel'] = self.widx

    # def eventFilter(self, obj, event):
    #     print ('Event: ', event.type().name)
    #     if event.type().value == QEvent.MouseButtonPress:
    #         print('saw mouse button')
    #         self.toggleAPlayer()
    #         return True
    #     else:
    #         print(event.type())
    #         return False    # stop propagation for now
    # def resetResultLineHiLites(self):
    #     self.resetScoringErrorHiLite(self.main.lw_resultLinePlayerGp)
    #     self.resetScoringErrorHiLite(self.main.lw_resultLinePlayerGW)
    #     self.resetScoringErrorHiLite(self.main.lw_resultLinePlayerSprd)
    #     self.resetScoringErrorHiLite(self.main.lw_resultLinePlayerTkn)
    #     self.resetScoringErrorHiLite(self.main.lw_resultLinePlayerCash)
        # self.resetScoringErrorHiLite(self.resultsGpEntry)
        # self.resetScoringErrorHiLite(self.resultsGwEntry)
        # self.resetScoringErrorHiLite(self.resultsSprdEntry)
        # self.resetScoringErrorHiLite(self.resultsTknEntry)
    # def hiLiteGamePoints(self,w):
    #     self.hilite(w)
    def hilite(self, w):
        w.setStyleSheet('background-color: blue; color: yellow')
        # w.config(background='blue', foreground='yellow')

    def resetHilite(self, w):
        w.setStyleSheet('background-color: whitesmoke; color: black')
        # w.config(background='whitesmoke', foreground='black')

    def errorHiLite(self, w):
        w.setStyleSheet('background-color: red; color: white')
        # w.config(background='red', foreground='white')

    # def resetScoringErrorHiLite(self, w):
    #     self.resetEntryHiLite(w)

    def resetEntryHiLite(self, w):
        w.setStyleShee('background-color: white; color: black')
        # w.config(background='white', foreground='black')
    # def hideResultLineErrorMessages(self):
    #     self.hideWidget(self.gpError)
    #     self.hideWidget(self.gwError)
    #     self.hideWidget(self.spreadError)
    #     self.hideWidget(self.cashError)
    #     self.hideWidget(self.tknError)
    # def hideResultsInputPanel(self):
    #
    #     self.hideWidget(self.resultsInputPanel)
    # def hideResultsInstructionsPanel(self):
    #
    #     self.hideWidget(self.resultsEntryInstructionsPanel)
    # def showResultsInputPanel(self):
    #
    #     self.showWidget(self.resultsInputPanel)
    # def showResultsInstructionsPanel(self):
    #
    #     self.showWidget(self.resultsEntryInstructionsPanel)
    def hideWidget(self, w):
        w.hide()
        # w.hide()

    def showWidget(self, w):
        w.show()
        # w.grid()

    def resetErrorMessages(self):
        self.hideWidget(self.main.lb_missingNames)
        self.hideWidget(self.main.lb_badPlayerDateError)
        self.hideWidget(self.main.lb_duplicatePlayerNameError)
        self.hideWidget(self.main.lb_badPlayerEmailError)
        self.hideWidget(self.main.lb_badPlayerAccNumberError)

