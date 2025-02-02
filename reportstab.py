# reportsstab.py
# 7/21/2020 update to cribbageconfig and cribbagereport
#
# Nov 2024 replace tkinter with PySide6
#
#####################################################################
#
#   Creates tab screen for requesting reports
#   Will self-register in notebook found in screenDict of cfg
#
#####################################################################
# TODO: From myPyfiles, move averagereport, battingavgreport, cashreport, nationalratingreport
# TODO: From myPyfiles, move qtrdropreport, qtrfullreport, skunkreport, tourneyreport
# TODO: Don't report players that are inactive - soft deleted.
# TODO: Indicate Done, ask for continue, and reset selections
# TODO: Must check for a valid tourney being selected - otherwise fails silently with tuple index out of range
# TODO: Vertical scroll bar not working!
# TODO: Need to be able to edit bad tourney week/date
# TODO: Make sure report is selected before running reports
# TODO: Add column totals to tourney reports
# TODO: Add bracket construction and MRP assignements
# TODO: improve input screen for results
# TODO: Improve alphs search for names
# TODO: Allow for active/inactive players in results & reports
# TODO: UPGRADE TO 2024 AFTER THE SEASON ENDS




# System imports
import operator
# import tkinter as tk
# from tkinter import messagebox as mbx

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, Qt
from PySide6 import QtCore, QtWidgets

from ctrlVariables import BoolVar, IntVar, StringVar
from ctrlVariables import StringVar, IntVar, DoubleVar

from reportsActivityPanel import Ui_reportsactivitypanel
from datetime import date

# Personal imports
import cribbageconfig as cfg
import cribbagereport as rpt
import alphareport
import battingavgreport
import cashreport
import individualstatsReport
import natallreport
import qtrdropreport
import qtrfullreport
import skunkreport
import tourneyreport
# from masterscreen import MasterScreen

