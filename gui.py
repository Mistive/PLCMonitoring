# -*- coding:utf-8 -*-
from monitor import Monitor

from PySide2.QtWidgets import QMainWindow, QFrame, QGridLayout
from PySide2.QtGui import *
from PySide2.QtCore import *  # Signal()

from ui_leftCar import Ui_leftCar
from ui_rightCar import Ui_rightCar
from ui_centerCar import Ui_centerCar

class Gui(Monitor):
    def __init__(self):
        print("Gui: ", Monitor.ui)
        self.ui = Monitor.ui

        self.CAR_NUMBER = [0, 0, 0, 0]
        self.CAR_NUMBER_POS = len(self.CAR_NUMBER) - 1
        self.carMonitoring()
        self.connectButton()

        print('Done to make MainWindow')

    def connectButton(self):
        self.button_list = [self.ui.button0, self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4,
                            self.ui.button5, self.ui.button6, self.ui.button7, self.ui.button8, self.ui.button9]

        for i, btn in enumerate(self.button_list):
            btn.clicked.connect(lambda stat=False, idx=i: self.setCarNumber(idx))

        self.ui.buttonSet.clicked.connect(self.buttonSet)
        self.ui.buttonClear.clicked.connect(self.buttonClear)
        self.ui.buttonIn.clicked.connect(self.buttonIn)
        self.ui.buttonOut.clicked.connect(self.buttonOut)

    def carMonitoring(self):
        self.CAR_NUM = 30
        self.carLList = []
        self.carRList = []
        self.carCList = []

        self.ui.layoutMonitor = QGridLayout(self.ui.scrollAreaWidgetContents)
        self.ui.layoutMonitor.setSpacing(0)
        self.ui.layoutMonitor.setAlignment(Qt.AlignBottom)
        self.ui.layoutMonitor.setContentsMargins(0, 0, 0, 0)

        for floor in range(0, int(self.CAR_NUM / 2)):
            self.carLList.append(leftCar())
            self.carRList.append(rightCar())
            self.carCList.append(centerCar())

            self.ui.layoutMonitor.addWidget(self.carLList[floor], self.CAR_NUM - floor, 0, 1, 1)
            self.ui.layoutMonitor.addWidget(self.carCList[floor], self.CAR_NUM - floor, 1, 1, 1)
            self.ui.layoutMonitor.addWidget(self.carRList[floor], self.CAR_NUM - floor, 2, 1, 1)

        for floor in range(0, int(self.CAR_NUM / 2)):
            self.carLList[floor].labelCarIdx.setText("승용\n" + str(floor * 2 + 1))
            self.carRList[floor].labelCarIdx.setText("승용\n" + str(floor * 2 + 2))

    def buttonSet(self):
        print("완료 버튼")

    def buttonIn(self):
        print("입고 버튼")

    def buttonOut(self):
        print("출고 버튼")

    def buttonClear(self):
        self.CAR_NUMBER = [0, 0, 0, 0]
        self.CAR_NUMBER_POS = len(self.CAR_NUMBER) - 1
        self.setCarNumberText()

    def setCarNumber(self, num):
        # 입력된 키값 차 번호에 저장
        self.CAR_NUMBER[self.CAR_NUMBER_POS] = num
        self.CAR_NUMBER_POS -= 1

        self.setCarNumberText()

        # 초기화
        if self.CAR_NUMBER_POS < 0:
            self.CAR_NUMBER = [0 for _ in range(len(self.CAR_NUMBER))]
            self.CAR_NUMBER_POS = len(self.CAR_NUMBER) - 1

    def setCarNumberText(self):
        # 차 번호 세팅
        self.ui.labelCNum.setText(''.join(str(e) for e in self.CAR_NUMBER))

class leftCar(QFrame, Ui_leftCar):
    def __init__(self, parent=None):
        super(leftCar, self).__init__(parent)
        self.setupUi(self)


class rightCar(QFrame, Ui_rightCar):
    def __init__(self, parent=None):
        super(rightCar, self).__init__(parent)
        self.setupUi(self)


class centerCar(QFrame, Ui_centerCar):
    def __init__(self, parent=None):
        super(centerCar, self).__init__()
        self.setupUi(self)