# Notes on GUI techniques for PySide6 Qt 

## Using Qt Properties

There are several examples out there that do not work with PySide6
Most notably the Property(read, write, notify) syntax.

**Must use the @Property(type) decorator from PySide6.QtCore**

---
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
---

**Things to observe**
1. The two signals must be defined inside a QObject derived class.
2. You have to define  your own signals and name them.
3. Must use from PySide6.QtCore import QObject, Property, Signal
4. The @Property(type) decorator passes on the value of the property to the signals
5. @myValue.setter refers to the name of the def defined under @Property(type)
6. The property getter and setter can perform any desired test before returning or setting the property, as needed.

**How to use QtProperties**
1. Import StringVar, IntVar, DoubleVar
2. Create local named instances of the required kind of property Var
3. Connect the <type>ValueRead|Changed signal to target function

Using these properties and their associated signals allows emulation of the tkinter control variables when they are attached to Gui widgets.

## Emulating tkinter control variables

This is why @Properties and signals were investigated in the first place.

tkinter control variables are the 'magic' where tkinter gui widgets interact with python variables.
When the gui widget changes value the python variable is updated and when the python variable is change the gui widget is updated.
If it a bidirectional synchronous relationship.

1. self.EntryField = QtWidgets.QLineEdit(parent=self.centralwidget)
2. self.entryInput = StringVar()
3. def returnPressed(self):
4.     self.entryInput.myValue = Self.EntryField.(text)
5. self.EntryField.returnPressed.connect(self.returnPressed)
6. self.entryInput.strValueChanged.connect(self.my_slot)
7. self.entryInput.strValueChanged.connect(self.EntryField.setText)
8. def my_slot(self, data):
9.    print ('Slot got ' + data)

The above code snippet emulates tkinter contol variables and chains events together
1. Define the entry field where changes will be made
2. Create a StringVar with the strValueChanged and strValueRead signals
3. Define a function to be executed when return is pressed on EntryField
4. Set the value of the entryInput property variable
5. Connect the EntryField pre-defined signal to the returnPressed function
6. Connect the strValueChanged signal for the entryInput property to the my_slot function
7. Connect the strValueChanged signal for the entryInput property to the EntryField.setText() function
8. Define the my_slot receiver slot from (6) above
9. Show the data that was received by my_slot

What this shows:
1. The returnPressed signal changes the entryInput property, just like a tkinter control variable
2. In turn the strValueChanged signal can be connected to more than one slot
3. The data from the strValueChanged signal can be retrieved by the slots
4. In item (7) the signal is wrapped back to the originator but this causes no loop because
    the original signal was issued from the returnPressed signal of the EntryInput widget
5. Setting the text does not cause the returnPressed signal to be reissued.

## Capturing Keystroke Events

Again their examples showing subclassing a widget to override the KeyPress event.
This flat out does not work as shown in the examples.

One must create a filter object and install it on the widget(s) to be monitored.
This example uses a QListWidget example.

1. Start with the needed imports
2. -- from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QListWidget--
3. Create a filter object class derived from QObject
4. --class FunctionKeyFilter(QObject):
    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            # print(event.key())
            if event.key() == QtCore.Qt.Key_F1:
                print("F1 pressed")
            return False
        else:
            return True--
5. Return False means stop the signal here; return True means pass it on up the hierarchy
6. Create an instance of the class: self.fObj = FunctionKeyFilter()
7. Now install this filter object using self.target.installEventFilter(self.fObj)
8. If the target is a single widget instance, only that widget's events are monitored
9. If installed on a more base class, all it's subclasses' events are filtered
10. If installed on a base class will be necessary to test widget.type() for relevance


## tkinter events vs. PyQt Signals

In general one has to bind an event to any tkinter widget to capture gui events.

PyQt has a number of standard signals (aka events) for the different widgets.

The best example is DoubleClick on a list box item. In PyQt this is a standard signal.
In tkinter one has to bind a doubleclick event definition to the tkinter list box widget.

Where there is no standard PyQt event you have to go create and bind a filter object to the widget and capture the desired QEvent
This is similar to the tkinter event bind protocol.

In all cases, the tkinter event and the PyQt filter must be connected to a handler for the event.

Where existing tkinter code uses a lot of F-keys as shortcuts, these must be bound using PyQt filter objects.
The end result is equivalent functionality with F-keys acting as shortcut keys.

## QtCreator/QtDesigner Notes

When QtCreator creates the .py file using Pyuic6 it uses PyQt6 imports; these must all be changed to PySide6

QtCreator always uses the class UI_Master(object) class construct and creates the main window inside the def setUpUI function

You should not add code directly to the created .py file; if the ui is recreated all added code will be wiped out.

Instead, extract a copy of the desired UI definitions and add application to this copy, 
As needed, rebuild the ui .py file and re-extract it into the copy with the application code.

Where UI updates are made for signals and emulated tkinter control variables always set these off with clear comment boxes

