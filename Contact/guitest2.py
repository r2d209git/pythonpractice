import sys
from PyQt5.QtWidgets import *
from win32com import client as win32


""" Python GUI modules
tkInter : 내장형
PyQt
wxPython """

#cl = win32.Dispatch("Excel.Application")
#cl.Visible = True

app = QApplication(sys.argv)
label = QLabel("Hello PyQt")
label.show()
button = QPushButton("Push")
button.show()
app.exec_()

print("%i: %s" % (1, "bae"))

print("%s, %s\n" % ("key", "value"))
