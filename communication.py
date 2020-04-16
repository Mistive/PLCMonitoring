import threading, time
from PySide2.QtCore import *
import serial, configparser
from pyModbus import pyModbus
#https://github.com/RavenKyu/OpenTutorials_PyQt/blob/master/QtFramework/QtWidgets/QProgressBar/QProgressBar_01_thread.py

class signalThread(QThread):
    Sig_getInfoFinished = Signal()  # singal을 통해 어떤 인자를 보낼지 타입을 결정해야 한다. -> 안하면 에러 발생
    Sig_connectFinished = Signal(bool)
    Sig_carButtonPressed = Signal(int)
    Sig_getCarNumber = Signal(list)

    lock = threading.Lock()
    data = {}

    # 설정값 불러오기
    config = configparser.ConfigParser()
    config.read('./func/config.ini', encoding='utf-8')
    serial_conf = config['SERIAL']
    ser = serial.Serial()
    mb = pyModbus(ser)

    def __init__(self, parent=None):
        super().__init__(parent)

    def set_serial_port(self):
        try:
            self.ser = serial.Serial(
                port=self.serial_conf['PORT'],
                baudrate=self.serial_conf['BAUDRATE'],
                timeout=float(self.serial_conf['TIMEOUT']),
                bytesize=int(self.serial_conf['BYTESIZE']),
                parity=self.serial_conf['PARITY'],
                stopbits=int(self.serial_conf['STOPBITS']),
                xonxoff=(self.serial_conf['XONXOFF'] == 'True'),
                rtscts=(self.serial_conf['RTSCTS'] == 'True'),
                dsrdtr=(self.serial_conf['DSRDTR'] == 'True')
            )  # timeout 단위: s
            self.mb = pyModbus(self.ser)
            self.Sig_connectFinished.emit(True)

        except Exception as e:
            self.Sig_connectFinished.emit(False)
            if self.ser.is_open:
                self.ser.close()
            print(e)

    def run(self):
        while True:
            # plc 연결 주기적 체크
            if not self.ser.is_open:
                time.sleep(1)
                continue
            self.data['isConnected'] = self.mb.readInputStatus(1, 1, 1)
            if self.data['isConnected'] is False:
                self.Sig_connectFinished.emit(False)
                self.ser.close()
                time.sleep(1)
                continue

            #plc 정보 가져오기
            self.get_info(self.data)
            self.Sig_getInfoFinished.emit()
            time.sleep(0.1)



    def get_info(self, data): #read
        self.getCarNumber()
        self.data['info'] = {}
        self.data['info']['차량번호'] = self.mb.readInputRegisters(1,4200,1)[0]    #차량 번호
        self.data['info']['적재파렛'] = self.mb.readInputRegisters(1,3003,1)[0]    #적재 파렛
        self.data['info']['출고파렛'] = self.mb.readInputRegisters(1,3004,1)[0]    #출고 파렛
        self.data['info']['전체주차'] = self.mb.readInputRegisters(1,70,1)[0]    #전체 주차
        self.data['info']['RV주차'] = self.mb.readInputRegisters(1,79,1)[0]    #RV 주차
        self.data['info']['일반주차'] = self.mb.readInputRegisters(1, 73, 1)[0]  # 일반 주차
        self.data['info']['전체공차'] = self.mb.readInputRegisters(1, 71, 1)[0]  # 전체 공차
        self.data['info']['RV공차'] = self.mb.readInputRegisters(1, 78, 1)[0]  # RV 공차
        self.data['info']['일반공차'] = self.mb.readInputRegisters(1, 72, 1)[0]  # 일반 공차


        self.data['parkinginfo'] = []
        img = [None] + self.mb.readInputRegisters(1, 2401, int(self.config['PARKING_INFO']['전체파렛수']))  # 일반 공차
        number = [None] + self.mb.readInputRegisters(1, 4001, int(self.config['PARKING_INFO']['전체파렛수']))  # 일반 공차

        for i in range(0, int(self.config['PARKING_INFO']['전체파렛수'])+1):
            self.data['parkinginfo'].append({'img' : img[i], 'number' : number[i]})





    @Slot()
    def sendSignal(self, data): #write
        with self.lock:
            #modbus WriteCoil
            print("Send: ", data)

    @Slot()
    def buttonCarNumber(self, idx):
        if not self.ser.is_open:
            return
        self.mb.writeSingleCoil(1, idx, True)
        self.mb.writeSingleCoil(1, idx, False)
        self.getCarNumber()

    @Slot()
    def buttonSet(self):
        if not self.ser.is_open:
            return
        self.mb.writeSingleCoil(1, 'c', True)
        self.mb.writeSingleCoil(1, 'c', False)
        self.getCarNumber()

    @Slot()
    def buttonIn(self):
        if not self.ser.is_open:
            return

    @Slot()
    def buttonOut(self):
        if not self.ser.is_open:
            return

    @Slot()
    def buttonClear(self):
        if not self.ser.is_open:
            return
        print('Clear')
        self.mb.writeSingleCoil(1, 'f', True)
        self.mb.writeSingleCoil(1, 'f', False)
        self.getCarNumber()

    def getCarNumber(self):
        self.data['CARNUMBER'] = self.mb.readInputRegisters(1, 13002, 4)  # 입출고 출력 번호
        self.Sig_getCarNumber.emit(self.data['CARNUMBER'])










