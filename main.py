import os, sys, inspect
from subprocess import Popen, PIPE
import PySide2 as ref_mod
from PySide2.QtWidgets import *

def installUI():
    # 파일 이름
    dir = os.getcwd()  # root 폴더 경로 가져오기    os.getcwd() == __file__

    ui_dir_path = os.path.join(dir, "ui")  # *.ui 경로 가져오기
    ui_py_dir_path = os.path.join(dir, "ui_py")

    filenames = os.listdir(ui_dir_path)

    for filename in filenames:
        exe = os.path.join(os.path.dirname(inspect.getfile(ref_mod)), "uic.exe")  # 실행 명령어 입력하기 inspect.getfile(ref_mod) == ref_mod.__file__
        ui_path = os.path.join(ui_dir_path, filename)
        cmd = [exe] + ['-g', 'python'] + [ui_path]

        proc = Popen(cmd, stdout=PIPE, encoding='utf8')  # 명령어 실행

        ui_py_path = os.path.join(ui_py_dir_path, "ui_" + filename.replace(".ui", ".py"))
        out = open(ui_py_path, 'w')  # 저장할 파일 열기
        print(proc.stdout.read(), file=out)  # 파일 저장
        out.close()  # 저장 파일 닫기

        print("Success to make the file: ", filename, file=sys.stdout)

installUI()

from monitor import Monitor

app = QApplication(sys.argv)
mainWindow = Monitor()
mainWindow.show()
sys.exit(app.exec_())


