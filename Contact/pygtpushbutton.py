from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        button = QPushButton("닫기", self)
        button.move(20, 20)
        button.clicked.connect(self.exit_window)

    def exit_window(self):
        print("Exit Window")
        QCoreApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    app.exec()