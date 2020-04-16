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

        self.sig.Sig_getInfoFinished.connect(self.update_info)
        self.sig.Sig_connectFinished.connect(self.update_connect)
        self.sig.Sig_getCarNumber.connect(self.update_carNumber)
        self.ui.buttonConnect.clicked.connect(lambda: self.sig.set_serial_port())

        self.carList = [None]
        self.carCList = [None]

        self.img_parking = [[QPixmap('./img/none.png'), QPixmap('./img/emptyS.png'), QPixmap('./img/parkingS.png')], [QPixmap('./img/none.png'), QPixmap('./img/emptyR.png'), QPixmap('./img/parkingR.png')]]

        self.init_update_parkingMonitor()
        self.connectButton()

        #click을 눌렀을 경우 데이터를 communication.py에 보내기
        data = {}
        data['send'] = 'Good'
        self.ui.buttonIn.clicked.connect(lambda: self.sig.sendSignal(data))



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





            # for i, value in enumerate(self.sig.data['parkinginfo']):
            #     if i % 2 == 0:
            #         if self.carLList[int(i/2)]['type'] == '승용':
            #             print(i, value)
            #             self.carLList[int(i / 2)]['widget'].labelCarImg.setPixmap(self.img_parking_S[value])
            #         if self.carLList[int(i/2)]['type'] == 'RV':
            #             self.carLList[int(i / 2)]['widget'].labelCarImg.setPixmap(self.img_parking_R[value])
            #     if i % 2 == 1:
            #         print(i, value)
            #         if self.carRList[int(i / 2)]['type'] == '승용':
            #             self.carRList[int(i / 2)]['widget'].labelCarImg.setPixmap(self.img_parking_S[value])
            #         if self.carRList[int(i / 2)]['type'] == 'RV':
            #             self.carRList[int(i / 2)]['widget'].labelCarImg.setPixmap(self.img_parking_R[value])
            # self.data['차량번호'] = self.mb.readInputRegisters(1, 4200, 1)  # 차량 번호

        # except Exception as e:
        #     print(e, file=sys.stderr)
        #     pass


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
        INPUTCOUNTER = int(config['진입카운터'])
        URS = int(config['상부RV시작번호'])
        URE = int(config['상부RV끝번호'])
        NRS = int(config['하부RV시작번호'])
        NRE = int(config['하부RV끝번호'])
        USS = int(config['상부일반시작번호'])
        USE = int(config['상부일반끝번호'])
        NSS = int(config['하부일반시작번호'])
        NSE = int(config['하부일반끝번호'])

        car_floor = int(CNUM / 2) + 1 #진입층 추가


        for floor in range(1, car_floor+1):
            idx = floor*2-1
            if (idx >= USS and idx <=USE) or (idx >= NSS and idx <= NSE):
                type = '승용'
                tidx = 0
            else:
                type = 'RV'
                tidx = 1

            if floor == INPUTCOUNTER:
                self.carCList.append({'widget': centerCar(), 'floor': floor})
            else:
                self.carList.append({'widget' : leftCar(), 'floor' : floor, 'type' : type, 'tidx' : tidx})
                self.carList.append({'widget': rightCar(), 'floor': floor, 'type': type, 'tidx': tidx})
                self.carCList.append({'widget': centerCar(), 'floor': floor})


        #Widget 추가
        idx = 1
        for floor in range(1, car_floor+1):
            if floor == INPUTCOUNTER:
                print('진입구: ', car_floor-floor)
                self.ui.layoutLeft.addWidget(inputLeft(), car_floor - floor, 0, 1, 1)
                self.ui.layoutRight.addWidget(inputRight(), car_floor - floor, 2, 1, 1)
                self.ui.layoutCenter.addWidget(self.carCList[floor]['widget'], car_floor - floor, 1, 1, 1)
            else:
                self.ui.layoutLeft.addWidget(self.carList[idx]['widget'], car_floor - floor, 0, 1, 1)
                self.ui.layoutRight.addWidget(self.carList[idx + 1]['widget'], car_floor - floor, 2, 1, 1)
                self.ui.layoutCenter.addWidget(self.carCList[floor]['widget'], car_floor - floor, 1, 1, 1)
                idx += 2

        for idx, car in enumerate(self.carList):
            if car is None: continue
            car['widget'].labelCarIdx.setText(car['type'] + "\n" + str(idx))
            car['widget'].labelCarImg.setPixmap(self.img_parking[car['tidx']][1])



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

