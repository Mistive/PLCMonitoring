from PySide2.QtWidgets import QMainWindow
from ui_monitor import Ui_monitor
from PySide2.QtCore import *
from communication import signalThread
import time
'''
signal/slot 기능을 활용하여 community.py의 thread에서 연산이 완료된 값을 Monitor로 가져와서 ui에 반영시킴 : Ui를 계속 업데이트 시킬 필요가 없음.(개꿀) 일종의 비동기
'''
'''
다음 해결과제는 Gui에서 처리한 값을 어떻게 community로 보낼 것인가?
'''
class Monitor(QMainWindow, Ui_monitor):

    def __init__(self):
        super(Monitor, self).__init__()
        self.setupUi(self)

        self.sig = signalThread()
        self.sig.start()

        #통신을 통해 한 스캔을 완료했을 경우 발생하는 signal이 finished이고, 해당 시그널이 발생하면 통신 결과를 Gui에 바로 반영할 수 있도록 update_info()를 호출
        #그리고 update_info()의 인자로 받아온 값들을 통해 gui에 바로 업데이트를 할 수 있다.
        self.sig.finished.connect(self.update_info)

        #click을 눌렀을 경우 데이터를 communication.py에 보내기
        data = {}
        data['send'] = 'Good'
        self.buttonIn.clicked.connect(lambda: self.sig.sendSignal(data))






    @Slot(dict)
    def update_info(self, data):
        try:
            print('Update Info', data)
        except Exception as e:
            print(e)
            pass