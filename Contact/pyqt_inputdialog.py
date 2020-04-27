import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("Input Dialog Test")

        self.pushbtn = QPushButton("Input number")
        self.pushbtn.clicked.connect(self.input_number)
        self.pushbtn2 = QPushButton("Input Item")
        self.pushbtn2.clicked.connect(self.input_item)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushbtn)
        layout.addWidget(self.pushbtn2)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def input_number(self):
        #return tuple(text, ok)
        text, ok = QInputDialog.getInt(self, '매수 수랑', '매수 수량을 입력하세요')
        if ok:
            self.label.setText(str(text))
        else:
            self.label.setText("None")

    def input_item(self):
        items = ("배영규", "김수진", "배한빈")
        #5th : default item index, 6th : 아이템 수정 가능 여부
        item, ok = QInputDialog.getItem(self, "이름 선택", "이름을 선택해주세요", items, 0, True)
        if ok and item:
            self.label.setText(item)
        else:
            self.label.setText("None")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWindow()
    mywin.show()
    app.exec()
