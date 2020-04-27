import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("File Dialog Test")

        self.pushbtn = QPushButton("File Open")
        self.pushbtn.clicked.connect(self.file_open)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushbtn)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def file_open(self):
        fname = QFileDialog.getOpenFileName(self)
        print(type(fname))
        print(fname)
        self.label.setText(fname[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWindow()
    mywin.show()
    app.exec()
