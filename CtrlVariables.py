
from PySide6.QtCore import QObject, Property, Signal

class StringVar(QObject):
    ''' Provides a Property function for PyQt/PySide6 that uses signals
        to emulate tkinter StringVar()'''
    strValueChanged = Signal(str)    # must be defined inside a QObject class type
    strValueRead    = Signal(str)    # optional signal on read

    def __init__(self):
        super().__init__()
        self._my_value = ''

    @Property(str)
    def myValue(self):
        self.strValueRead(_my_value)
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
    intValueChange = Signal(int)    # must be defined inside a QObject class type
    intValueRead   = Signal(int)    # optional signal on read

    def __init__(self):
        super().__init__()
        self._my_value = 0

    @Property(int)
    def myValue(self):
        self.intValueRead.emit(self._my_value)
        return self._my_value

    @myValue.setter
    def myValue(self,value):
        if value != self._my_value:
            self._my_value = value
            self.intValueChanged.emit(value)


class DoubleVar(QObject):
    ''' Provides a Property function for PyQt/PySide6 that uses signals
        to emulate tkinter DoubleVar()'''
    dblValueChanged = Signal(int)  # must be defined inside a QObject class type
    dblValueRead = Signal(int)  # optional signal on read

    def __init__(self):
        super().__init__()
        self._my_value = 0

    @Property(float)
    def myValue(self):
        self.dblValueRead.emit(self._my_value)
        return self._my_value

    @myValue.setter
    def myValue(self, value):
        if value != self._my_value:
            self._my_value = value
            self.dblValueChanged.emit(value)
