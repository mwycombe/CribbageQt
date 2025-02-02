# Cribbage V2
## Inactive MembersPlayers
1. Change all references to players to show and allow lists to include all or just active players
2. Allow activation/deactivation of players from players list windown without F2
3. Provide option to include/exclude inactive players from reports.

## Window sizing
1. Fix frames and windows so they resize with windows.

## Results
1. Make active results line have bolder player name
2. Forget entry order - always sort input by seat number

## Reports 
1. Include or exclude inactive players
2. Provide total lines for tourney, cash report, alpha reports
3. Ensure a tourney is selected before running reports
4. Default to latest tourney selected

## Screens and lists
1. Ensure an entry is selected from the list when arriving at a screen
2. Implement alpha search and wrap for player lists


## Active players
1. Change activity status by going to the Players Tab
2. For Results entry, go to Players Tab for now to make players active as needed

## Default focus on first entry
1,  Does not appear to want to work...

## ScreenDict contents under Qt
['masterwindow']        MasterWindow for Qt application\
['uimaster']            Ui_Master object\
['toppanel']            TopContainer where everything resides\
['notebook']            QtTabWdiget used to hold all tab screens\
['ptab']                playersTab screen\
['ttab']                tourneysTab screen\
['rsltstab']            resultsTab screen\
['rptstab']             reportsTab screen\
['activitypanel']       blank activity panel\
['playersactivitytab']  player activity panel
['resultsactivitytab']  results activity panel\
['reportsactivitytab']  reports activity panel\
['tourneysactivitytab'] tourneys activity panel\
['sessionpanel']        session header panel\
['clubpanel]']          club header panel\
['activitystack']       where all the action  panels are displayed\

## stackedActivityDict
Dictionary contains '<name>':activitystack index xref into\
the activitystack QStackWidget where all of the activity widgets have been pushed\



## Setting up the UI with Qt vs. tkinter

Current structure defers setting up the players, tourneys, reports, and results tabs to the instantiation of the tab object. 
This makes it easy to connect events to the fields in the control variables.

For Qt, the QtCreator delivers a single file with all of the fields and initializations defined. The one area that really
needs to be in the invidual tab objects are the activity panel entries which are totally dependent on which tab is active.

The challenge will be to connect the signals and control properties when in the various tab objects to the centrally defined tab ui fields.

The main activity panel is set up with blank content and each tab activates their own content when the tab is switched to.

## Learnings
1. QListWidget will not respond to mouseevents if it's empty - specifically DoubleClick events.
2. QListItems do have an inbuilt signal, including DoubleClick that they will emit.
3. Always remove the () from the target slot of a signal. Only the name is required. () tries to call it.