import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def initWindow(self):
        self.setWindowTitle("Bae First Window")
        self.setGeometry(300, 300, 300, 400)

        pushBtn = QPushButton("Click me", self)
        pushBtn.move(20, 20)
        pushBtn.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.initWindow()
    window.show()
    app.exec()