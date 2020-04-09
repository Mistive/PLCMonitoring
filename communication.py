import threading, time
from PySide2.QtCore import *
#https://github.com/RavenKyu/OpenTutorials_PyQt/blob/master/QtFramework/QtWidgets/QProgressBar/QProgressBar_01_thread.py

class signalThread(QThread):
    finished = Signal(dict) #singal을 통해 어떤 인자를 보낼지 타입을 결정해야 한다. -> 안하면 에러 발생
    syncTest = 0
    def run(self):
        while True:
            with threading.Lock():
                data = {}
                data['test'] = self.get_info()
                self.finished.emit(data)
            time.sleep(1)

    def get_info(self):
        try:
            for i in range(0, 100000):
                signalThread.syncTest += 1
                print(signalThread.syncTest)
            return 1
        except Exception as e:
           print(e)

    @Slot()
    def sendSignal(self, data, thread):
        with threading.Lock():
            print("Send: ", data)






