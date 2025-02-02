# ctrlVariables.py
#
# Update  with bool 1/25/2025 mwycombe
#
# To provide equivalnt of tkinter UI control variable
#
# QObject properties only support direct assegnment and reading of the Property
#
# Each ctrlVariable has slots for allowing connection from UI fields and signals to
# notify of changes.
#
# In addition, for interfacing with UI fields, ctrlVariables support receiving strings
#

from PySide6.QtCore import QObject, Property, Signal, Slot, Qt
from PySide6 import QtCore as qtc

class StringVar(QObject):
    ''' Provides a Property function for PyQt/PySide6 that uses signals
        to emulate tkinter StringVar()'''
    strValueChanged = Signal(str)    # must be defined inside a QObject class type
    strValueRead    = Signal(str)    # optional signal on read

    def __init__(self):
        super().__init__()
        self._my_value = ''

    # need separate slot as cannot apply @Slot to setter
    @Slot(str)
    def acceptStr(self,value):
        self.myValue = value

    @Property(str)
    def myValue(self):
        self.strValueRead.emit(self._my_value)
        return self._my_value

    @myValue.setter
    def myValue(self,value):
        print('StrVar received: ', value)
        if value != self._my_value:
            self._my_value = value
            print ('strValueChanged: ', value)
            self.strValueChanged.emit(value)

class IntVar(QObject):
    ''' Provides a Property function for PyQt/PySide6 that uses signals
        to emulate tkinter IntVar()'''
    intValueChanged = Signal(int)
    intValueAsStringChanged = Signal(str)   # must be defined inside a QObject class type
    intValueRead   = Signal(int)    # optional signal on read

    def __init__(self):
        super().__init__()
        self._my_value = 0

    @Slot(str)
    def acceptIntAsStr(self,value):
        if value == '' or value == None or not value.isnumeric():
            value = 0
        self.myValue = int(value)

    @Slot(int)
    def acceptInt(self,value):
        self.myValue = value

    @Property(int)
    def myValue(self):
        self.intValueRead.emit(self._my_value)
        return self._my_value

    @myValue.setter
    def myValue(self,value):
        if value != self._my_value:
            self._my_value = value
            self.intValueChanged.emit(value)
            self.intValueAsStringChanged.emit(str(value))

class DoubleVar(QObject):
    ''' Provides a Property function for PyQt/PySide6 that uses signals
        to emulate tkinter DoubleVar()'''
    dblValueChanged = Signal(float)  # must be defined inside a QObject class type
    dblValueRead = Signal(float)
    dblValueAsStrChanged = Signal(str)# optional signal on read

    def __init__(self):
        super().__init__()
        self._my_value = 0

    @Slot(str)
    def acceptDblAsStr(self,value):
        if value == '' or value == None:
            value = 0.0
        self.myValue = float(value)

    @Property(float)
    def myValue(self):
        self.dblValueRead.emit(self._my_value)
        return self._my_value

    @myValue.setter
    def myValue(self, value):
        if value != self._my_value:
            self._my_value = value
            self.dblValueChanged.emit(value)
            self.dblValueAsStrChanged.emit(str(value))

class BoolVar(QObject):
    ''' Provides a for holding state of checkboxes and
        radio buttons among other things'''
    boolValueChanged = Signal(bool)
    boolValueRead    = Signal(bool)     # optional signal on read
    boolValueAsIntChanged = Signal(int)  # for those that prefer 1/0

    def __init__(self):
        super().__init__()
        self._my_value = False

    @Slot(int)
    def acceptBoolAsInt(self,value):
        if value == 0 or value == None:
            self.myValue = False
        else:
            self.myValue = True

    @Slot(bool)
    def acceptBool(self, value):
        self.myValue = value

    @Slot(Qt.CheckState)
    def acceptCheckState(self, value):
        print('Bool check state: ', value)
        if value == Qt.Checked:
            print('Set as True')
            self.myValue = True
        else:
            self.myValue = False

    @Property(bool)
    def myValue(self):
        self.boolValueRead.emit(self._my_value)
        if self._my_value == True:
            self.boolValueAsIntChanged.emit(1)
        else:
            self.boolValueAsIntChanged.emit(0)
        return self._my_value
    @myValue.setter
    def myValue(self, value):
        print ('value, _my_value ', value, self._my_value)
        if value != self._my_value:
            print('set _my_value to: ', value)
            self._my_value = value
            self.boolValueChanged.emit(value)
            if value == True:
                self.boolValueAsIntChanged.emit(1)
            else:
                self.boolValueAsIntChanged.emit(0)
