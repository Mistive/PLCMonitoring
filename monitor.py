from PySide2.QtWidgets import QMainWindow
from ui_monitor import Ui_monitor

'''
부모클래스에서는 자식 클래스를 선언할 수 없음....
'''

class Monitor(QMainWindow, Ui_monitor):
    ui = Ui_monitor()

    def __init__(self, parent=None):
        super(Monitor, self).__init__(parent)
        Monitor.ui.setupUi(self)


        '''
        현재의 문제점...
        부모 클래스에서 자식 클래스(Gui(), Communicaton())을 생성하려고 하기 때문에
        
        '''