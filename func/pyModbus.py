import sys
from threading import Lock


class pyModbus():

    def __init__(self, serial):
        self.ser = serial
        self.count = 0
        self.lock = Lock()

    def crc16(data, byInt=False):
        # This code is ported from modbus CRC16(https://www.modbustools.com/modbus_crc16.htm)
        crcTable = [0x0000, 0xC0C1, 0xC181, 0x0140, 0xC301, 0x03C0, 0x0280, 0xC241, 0xC601, 0x06C0, 0x0780, 0xC741,
                    0x0500,
                    0xC5C1, 0xC481, 0x0440, 0xCC01, 0x0CC0, 0x0D80, 0xCD41, 0x0F00, 0xCFC1, 0xCE81, 0x0E40, 0x0A00,
                    0xCAC1,
                    0xCB81, 0x0B40, 0xC901, 0x09C0, 0x0880, 0xC841, 0xD801, 0x18C0, 0x1980, 0xD941, 0x1B00, 0xDBC1,
                    0xDA81,
                    0x1A40, 0x1E00, 0xDEC1, 0xDF81, 0x1F40, 0xDD01, 0x1DC0, 0x1C80, 0xDC41, 0x1400, 0xD4C1, 0xD581,
                    0x1540,
                    0xD701, 0x17C0, 0x1680, 0xD641, 0xD201, 0x12C0, 0x1380, 0xD341, 0x1100, 0xD1C1, 0xD081, 0x1040,
                    0xF001,
                    0x30C0, 0x3180, 0xF141, 0x3300, 0xF3C1, 0xF281, 0x3240, 0x3600, 0xF6C1, 0xF781, 0x3740, 0xF501,
                    0x35C0,
                    0x3480, 0xF441, 0x3C00, 0xFCC1, 0xFD81, 0x3D40, 0xFF01, 0x3FC0, 0x3E80, 0xFE41, 0xFA01, 0x3AC0,
                    0x3B80,
                    0xFB41, 0x3900, 0xF9C1, 0xF881, 0x3840, 0x2800, 0xE8C1, 0xE981, 0x2940, 0xEB01, 0x2BC0, 0x2A80,
                    0xEA41,
                    0xEE01, 0x2EC0, 0x2F80, 0xEF41, 0x2D00, 0xEDC1, 0xEC81, 0x2C40, 0xE401, 0x24C0, 0x2580, 0xE541,
                    0x2700,
                    0xE7C1, 0xE681, 0x2640, 0x2200, 0xE2C1, 0xE381, 0x2340, 0xE101, 0x21C0, 0x2080, 0xE041, 0xA001,
                    0x60C0,
                    0x6180, 0xA141, 0x6300, 0xA3C1, 0xA281, 0x6240, 0x6600, 0xA6C1, 0xA781, 0x6740, 0xA501, 0x65C0,
                    0x6480,
                    0xA441, 0x6C00, 0xACC1, 0xAD81, 0x6D40, 0xAF01, 0x6FC0, 0x6E80, 0xAE41, 0xAA01, 0x6AC0, 0x6B80,
                    0xAB41,
                    0x6900, 0xA9C1, 0xA881, 0x6840, 0x7800, 0xB8C1, 0xB981, 0x7940, 0xBB01, 0x7BC0, 0x7A80, 0xBA41,
                    0xBE01,
                    0x7EC0, 0x7F80, 0xBF41, 0x7D00, 0xBDC1, 0xBC81, 0x7C40, 0xB401, 0x74C0, 0x7580, 0xB541, 0x7700,
                    0xB7C1,
                    0xB681, 0x7640, 0x7200, 0xB2C1, 0xB381, 0x7340, 0xB101, 0x71C0, 0x7080, 0xB041, 0x5000, 0x90C1,
                    0x9181,
                    0x5140, 0x9301, 0x53C0, 0x5280, 0x9241, 0x9601, 0x56C0, 0x5780, 0x9741, 0x5500, 0x95C1, 0x9481,
                    0x5440,
                    0x9C01, 0x5CC0, 0x5D80, 0x9D41, 0x5F00, 0x9FC1, 0x9E81, 0x5E40, 0x5A00, 0x9AC1, 0x9B81, 0x5B40,
                    0x9901,
                    0x59C0, 0x5880, 0x9841, 0x8801, 0x48C0, 0x4980, 0x8941, 0x4B00, 0x8BC1, 0x8A81, 0x4A40, 0x4E00,
                    0x8EC1,
                    0x8F81, 0x4F40, 0x8D01, 0x4DC0, 0x4C80, 0x8C41, 0x4400, 0x84C1, 0x8581, 0x4540, 0x8701, 0x47C0,
                    0x4680,
                    0x8641, 0x8201, 0x42C0, 0x4380, 0x8341, 0x4100, 0x81C1, 0x8081, 0x4040]
        crc = [0xff, 0xff];
        for datum in data:
            ncrc = crcTable[(crc[0] ^ datum)]
            crc[0] = (ncrc & 0x00FF) ^ crc[1]
            crc[1] = ncrc >> 8

        if (byInt):
            return crc[0] * 256 + crc[1];
        return crc

    # 기능코드 : 02 Coil Read to Input
    def readInputStatus(self, id, address, num):
        with self.lock:
            # id : 국번, address : 시작 레지스터 주소, num : 읽어들 데이터 개수
            if num > 2000:
                print("ERROR: 한 번에 요청가능한 비트의 개수가 2000개입니다. 1register => 16bit, 16bit * 125 = 2000")
                return False
            hid = id

            if type(address) is str:
                address_hex = int(address[len(address) - 1], 16)

                address_dec = 0
                if len(address) > 1:
                    address_dec = int(address[0:len(address) - 1], 10)
                address = address_dec * 16 + address_hex
            else:
                address = int(address / 10) * 16 + address % 10

            haddressHi = address >> 8
            haddressLo = address & 0xff

            hnumHi = num >> 8
            hnumLo = num & 0xff

            hcrc = pyModbus.crc16([hid, 2, haddressHi, haddressLo, hnumHi, hnumLo])
            command = bytearray([hid, 2, haddressHi, haddressLo, hnumHi, hnumLo, hcrc[0], hcrc[1]])

            try:
                self.ser.write(command)
            except Exception as e:
                print(e, file=sys.stderr)
                return False

            ack_info = self.ser.read(3)
            ret = []
            if ack_info is not bytes():  # ack가 아무것도 들어오지 않았을 경우

                ack_id = ack_info[0]  # byte -> int
                ack_fn = ack_info[1]
                ack_byte_size = ack_info[2]

                cnt = num
                while (cnt):
                    ack = self.ser.read(1)[0]  # 1byte 데이터 가져옴
                    for i in range(0, 8):
                        ret += [ack & 1]
                        ack = ack >> 1
                        cnt -= 1
                        if cnt == 0: break
                ack_crc = self.ser.read(2)
            else:
                print("No Data")
                return False

            return ret

    # 기능코드 : 04
    #register는 최대 125개까지밖에 입력받을 수 없다
    def readInputRegisters(self, id, address, num):  # 아날로그 레지스터 값을 읽을 때 사용(WORD, 16bit로 읽어옴)
        with self.lock:
            if num > 125:
                print("ERROR: 한 번에 요청 가능한 레지스터 개수가 125개 입니다.(1register = 2bytes)")
                return False
            # id : 국번, address : 시작 레지스터 주소, num : 읽어들 데이터 개수
            hid = id

            haddressHi = address >> 8
            haddressLo = address & 0xff

            hnumHi = num >> 8
            hnumLo = num & 0xff

            hcrc = pyModbus.crc16([hid, 4, haddressHi, haddressLo, hnumHi, hnumLo])
            command = bytearray([hid, 4, haddressHi, haddressLo, hnumHi, hnumLo, hcrc[0], hcrc[1]])

            try:
                self.ser.write(command)
            except Exception as e:
                print(e, file=sys.stderr)
                return False

            ack_info = self.ser.read(3)

            ret = []
            if ack_info is not bytes():  # ack가 아무것도 들어오지 않았을 경우

                ack_id = ack_info[0]  # byte -> int
                ack_fn = ack_info[1]
                ack_byte_size = ack_info[2]

                cnt = ack_byte_size

                while (cnt):
                    dataHi = self.ser.read(1)[0]  # 1byte 데이터 가져옴
                    dataLo = self.ser.read(1)[0]
                    ret += [(dataHi << 8) + dataLo]
                    cnt -= 2

                ack_crc = self.ser.read(2)
            else:
                print("No Data")
                return [False]

            return ret

    # 기능코드 : 05
    def writeSingleCoil(self, id, address, on):
        with self.lock:
            # id : 국번, address : 시작 레지스터 주소, num : 읽어들 데이터 개수
            hid = id

            if type(address) is str:
                address_hex = int(address[len(address) - 1], 16)

                address_dec = 0
                if len(address) > 1:
                    address_dec = int(address[0:len(address) - 1], 10)
                address = address_dec*16 + address_hex

            else:
                address = int(address / 10) * 16 + address % 10

            haddressHi = address >> 8
            haddressLo = address & 0xff

            hnumHi = 0
            hnumLo = 0

            if on is True:
                hnumHi = 0xFF

            hcrc = pyModbus.crc16([hid, 5, haddressHi, haddressLo, hnumHi, hnumLo])
            command = bytearray([hid, 5, haddressHi, haddressLo, hnumHi, hnumLo, hcrc[0], hcrc[1]])

            try:
                self.ser.write(command)
            except Exception as e:
                print(e, file=sys.stderr)
                return False

            ret = self.ser.read(command.__len__())
            if ret is bytes():
                print("Fail to Write")
                return False

            return True
            # req와 ack가 동일하면 정상 응답

    # 기능코드 : 6
    def writeSingleRegister(self, id, address, data):
        with self.lock:
            # id : 국번, address : 시작 레지스터 주소, num : 읽어들 데이터 개수
            hid = id

            haddressHi = address >> 8
            haddressLo = address & 0xff

            hdataHi = data >> 8
            hdataLo = data & 0xFF

            hcrc = pyModbus.crc16([hid, 6, haddressHi, haddressLo, hdataHi, hdataLo])
            command = bytearray([hid, 6, haddressHi, haddressLo, hdataHi, hdataLo, hcrc[0], hcrc[1]])

            try:
                self.ser.write(command)
            except Exception as e:
                print(e, file=sys.stderr)
                return False

            ret = self.ser.read(command.__len__())
            if ret is bytes():
                print("Fail to Write")
                return False

            return True
        # req와 ack가 동일하면 정상 응답


if __name__ == '__main__':

    import serial
    import time
    # ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.1)  # timeout 단위: s
    ser = serial.Serial("COM3", baudrate=115200, timeout=0.1)  # timeout 단위: s
    # example

    modbus = pyModbus(ser)
    # 반환값 : ret-> bit 값이 각 list에 들어가있음.
    start = time.time()  # 시작 시간 저장
    while(True):

        # modbus.writeSingleCoil(1, 0, on=True)
        #modbus.writeSingleRegister(id=1, address=1, data=300)
        #ret = modbus.readInputStatus(id=1, address=1, num=1)
        #print(ret)
        ret = modbus.readInputRegisters(id=1, address=0, num=125) #가져올 수 있는 최대 개수가 125개
        # for i, v in enumerate(ret):
        #     print(i, v)
        # print("Clear")
        break

    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간