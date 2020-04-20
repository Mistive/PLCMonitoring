from PySide2.QtWidgets import * #QMainWindow, QWidget, QGridLayout
from PySide2.QtCore import *    #Signal()
from PySide2.QtGui import *

import os, sys
from communication import signalThread

from ui_monitor import Ui_monitor
from ui_leftCar import Ui_leftCar
from ui_rightCar import Ui_rightCar
from ui_centerCar import Ui_centerCar
from ui_inputLeft import Ui_inputLeft
from ui_inputRight import Ui_inputRight
from ui_leftStorage import Ui_leftStorage
from ui_rightStorage import Ui_rightStorage
from ui_changeCarNumber import Ui_changeCarNumber
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

        self.sig = signalThread()
        self.sig.start()

        self.carList = [None]   #주차 격납고 리스트
        self.carCList = [None]  #주차 리프트 리스트
        self.storageList = []   #보관소 리스트
        self.car_floor = 0      #승강기식 층수(진입구 + 보관소(보관소는 전체를 1개의 층으로 식별)

        self.img_parking = [[QPixmap('./img/none.png'), QPixmap('./img/emptyS.png'), QPixmap('./img/parkingS.png')], [QPixmap('./img/none.png'), QPixmap('./img/emptyR.png'), QPixmap('./img/parkingR.png')]]
        self.img_storage = [QPixmap('./img/emptystorage.png'), QPixmap('./img/storage.png')]
        self.img_lift = [QPixmap('./img/none.png'), QPixmap('./img/emptyS.png'), QPixmap('./img/emptyS.png'), QPixmap('./img/parkingS.png')]

        self.init_update_parkingMonitor()
        self.connectButton()

        self.sig.Sig_getInfoFinished.connect(self.update_info)
        self.sig.Sig_connectFinished.connect(self.update_connect)
        self.sig.Sig_getCarNumber.connect(self.update_carNumber)
        self.ui.buttonExit.clicked.connect(lambda: self.close())
        self.ui.buttonConnect.clicked.connect(lambda: self.sig.set_serial_port())

        self.ui.scrollArea.verticalScrollBar().rangeChanged.connect(self.update_init_scrollArea)



        #click을 눌렀을 경우 데이터를 communication.py에 보내기
        data = {}
        data['send'] = 'Good'
        self.ui.buttonIn.clicked.connect(lambda: self.sig.sendSignal(data))

    @Slot()
    def update_init_scrollArea(self):
        scrollbar = self.ui.scrollArea.verticalScrollBar()
        QScrollBar.setSingleStep(scrollbar, 100)
        QScrollBar.setValue(scrollbar, scrollbar.maximum())



    @Slot()
    def update_carNumber(self, car_number):
        car_number.reverse()
        car_number  = ''.join(str(e) for e in car_number)
        self.ui.labelCNum.setText(car_number)

    @Slot(int)
    def update_connect(self, isconnected):
        if isconnected:
            self.ui.labelConnectCheck.setText('Connected')
            self.ui.buttonConnect.setText('연결 끊기')
        else:
            self.ui.labelConnectCheck.setText('Disconnected')
            self.ui.buttonConnect.setText('연결 하기')

    @Slot()
    def update_info(self):
        # try:
        print(self.sig.data)

        self.ui.labelParkingNum.setText(str(self.sig.data['info']['전체주차']))
        self.ui.labelEmptyNum.setText(str(self.sig.data['info']['전체공차']))
        self.ui.labelSedanParkingNum.setText(str(self.sig.data['info']['일반주차']))
        self.ui.labelSedanEmptyNum.setText(str(self.sig.data['info']['일반공차']))
        self.ui.labelRVParkingNum.setText(str(self.sig.data['info']['RV주차']))
        self.ui.labelRVEmptyNum.setText(str(self.sig.data['info']['RV공차']))
        self.ui.labelINSell.setText(str(self.sig.data['info']['적재파렛']))
        self.ui.labelOUTSell.setText(str(self.sig.data['info']['출고파렛']))

        for idx, value in enumerate(self.sig.data['parkinginfo']):
            if value['img'] is None or value['number'] is None: continue
            car = self.carList[idx]
            car['widget'].labelCarImg.setPixmap(self.img_parking[car['tidx']][value['img']])
            if value['number'] is not 0:
                car['widget'].labelCarNum.setText(str(value['number']))

        for idx, lift in enumerate(self.carCList):
            if lift is None: continue
            if lift['address'] is None: continue

            value = self.sig.data['lift'][lift['address']]
            lift['widget'].labelCarImg.setPixmap(self.img_lift[value])




    def connectButton(self):
        self.button_list = [self.ui.button0, self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4,
                            self.ui.button5, self.ui.button6, self.ui.button7, self.ui.button8, self.ui.button9]

        for i, btn in enumerate(self.button_list):
            # btn.clicked.connect(lambda stat=False, idx=i: self.setCarNumber(idx))
            btn.clicked.connect(lambda stat=False, idx=i: self.sig.buttonCarNumber(idx))

        self.ui.buttonSet.clicked.connect(self.sig.buttonSet)
        self.ui.buttonClear.clicked.connect(self.sig.buttonClear)
        self.ui.buttonIn.clicked.connect(self.sig.buttonIn)
        self.ui.buttonOut.clicked.connect(self.sig.buttonOut)

    def init_update_parkingMonitor(self):


        #오른쪽으로 QWidget보내기 : layoutDirection 변경
        self.ui.layoutLeft = QGridLayout(self.ui.frameLeft)
        self.ui.layoutRight = QGridLayout(self.ui.frameRight)
        self.ui.layoutCenter = QGridLayout(self.ui.frameCenter)
        #
        self.ui.layoutLeft.setAlignment(Qt.AlignBottom|Qt.AlignRight)
        self.ui.layoutRight.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.ui.layoutCenter.setAlignment(Qt.AlignBottom|Qt.AlignLeft)

        self.ui.layoutLeft.setSpacing(0)
        self.ui.layoutRight.setSpacing(0)
        self.ui.layoutCenter.setSpacing(0)

        self.ui.layoutLeft.setMargin(0)
        self.ui.layoutRight.setMargin(0)
        self.ui.layoutCenter.setMargin(0)

        config = self.sig.config['PARKING_INFO']
        CNUM = int(config['전체파렛수'])
        STORAGESTART = int(config['보관소시작번호'])
        STORAGEEND = int(config['보관소끝번호'])
        INPUTCOUNTER = int(config['진입카운터'])
        URS = int(config['상부RV시작번호'])
        URE = int(config['상부RV끝번호'])
        NRS = int(config['하부RV시작번호'])
        NRE = int(config['하부RV끝번호'])
        USS = int(config['상부일반시작번호'])
        USE = int(config['상부일반끝번호'])
        NSS = int(config['하부일반시작번호'])
        NSE = int(config['하부일반끝번호'])

        self.car_floor = int(CNUM / 2) + 1  # 진입층 추가

        #보관소 추가
        self.ui.frameLeftStorage = QFrame()
        self.ui.frameRightStorage = QFrame()
        self.ui.layoutLeftStorage = QGridLayout(self.ui.frameLeftStorage)
        self.ui.layoutRightStorage = QGridLayout(self.ui.frameRightStorage)
        self.ui.frameLeftStorage.setLayoutDirection(Qt.RightToLeft)
        # self.ui.frameLeftStorage.setFrameShape(QFrame.Box)
        # self.ui.frameRightStorage.setFrameShape(QFrame.Box)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.ui.frameLeftStorage.setSizePolicy(sizePolicy4)
        self.ui.frameRightStorage.setSizePolicy(sizePolicy4)
        self.ui.frameLeftStorage.setMinimumHeight(100)
        self.ui.frameLeftStorage.setMaximumHeight(100)
        self.ui.frameRightStorage.setMinimumHeight(100)
        self.ui.frameRightStorage.setMaximumHeight(100)
        # self.ui.frameLeftStorage.setMinimumSize(QSize(110, 80))
        # self.ui.frameLeftStorage.setMaximumSize(QSize(110, 80))
        # self.ui.frameRightStorage.setMinimumSize(QSize(110, 80))
        # self.ui.frameRightStorage.setMaximumSize(QSize(110, 80))

        self.ui.layoutLeftStorage.setSpacing(0)
        self.ui.layoutRightStorage.setSpacing(0)
        self.ui.layoutLeftStorage.setMargin(0)
        self.ui.layoutRightStorage.setMargin(0)
        self.car_floor += 1  #보관소 추가

        address = 1
        for floor in range(1, self.car_floor+1):
            idx = floor*2-1
            if (idx >= USS and idx <=USE) or (idx >= NSS and idx <= NSE):
                type = '승용'
                tidx = 0
            else:
                type = 'RV'
                tidx = 1

            if floor == INPUTCOUNTER:
                type = '진입구'
                self.carCList.append({'widget': centerCar(), 'floor': floor, 'type': type, 'address': address})
                address += 1
            elif floor == INPUTCOUNTER+1: #후에 보관소 존재 유무 추가
                type = '보관소'
                tidx = 2
                self.carCList.append({'widget': centerCar(), 'floor': floor, 'type': type,  'address': None})
                for idx in range(STORAGESTART, STORAGEEND+1, 2):
                    self.storageList.append({'widget':leftStorage(), 'idx': idx, 'floor': floor, 'type': type, 'tidx': tidx})
                    self.storageList.append({'widget':rightStorage(), 'idx': idx+1, 'floor': floor, 'type': type, 'tidx': tidx})
            else:
                self.carList.append({'widget' : leftCar(), 'floor' : floor, 'type' : type, 'tidx' : tidx})
                self.carList.append({'widget': rightCar(), 'floor': floor, 'type': type, 'tidx': tidx})
                self.carCList.append({'widget': centerCar(), 'floor': floor, 'type': type, 'address': address})
                address += 1


        #Widget 추가
        caridx = 1
        for floor in range(1, self.car_floor+1):
            if floor == INPUTCOUNTER:   #진입구 생성
                self.ui.layoutLeft.addWidget(inputLeft(), self.car_floor - floor, 0, 1, 1)
                self.ui.layoutRight.addWidget(inputRight(), self.car_floor - floor, 2, 1, 1)
                self.ui.layoutCenter.addWidget(self.carCList[floor]['widget'], self.car_floor - floor, 1, 1, 1)

            elif floor == INPUTCOUNTER +1:  #보관소 생성
                self.ui.layoutLeft.addWidget(self.ui.frameLeftStorage, self.car_floor-floor, 0, 1, 1)
                self.ui.layoutRight.addWidget(self.ui.frameRightStorage, self.car_floor-floor, 2, 1, 1)
                self.ui.layoutCenter.addWidget(self.carCList[floor]['widget'], self.car_floor - floor, 1, 1, 1)

                horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                for idx in range(0, STORAGEEND-STORAGESTART, 2):
                    self.ui.layoutLeftStorage.addItem(horizontalSpacer, STORAGEEND-STORAGESTART - idx, 1, 1, 1)
                    self.ui.layoutLeftStorage.addWidget(self.storageList[idx]['widget'], STORAGEEND-STORAGESTART - idx, 0, 1, 1)
                    self.ui.layoutRightStorage.addWidget(self.storageList[idx+1]['widget'],STORAGEEND-STORAGESTART- idx, 0, 1, 1)
                    self.ui.layoutRightStorage.addItem(horizontalSpacer, STORAGEEND - STORAGESTART - idx, 1, 1, 1)

            else:   #주차 구역 생성
                self.ui.layoutLeft.addWidget(self.carList[caridx]['widget'], self.car_floor - floor, 0, 1, 1)
                self.ui.layoutRight.addWidget(self.carList[caridx + 1]['widget'], self.car_floor - floor, 2, 1, 1)
                self.ui.layoutCenter.addWidget(self.carCList[floor]['widget'], self.car_floor - floor, 1, 1, 1)
                caridx += 2

        for idx, car in enumerate(self.carList):
            if car is None: continue
            clickable(car['widget']).connect(self.changeCarNumberWindow)

            car['widget'].labelCarIdx.setText(car['type'] + "\n" + str(idx))
            car['widget'].labelCarImg.setPixmap(self.img_parking[car['tidx']][1])

        for idx, storage in enumerate(self.storageList):
            storage['widget'].labelCarIdx.setText(str(storage['idx']))
            storage['widget'].labelCarImg.setPixmap(self.img_storage[1])

        for idx, lift in enumerate(self.carCList):
            if lift is None: continue
            if lift['type'] == '보관소':
                lift['widget'].labelCarImg.setHidden(True)
                continue

            if lift['type'] == '진입구':
                lift['widget'].labelCarImg.setPixmap(self.img_lift[1])
            else:
                lift['widget'].labelCarImg.setPixmap(self.img_lift[0])

    def changeCarNumberWindow(self):
        self.cN = changeCarNumber()
        self.cN.showFullScreen()



#label, frame 등을 click 이벤트가 가능하게 만들어 주는 것
def clickable(widget):
    class Filter(QObject):

        clicked = Signal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True

            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


class changeCarNumber(QWidget, Ui_changeCarNumber):
    def __init__(self, parent=None):
        super(changeCarNumber, self).__init__(parent)
        self.setupUi(self)

        self.buttonReturn.clicked.connect(self.returnWindow)

    def returnWindow(self):
        self.close()




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

class inputLeft(QFrame, Ui_inputLeft):
    def __init__(self, parent=None):
        super(inputLeft, self).__init__()
        self.setupUi(self)

class inputRight(QFrame, Ui_inputRight):
    def __init__(self, parent=None):
        super(inputRight, self).__init__()
        self.setupUi(self)

class leftStorage(QFrame, Ui_leftStorage):
    def __init__(self, parent=None):
        super(leftStorage, self).__init__()
        self.setupUi(self)

class rightStorage(QFrame, Ui_rightStorage):
    def __init__(self, parent=None):
        super(rightStorage, self).__init__()
        self.setupUi(self)

