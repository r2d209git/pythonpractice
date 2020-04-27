from pandas import Series, DataFrame
import pandas as pd
import sqlite3
import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.pushbtn = QPushButton("DB Open")
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("DB File Open Dialog")

        self.pushbtn.clicked.connect(self.db_open)

        layout = QVBoxLayout()
        layout.addWidget(self.pushbtn)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def db_open(self):
        fname = QFileDialog.getOpenFileName(self)
        print(type(fname))
        print(fname)
        self.label.setText(fname[0])
        db = DBRead(fname[0])
        db.readDB()


class DBRead:
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def readDB(self):
        con = sqlite3.connect(self.dbfile)
        df = pd.read_sql("SELECT * from test", con, index_col='index')
        print(df)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWindow()
    mywin.show()
    app.exec()
