# cribbage.py

#
#	11/4/2024 converted to PySide6 (PyQt)
#
#	All of the ui definitions are now located in masterscreenV3.py
#	which was generated from masterscreenV3.ui
#
# 	7/20/2020 cloned from peggers.py
#
#################################################
#                                               #
#   Track scores each week for club  cribbage   #
#                                               #
#   All screen and tab creation promote to here #
#                                               #
#   Follow PEP8 naming conventions              #
#################################################

############# testing databse ######################
#	cribbageconfig.py uses test_dbms for all testing
# 	change to prot_dbms when using in production
####################################################

###################################################
#
#   Index of modules used
#
#   cribbageconfig.py as cfg    globals
#   cribbagetartup.py           kicks everything else off
#
#   Struct modules
#   
#   club.py                     sqlobject for Club record
#   tourney.py                  sqlobject for Tourney record
#   player.py                   sqlobject for Player record
#   scorecard.py                sqlobject for ScoreCard record
######### obsolete game record
#   game.py                     sqlobject for Game record
#########
#
#   Mem struct modules          used for fast results checking
######### mem structs are now obsolete
#
#   lists of sqlobjects for the records serve the same purpose
#
#
#   Screen builders        Dict Key
#
#   <>                      root        app root level window
#   startup                 main        top level container
#   masterscreenV3.py       master      container frame
#                           club        club header frame
#                           activity    activity header frame
#                           notebook    notebook frame for all tabs
#   playerstab.py           ptab        for add/change/del players
#   tourneystab.py          ttab        for add/change/del tourneys
#   resultstab.py           rsltab
#   reportstab.py           rtab        select/print reports
#
################## obsolete tabs ################
#	Removed Nov 2024 in Qt rewrite
#   finishtab.py            ftab        wrap up - update db as required
#   helptab.py              htab        help tab
#   cribbagesetup.py        sets        setting/resetting the cribbage environment
################################################

################## obsolete tabs #############################################
#   scoringtab.py           sctab       capture score cards and games
#   validatetab.py          vtab        validate/correct recorded scores
#   tourneyplayerstab.py    tptab       add/change/del/seat tourney players
#   seatingtab.py           stab        capture games & score cards
##############################################################################
#   Action modules
#
#   Because most actions are associated with Variable() object closely
#   associated with the tkinter widgets, the actions will mostly be
#   contained along with the screen definition modules.
#
#   Results that need to be shared across modules will be promoted up
#   to the cribbageconfig module with cfg. prefix
#
################################################################################

########################## Qt Control variable equivalents #####################
#	CtrlVars provides StringVar, IntVar, DoubleVar QtObjects properties that emulate
#	the	tkinter control variables.
#	They act just like Python properties and are get and set with name.property notation
#	No longer do they use the get and set syntax used by tkinter control variables.
#	When changed variables emit a str|int|dbl changed signal
#	When read variables emil a str|int|dbl read signal
#	The signals from the specific instances can be connected to a target slot
#################################################################################

# block of outstanding changes
# TODO: Set-up screen for location of reports, progs, database
# TODO: Allow confirmation to build blank database or copy from incoming populated database
# TODO: Package application for installing on a clean PC or Mac
# TODO: Checks for SQLite, SQLObjects, Python version, tkinter package
# TODO: Replace tkinter et al with PySide6 PyQt for screen definitions
# TODO: Player
#       TODO:   Allow assignment/change of club affiliation for a player
# TODO: Reports
#       TODO:   If reports runs and no tourney selected, message user then recycle
#       TODO:   Add configurable set of weekly reports, not just all
# TODO: Clubs
#       TODO:   Provide screen to define new clubs in the data base.
# TODO: Set-up screen to change club paramaters and create clean database
# TODO: Build quarter tourney allocation screen
# TODO: Test for Python minimum install of Python 3.8.1
#       assert sys.version_info >= (3,7) reqs for fromisoformat()
# TODO: Allow removal of results from results page
# TODO: Check for duplicate entry of results
# TODO: Run dbms scrub for conflicts - as this screws up reporting!
# TODO: Check editing of players - throws errors on dates.

# System imports
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox as mbx
# from tkinter import filedialog as fdg

# Qt ui imports
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtGui import	QShortcut, QKeySequence,Qt

import sys as sys
import os as os
from sqlobject import *

# Personal imports
from ctrlVariables import StringVar, IntVar, DoubleVar

# dbms imports

from accessPlayers      import AccessPlayers
from accessTourneys     import AccessTourneys
from accessResults      import AccessResults
from accessClubs        import AccessClubs

import cribbageconfig 	as cfg
from cribbagestartup    import CribbageStartup

from masterscreenV3      import MasterScreen

#from playerstab         import PlayersTab
# from tourneystab  		import TourneysTab
# from resultstab         import ResultsTab
# from reportstab         import ReportsTab

from player import Player