class ReportsTab (qtw.QWidget, Ui_reportsactivitypanel):
    # screen class is always a frame

    #************************************************************   
    #   
    #   sets up tab for requesting reports & regiester with notebook frame

    def __init__ (self, parent=None):
        super().__init__( parent)
        if cfg.debug:
            print('starting reportstab')
        self.setupUi(self)

        # all of the fields should already be in the widget inside the QTabWidget

        self.installReportsActivity()

        cfg.screenDict['rtab'] = self

        #provide shortcut for addressing UI definitions in masterscreen
        self.main = cfg.screenDict['masterwindow']

        # PyQt control variables for report selecton
        self.allReportsVar = BoolVar()
        self.alphaVar = BoolVar()
        self.battingAvgVar = BoolVar()
        self.cashVar = BoolVar()
        self.individStatsVar = BoolVar()
        self.natallVar = BoolVar()
        self.qtrDropVar = BoolVar()
        self.qtrFullVar = BoolVar()
        self.skunksVar = BoolVar()
        self.tourneyVar = BoolVar()

        # connect UI entities to ctrlvariables
        self.main.ckb_alpha.checkStateChanged.connect(self.alphaVar.acceptCheckState)
        self.main.ckb_battingAverage.checkStateChanged.connect(self.battingAvgVar.acceptCheckState)
        self.main.ckb_cash.checkStateChanged.connect(self.cashVar.acceptCheckState)
        self.main.ckb_individStats.checkStateChanged.connect(self.individStatsVar.acceptCheckState)
        self.main.ckb_nationalAvges.checkStateChanged.connect(self.natallVar.acceptCheckState)
        self.main.ckb_qtrDrop.checkStateChanged.connect(self.qtrDropVar.acceptCheckState)
        self.main.ckb_qtrFull.checkStateChanged.connect(self.qtrFullVar.acceptCheckState)
        self.main.ckb_skunk.checkStateChanged.connect(self.skunksVar.acceptCheckState)
        self.main.ckb_tourney.checkStateChanged.connect(self.tourneyVar.acceptCheckState)

        # connect ctrlvariables back to UI entities
        self.allReportsVar.boolValueChanged.connect(self.main.ckb_allReports.setChecked)
        self.alphaVar.boolValueChanged.connect(self.main.ckb_alpha.setChecked)
        self.battingAvgVar.boolValueChanged.connect(self.main.ckb_battingAverage.setChecked)
        self.cashVar.boolValueChanged.connect(self.main.ckb_cash.setChecked)
        self.individStatsVar.boolValueChanged.connect(self.main.ckb_individStats.setChecked)
        self.natallVar.boolValueChanged.connect(self.main.ckb_nationalAvges.setChecked)
        self.qtrDropVar.boolValueChanged.connect(self.main.ckb_qtrDrop.setChecked)
        self.qtrFullVar.boolValueChanged.connect(self.main.ckb_qtrFull.setChecked)
        self.skunksVar.boolValueChanged.connect(self.main.ckb_skunk.setChecked)
        self.tourneyVar.boolValueChanged.connect(self.main.ckb_tourney.setChecked)

        # select all reports is special
        self.main.ckb_allReports.checkStateChanged.connect(self.allReportsVar.acceptCheckState)
        # self.main.ckb_allReports.checkStateChanged.connect(self.allReportsChange)
        self.allReportsVar.boolValueChanged.connect(self.handleAllReportsState)

        # control variables for report selection
        # self.allReportsVar = tk.IntVar()
        # self.alphaVar = tk.IntVar()
        # self.battingAvgVar = tk.IntVar()
        # self.cashVar = tk.IntVar()
        # self.individStatsVar = tk.IntVar()
        # self.natallVar = tk.IntVar()
        # self.qtrDropVar = tk.IntVar()
        # self.qtrFullVar = tk.IntVar()
        # self.skunksVar = tk.IntVar()
        # self.tourneyVar = tk.IntVar()

        # rpt.reportStack = {}
        # rpt.reportStack['alphareport'] = (self.alphaVar.myValue, alphareport.AlphaReport)
        # rpt.reportStack['battingavgreport'] = (self.battingAvgVar.myValue, battingavgreport.BattingAvgReport)
        # rpt.reportStack['cashreport'] = (self.cashVar.myValue, cashreport.CashReport)
        # rpt.reportStack['individstatsreport'] = (self.individStatsVar.myValue, individualstatsReport.IndividualStatsReport)
        # rpt.reportStack['natallreport'] = (self.natallVar.myValue, natallreport.NatAllReport)
        # rpt.reportStack['qtrdropreport'] = (self.qtrDropVar.myValue, qtrdropreport.QtrDropReport)
        # rpt.reportStack['qtrfullreport'] = (self.qtrFullVar.myValue, qtrfullreport.QtrFullReport)
        # rpt.reportStack['skunkreport'] = (self.skunksVar.myValue, skunkreport.SkunkReport)
        # rpt.reportStack['tourneyreport'] = (self.tourneyVar.myValue, tourneyreport.TourneyReport)


        # build stack of selections
        rpt.reportStack = {}
        rpt.reportStack['alphareport'] = (self.alphaVar, alphareport.AlphaReport)
        rpt.reportStack['battingavgreport'] = (self.battingAvgVar, battingavgreport.BattingAvgReport)
        rpt.reportStack['cashreport'] = (self.cashVar, cashreport.CashReport)
        rpt.reportStack['individstatsreport'] = (self.individStatsVar, individualstatsReport.IndividualStatsReport)
        rpt.reportStack['natallreport'] = (self.natallVar, natallreport.NatAllReport)
        rpt.reportStack['qtrdropreport'] = (self.qtrDropVar, qtrdropreport.QtrDropReport)
        rpt.reportStack['qtrfullreport'] = (self.qtrFullVar, qtrfullreport.QtrFullReport)
        rpt.reportStack['skunkreport'] = (self.skunksVar, skunkreport.SkunkReport)
        rpt.reportStack['tourneyreport'] = (self.tourneyVar, tourneyreport.TourneyReport)

        # capture run reports button pressed
        self.main.pb_runReportsButton.clicked.connect(self.reportHandler)
        self.allReportsVar.boolValueChanged.connect(self.handleAllReportsState)


        # build out tab and register with notebook
        # self.config(padx = '5', pady = '5')
        # tabTarget.add(self,text='Reports')
        # cfg.screenDict['rtab'] = self
        # self.reportsPanel = tk.Frame(self,
        #                               borderwidth = '1',
        #                               height = '8c',
        #                               width = '10c',
        #                               padx = '10', pady = '10',
        #                               relief = 'sunken')
        # self.trnysPanel = tk.LabelFrame(self.reportsPanel,
        #                                  text = 'Tourneys',
        #                                  height = '8c',
        #                                  width = '5c',
        #                                  padx = '5', pady = '5',
        #                                  relief = 'sunken')
        # # self.instrPanel = tk.Frame(self.trnysPanel,
        # #                             relief = 'sunken',
        # #                             borderwidth = 3)
        # self.listPanel = tk.Frame(self.trnysPanel,
        #                            relief = 'sunken',
        #                            borderwidth = 0)
        # # self.instrPanel.grid(row=0, column=0)
        # self.listPanel.grid(row=0, column=0)
        # self.rptsPanel = tk.LabelFrame(self.reportsPanel,
        #                                 text = 'Reports',
        #                                 height = '8c',
        #                                 width = '5c',
        #                                 padx = '5', pady = '5',
        #                                 borderwidth = 3,
        #                                 relief = 'sunken')
        # self.selectPanel = tk.Frame(self.rptsPanel,
        #                              relief = 'sunken',
        #                              borderwidth = 0)
        # self.runPanel = tk.Frame(self.rptsPanel,
        #                           relief = 'sunken',
        #                           borderwidth = 3)
        # self.selectPanel.grid(row=0, column=0)
        # self.runPanel.grid(row=1, column=0)
        # self.reportsPanel.grid(row = 0, column = 0)
        # self.trnysPanel.grid(row = 0, column = 0, sticky = 'n')
        # self.rptsPanel.grid(row = 0, column = 1, sticky = 'n')
        #
        # self.runButton = tk.Button(self.runPanel,
        #                             text='Run Reports')
        # self.runButton.bind('<Button-1>', self.reportHandler)
        # self.runButton.grid(column=0)
        #
        # # set up for reports all finished.
        # self.finishedPanel = tk.Frame(self.reportsPanel,
        #                    relief = 'sunken',
        #                    borderwidth = 3)
        # self.finishedPanel.grid(row=0, column=3, sticky = 'n')
        # self.finishedLabel = tk.Label(self.finishedPanel,
        #                               text = 'All Reports Have Been Run')
        # self.finishedLabel.grid(row=0, column=0, sticky = 'n')
        # self.hideWidget(self.finishedPanel)   # hide until needed
        # self.tourneysWithResults = tk.Listbox(self.listPanel,
        #                                       width = 15,
        #                                       height = 18)
        # self.tourneysWithResults.grid(row=0, column=0,sticky='n')
        # self.vsb = tk.Scrollbar(self.listPanel)
        # self.vsb.grid(row=0, column=1, sticky='ns')
        # self.tourneysWithResults.config(yscrollcommand = self.vsb.set)
        # self.vsb.config(command = self.tourneysWithResults.yview)
        # self.tourneysWithResults.select_set(0)
        # self.tourneysWithResults.activate(0)
        # self.tourneysWithResults.focus_force()
        # # build list of selectable reports
        # self.allChoice = tk.Checkbutton(self.selectPanel,
        #                                   text = 'AllReports',
        #                                   onvalue = 1, offvalue = 0,
        #                                   anchor = 'w',
        #                                   height = 2,
        #                                   width = 20,
        #                                   command = self.selectAllReports,
        #                                   variable = self.allReportsVar
        #                                   )
        # self.alphaChoice = tk.Checkbutton(self.selectPanel,
        #                                     text = 'Alpha Report',
        #                                     onvalue = 1, offvalue = 0,
        #                                     anchor = 'w',
        #                                     height = 1,
        #                                     width = 20,
        #                                     variable = self.alphaVar
        #                                     )
        # self.battingAvgChoice = tk.Checkbutton(self.selectPanel,
        #                                       text = 'Batting Average Report',
        #                                       onvalue = 1, offvalue = 0,
        #                                       anchor = 'w',
        #                                       height = 1,
        #                                       width = 20,
        #                                       variable = self.battingAvgVar
        #                                       )
        # self.cashChoice = tk.Checkbutton(self.selectPanel,
        #                                       text = 'Cash Report',
        #                                       onvalue = 1, offvalue = 0,
        #                                       anchor = 'w',
        #                                       height = 1,
        #                                       width = 20,
        #                                       variable = self.cashVar
        #                                       )
        # self.individStatsChoice = tk.Checkbutton(self.selectPanel,
        #                                       text = 'Individ. Stats Report',
        #                                       onvalue = 1, offvalue = 0,
        #                                       anchor = 'w',
        #                                       height = 1,
        #                                       width = 20,
        #                                       variable = self.individStatsVar
        #                                       )
        # self.natAllChoice = tk.Checkbutton(self.selectPanel,
        #                                       text = 'National Avges Report',
        #                                       onvalue = 1, offvalue = 0,
        #                                       anchor = 'w',
        #                                       height = 1,
        #                                       width = 20,
        #                                       variable = self.natallVar
        #                                       )
        # self.qtrDropChoice = tk.Checkbutton(self.selectPanel,
        #                                       text = 'Qtr Drop Report',
        #                                       onvalue = 1, offvalue = 0,
        #                                       anchor = 'w',
        #                                       height = 1,
        #                                       width = 20,
        #                                       variable = self.qtrDropVar
        #                                       )
        # self.qtrFullChoice = tk.Checkbutton(self.selectPanel,
        #                                       text = 'Qtr Full Report',
        #                                       onvalue = 1, offvalue = 0,
        #                                       anchor = 'w',
        #                                       height = 1,
        #                                       width = 20,
        #                                       variable = self.qtrFullVar
        #                                       )
        # self.skunkChoice = tk.Checkbutton(self.selectPanel,
        #                                       text = 'Skunk Report',
        #                                       onvalue = 1, offvalue = 0,
        #                                       anchor = 'w',
        #                                       height = 1,
        #                                       width = 20,
        #                                       variable = self.skunksVar
        #                                       )
        # self.tourneyChoice = tk.Checkbutton(self.selectPanel,
        #                                       text = 'Tourney Report',
        #                                       onvalue = 1, offvalue = 0,
        #                                       anchor = 'w',
        #                                       height = 1,
        #                                       width = 20,
        #                                       variable = self.tourneyVar
        #                                       )
        #
        # self.rptsPanel.columnconfigure(0, weight=1)
        # self.allChoice.grid(row = 0, column = 0, sticky = 'w')
        # self.alphaChoice.grid(column = 0, sticky='w')
        # self.battingAvgChoice.grid(column = 0, sticky='w')
        # self.cashChoice.grid(column = 0, sticky='w')
        # self.individStatsChoice.grid(column = 0, sticky='w')
        # self.natAllChoice.grid(column = 0, sticky='w')
        # self.qtrDropChoice.grid(column = 0, sticky='w')
        # self.qtrFullChoice.grid(column = 0, sticky='w')
        # self.skunkChoice.grid(column = 0, sticky='w')
        # self.tourneyChoice.grid(column = 0, sticky='w')
        # self.buildActivityPanel()


    @Slot(Qt.CheckState)
    def allReportsChange(self,value):
        print ('Got all reports signal')
        print (value)
        # try to set boolVar

    @Slot(bool)
    def handleAllReportsState(self,value):
        if value:
            self.selectAllReports()
        else:
            self.resetSelections()

    def buildActivityPanel(self):
        # make the appropriate stacked widget current
        self.widgetIndex = cfg.stackedActivityDict['reportsactivitypanel']
        cfg.screenDict['activitystack'].setCurrentIndex(self.widgetIndex)

        # MasterScreen.wipeActivityPanel()
        # self.ap = cfg.screenDict['activity']
        # print ('self.ap in reportstab: ', self.ap)
        # self.instr1 = tk.Label(self.ap,
        #                               text='First Pick a Tourney')
        # self.instr2 = tk.Label(self.ap,
        #                         text='Then One or More Reports')
        # self.instr3 = tk.Label(self.ap,
        #                         text='And Press Run Reports When Ready')
        # self.instr1.grid(row=0, column=0, sticky='w')
        # self.instr2.grid(row=1, column=0, sticky='w')
        # self.instr3.grid(row=2, column=0, sticky='w')

    def tabChange(self):
        # no longer event driven
        # tabchanged signal caught in MasterScreen
        # show the menu of choices for reports
        # reports will be run from the database
        # which has been updated with the latest tournament
        self.buildActivityPanel()
        print ('Tourney List', cfg.at.getTourneysWithResults(cfg.season))
        self.main.lw_listOfReportTourneys.clear()
        self.trnyList = cfg.at.getTourneysWithResults(cfg.season)
        # print('rpt', dir(rpt))
        # self.tourneysWithResults.delete(0, tk.END)
        for trny in self.trnyList:
            print(trny)
            tDate = date.fromisoformat(trny[2]).strftime('%m/%d/%Y')
            self.main.lw_listOfReportTourneys.addItem(' ' + str(trny[1]) + '.  ' + tDate)
            # self.tourneysWithResults.insert(tk.END,'  ' + str(trny[1]) + '.  ' + tDate)
        # set focus to first entry
        self.main.lw_listOfReportTourneys.setCurrentRow(0)
        self.main.lw_listOfReportTourneys.setFocus()

    def selectAllReports(self):
        # these gets must be replaced by UI signals setting the ctrlVariables
        # self.alphaVar.set(self.allReportsVar.get())
        # self.battingAvgVar.set(self.allReportsVar.get())
        # self.cashVar.set(self.allReportsVar.get())
        # # skip individual stats
        # # self.individStatsVar.set(self.allReportsVar.get())
        # self.natallVar.set(self.allReportsVar.get())
        # self.qtrDropVar.set(self.allReportsVar.get())
        # # skip full quarter report
        # # self.qtrFullVar.set(self.allReportsVar.get())
        # self.skunksVar.set(self.allReportsVar.get())
        # self.tourneyVar.set(self.allReportsVar.get())
        self.alphaVar.myValue = True
        self.battingAvgVar.myValue = True
        self.cashVar.myValue = True
        self.natallVar.myValue = True
        # check for which aqr it is
        self.qtrDropVar.myValue = True
        # self.qtrFullVar.myValue.myValue == True    # not by default
        self.skunksVar.myValue = True
        self.tourneyVar.myValue = True

    def runReports(self, tnumber, tdate):
        # Was unable to resolve rpt. variables in this method called from the tkinter event handler
        # Calling this other method allowed all rpt. variables to be resolved.
        # This was the original attempt to include default parameters into the event handler
        self.reportRunner()     #NB. no params passed on!

    @Slot()
    def reportHandler(self):
        print ('Initial reportHandler')
        # reinitialize after every report selection cycle

        # print ('dir(rpt)', dir(rpt))
        # get the line selected by the report requestor
        # rpt.tourneyNumber =
        # neither rpt.tourneyNumber nor rpt.tourneyDate have yet been set
        return self.runReports( tnumber=rpt.tourneyNumber, tdate=rpt.tourneyDate)

    def reportRunner(self):
        print ('reportrunner')
        self.trnyListSelection = self.main.lw_listOfReportTourneys.currentRow()
        # self.trnyListSelection = self.tourneysWithResults.curselection()[0]
        print ('trnyListSelection: ', self.trnyListSelection)
        rpt.reportSeason = cfg.season
        rpt.tourneyRecordId = self.trnyList[self.trnyListSelection][0]
        rpt.tourneyNumber = self.trnyList[self.trnyListSelection][1]
        rpt.tourneyDate = self.trnyList[self.trnyListSelection][2]
        print ('rpt. tourneyRecordId, tourneyNumber, tourneyDate: ', rpt.tourneyRecordId, rpt.tourneyNumber, rpt.tourneyDate)
        # print ('Dir?', dir(rpt))
        curSel = self.main.lw_listOfReportTourneys.currentRow()
        # curSel = self.tourneysWithResults.curselection()
        # use lw_listOfReportTourneys
        print('cursel:', curSel)
        # print('line:', self.tourneysWithResults.get(curSel[0]))
        print ('line: ', self.main.lw_listOfReportTourneys.item(curSel))
        parsedLine = self.main.lw_listOfReportTourneys.item(curSel).text().strip(' ').split(' ')
        print('Parsed line:', parsedLine)
        # rpt.tourneyNumber = int(parsedLine[0].split('.')[0])
        # rpt.reportSeason = cfg.season
        # rpt.tourneyRecordId = cfg.tourneyRecordId
        # get tourney recod for the selected tourney
        # TODO: this has to be by season and by tourney number]
        print ('rptSeason: ', rpt.reportSeason)
        rpt.tourneyRecord = cfg.at.getTourneyRecordById(rpt.tourneyRecordId)
        print('rpt.tourneyNumber:', rpt.tourneyNumber)
        rpt.tourneyDate = parsedLine[2]
        print ("rpt vars: ", rpt.tourneyNumber, rpt.tourneyDate)
        print ('rpt stack', rpt.reportStack)
        for (k,v) in rpt.reportStack.items():
            print ('Stack entry', k, v, type(k), type(v))

        # step through report stack
        for (k, v) in rpt.reportStack.items():
            # k is reportname, v is (IntVar, report Class to run)
            print ('value: ',v)
            # if v[0].get() == 1:
            # dictionary holds boolVar properties
            print ('k, v[0]: ', k, v[0].myValue)
            if v[0].myValue == True:

                # instantiate and run report class
                print ('Run: ', k)
                runReport = v[1]
                runReport()
                # rpt = v[1]
                # print('Run ', v[1])
        # after all reports have been run, show msgbox and clean up.
        self.reportsFinished()
    def reportsFinished(self):
        # pass
        # self.showWidget(self.finishedPanel)
        # self.showWidget(self.finishedLabel)
        # mbx.showinfo('Reports All Run', 'Press Enter to Continue')
        # self.hideWidget(self.finishedPanel)
        # self.hideWidget(self.finishedLabel)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('Reports all done')
        msgBox.setWindowTitle('Reports Finished')
        msgBox.setStandardButtons(QMessageBox.Ok )

        result = msgBox.exec()
        self.resetSelections()

    def resetSelections(self):
        # pass
        self.allReportsVar.myValue = False
        self.alphaVar.myValue = False
        self.battingAvgVar.myValue = False
        self.cashVar.myValue = False
        self.individStatsVar.myValue = False
        self.natallVar.myValue = False
        self.qtrDropVar.myValue = False
        self.qtrFullVar.myValue = False
        self.skunksVar.myValue = False
        self.tourneyVar.myValue = False
        # self.allReportsVar.set(0)
        # self.battingAvgVar.set(0)
        # self.cashVar.set(0)
        # self.individStatsVar.set(0)
        # self.natallVar.set(0)
        # self.qtrDropVar.set(0)
        # self.qtrFullVar.set(0)
        # self.skunksVar.set(0)
        # self.tourneyVar.set(0)

    def hideWidget (self,w):
        w.grid_remove()
    def showWidget (self,w):
        w.grid()
    def installReportsActivity(self):
        print ('install reports activity panel')

        # have to add this into the master activity stacked widget
        self.widx = cfg.screenDict['activitystack'].addWidget(self)
        # remember this index
        cfg.stackedActivityDict['reportsactivitypanel'] = self.widx