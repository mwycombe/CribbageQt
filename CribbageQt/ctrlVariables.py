
from PySide6.QtCore import QObject, Property, Signal, Slot
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
        print('StrVar received: ' + value)
        if value != self._my_value:
            self._my_value = value
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
        if value == '' or value == None:
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