class Cribbage (object):
	#************************************************************
	#   high level GUI
	#
	def __init__(self):
		# received parent will be the Master Window called Master
		# super().__init__(parent)
		# self.grid(sticky='nsew')
		# self.parent = parent
		# self.parent.grid()
		# self.parent.title(title)
		# self.rowconfigure(0,weight=1, uniform='a')
		# self.columnconfigure(0,weight=1, uniform='a')
		# cfg.screenDict['cribbage'] = self  # register this frame
		# print ('Starting  Cribbage')
		# build global xref files
		# moved to peggersstartup.py
		# self.createPlayersXref()
		# self.createClubXref()
		# self.openAccessModules()

			# call class level init methods
		print ('Starting cribbage...')

		CribbageStartup.initGlobalCfg()
		# CribbageStartup.createPlayersXref()
		# CribbageStartup.createClubXref()
		# CribbageStartup.createTourneyXref()

		self.buildPanels()
		# on return MasterScreen has built everything

	#************************************************************
	#
	#   call all the modules that build panels for the app
	#   Each screen will also register itself in cfg.screenDict
	#
	def buildPanels (self):
		pass
		# build master inside senior panel
		# master sets up the notebook panel to be used by all tabs
		# with Qt all of the tab static definitions are done inside MasterScreen
		# MasterScreen()		# this should be from masterscreenV3 import
		# build out the tabs into notebook and self register themselves
		# when done, position in first tab
		#
		####################################################
		# tabs will be responsible for:
		#	connecting up control variables
		#	capturing events from fields
		#	showing their appropriate activity panel
		####################################################
		# PlayersTab(cfg.screenDict['notebook'])
		# TourneysTab(cfg.screenDict['notebook'])
		# ResultsTab(cfg.screenDict['notebook'])
		# ReportsTab(cfg.screenDict['notebook'])
		# FinishTab(cfg.screenDict['notebook'])
		# HelpTab(cfg.screenDict['notebook'])
		# cfg.screenDict['notebook'].select(1)    # reposition back at TourneysAtb

		# self.setNotebookEventCapture()

	# def openAccessModules(self):
	# 	# create an instance of each access module in cfg
	# 	cfg.ap = AccessPlayers()
	# 	cfg.at = AccessTourneys()
	# 	cfg.ar = AccessResults()

	#************************************************************
	#   capture notebook tab events one place
	#
	# def setNotebookEventCapture(self):
	# 	print ('generic notebook tab event capture')
	# 	cfg.screenDict['notebook'].bind('<<NotebookTabChanged>>',self.tabChange)


	#************************************************************
	#   route captured tab event
	#
	#	now donw with a QTabWidget signal handled in MasterScreen

# def tabChange (self,tabIndex):
# 	tabIndex = cfg.screenDict['notebook'].currentIndex
# 	print('Tab Index:=',tabIndex)
# 	cfg.screenDict['notebook'].setIndex(tabIndex)
	# if tabIndex == 0:
	# 	# pass
	# 	cfg.screenDict['ptab'].tabChange(event)
	# elif tabIndex == 1:
	# 	# pass
	# 	cfg.screenDict['ttab'].tabChange(event)
	# elif tabIndex == 2:
	# 	cfg.screenDict['rsltstab'].tabChange(event)
	# elif tabIndex == 3:
	# 	cfg.screenDict['rptsab'].tabChange(event)


if __name__ == '__main__':

	# cfg variables should now be populated

	######################################################
	#
	#	All of the QApplications stuff will be handled inside
	#	masterscreenV3 as that's where all the UI is located
	######################################################
	# # put root frame object into config module dictionary
	# app = QtWidgets.QApplication(sys.argv)
	# if 'masterwindow' not in cfg.screenDict:
	# 	print(cfg.screenDict)
	# 	Master = QtWidgets.QMainWindow()
	# 	cfg.screenDict['masterwindow'] = Master
	# print ('In peggers ... screenDict:= ', cfg.screenDict)
	# # make resizeable
	# # cfg.screenDict['root'].rowconfigure(0, weight=1)
	# # cfg.screenDict['root'].columnconfigure(0, weight=1)
	# # cfg.screenDict['root'].resizable(True, True)
	#
	#
	#
	# ui = Ui_Master()		# this is the whole of the UI
	# ui.setupUi(Master,'Qt Test UI')		# assign all ui elmeents
	# Master.show()			# maket itvisible.
	#
	# # cfg.appTitle = 'From the club table in dbms'
	# # app = Cribbage(cfg.screenDict['root'],cfg.appTitle)

	# this will run cfg setup
	cribbageApp = Cribbage()

	app = qtw.QApplication(sys.argv)
	window = MasterScreen()
	window.show()

	# if 'window' not in cfg.screenDict:
	# 	print('Empty screenDict')
	# 	cfg.screenDict['window'] = window
	# 	print('screenDict[window]: ')
	# 	print(cfg.screenDict['window'])

	print('Window should show...')


	sys.exit(app.exec())


    

