from PySide2.QtWidgets import * #QMainWindow, QWidget, QGridLayout
from PySide2.QtCore import *    #Signal()
from PySide2.QtGui import *

from communication import signalThread

from ui_monitor import Ui_monitor
from ui_leftCar import Ui_leftCar
from ui_rightCar import Ui_rightCar
from ui_centerCar import Ui_centerCar
'''
signal/slot 기능을 활용하여 community.py의 thread에서 연산이 완료된 값을 Monitor로 가져와서 ui에 반영시킴 : Ui를 계속 업데이트 시킬 필요가 없음.(개꿀) 일종의 비동기
'''
'''
다음 해결과제는 Gui에서 처리한 값을 어떻게 community로 보낼 것인가?
'''
class Monitor(QMainWindow, Ui_monitor):

    def __init__(self):
        super(Monitor, self).__init__()
        self.ui = Ui_monitor()
        self.ui.setupUi(self)

        self.CAR_NUMBER = [0, 0, 0, 0]
        self.CAR_NUMBER_POS = len(self.CAR_NUMBER) - 1
        self.carMonitoring()
        self.connectButton()

        self.sig = signalThread()
        self.sig.start()
        self.sig.finished.connect(self.update_info)
        self.sig.connectfinished.connect(self.update_connect)
        self.ui.buttonConnect.clicked.connect(lambda: self.sig.set_serial_port())


        #click을 눌렀을 경우 데이터를 communication.py에 보내기
        data = {}
        data['send'] = 'Good'
        self.ui.buttonIn.clicked.connect(lambda: self.sig.sendSignal(data))

    @Slot(int)
    def update_connect(self, isconnected):
        if isconnected:
            self.ui.labelConnectCheck.setText('Connected')
            self.ui.buttonConnect.setText('연결 끊기')
        else:
            self.ui.labelConnectCheck.setText('Disconnected')
            self.ui.buttonConnect.setText('연결 하기')

    @Slot(dict)
    def update_info(self, data):
        try:
            print('Update Info', data)
        except Exception as e:
            print(e)
            pass

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
