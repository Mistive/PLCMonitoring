# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changeCarNumber.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(842, 642)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 60))
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 210))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setMaximumSize(QSize(500, 16777215))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(91, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(91, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(320, 102))
        self.frame_6.setMaximumSize(QSize(320, 102))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_6, 0, 1, 1, 1)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(520, 400))
        self.frame_7.setMaximumSize(QSize(520, 400))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.button7 = QPushButton(self.frame_7)
        self.button7.setObjectName(u"button7")
        self.button7.setGeometry(QRect(40, 202, 70, 70))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy)
        self.button7.setMinimumSize(QSize(70, 70))
        self.button7.setMaximumSize(QSize(70, 70))
        self.button3 = QPushButton(self.frame_7)
        self.button3.setObjectName(u"button3")
        self.button3.setGeometry(QRect(200, 50, 70, 70))
        sizePolicy.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy)
        self.button3.setMinimumSize(QSize(70, 70))
        self.button3.setMaximumSize(QSize(70, 70))
        self.button5 = QPushButton(self.frame_7)
        self.button5.setObjectName(u"button5")
        self.button5.setGeometry(QRect(119, 126, 70, 70))
        sizePolicy.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy)
        self.button5.setMinimumSize(QSize(70, 70))
        self.button5.setMaximumSize(QSize(70, 70))
        self.button6 = QPushButton(self.frame_7)
        self.button6.setObjectName(u"button6")
        self.button6.setGeometry(QRect(200, 126, 70, 70))
        sizePolicy.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy)
        self.button6.setMinimumSize(QSize(70, 70))
        self.button6.setMaximumSize(QSize(70, 70))
        self.button0 = QPushButton(self.frame_7)
        self.button0.setObjectName(u"button0")
        self.button0.setGeometry(QRect(40, 278, 70, 70))
        sizePolicy.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy)
        self.button0.setMinimumSize(QSize(70, 70))
        self.button0.setMaximumSize(QSize(70, 70))
        self.button9 = QPushButton(self.frame_7)
        self.button9.setObjectName(u"button9")
        self.button9.setGeometry(QRect(200, 202, 70, 70))
        sizePolicy.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy)
        self.button9.setMinimumSize(QSize(70, 70))
        self.button9.setMaximumSize(QSize(70, 70))
        self.button1 = QPushButton(self.frame_7)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(40, 50, 70, 70))
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setMinimumSize(QSize(70, 70))
        self.button1.setMaximumSize(QSize(70, 70))
        self.button4 = QPushButton(self.frame_7)
        self.button4.setObjectName(u"button4")
        self.button4.setGeometry(QRect(40, 126, 70, 70))
        sizePolicy.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy)
        self.button4.setMinimumSize(QSize(70, 70))
        self.button4.setMaximumSize(QSize(70, 70))
        self.button8 = QPushButton(self.frame_7)
        self.button8.setObjectName(u"button8")
        self.button8.setGeometry(QRect(119, 202, 70, 70))
        sizePolicy.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy)
        self.button8.setMinimumSize(QSize(70, 70))
        self.button8.setMaximumSize(QSize(70, 70))
        self.button2 = QPushButton(self.frame_7)
        self.button2.setObjectName(u"button2")
        self.button2.setGeometry(QRect(119, 50, 70, 70))
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setMinimumSize(QSize(70, 70))
        self.button2.setMaximumSize(QSize(70, 70))
        self.buttonClear = QPushButton(self.frame_7)
        self.buttonClear.setObjectName(u"buttonClear")
        self.buttonClear.setGeometry(QRect(118, 280, 150, 70))
        self.buttonClear.setMinimumSize(QSize(150, 70))
        self.buttonClear.setMaximumSize(QSize(130, 70))
        self.buttonSet = QPushButton(self.frame_7)
        self.buttonSet.setObjectName(u"buttonSet")
        self.buttonSet.setGeometry(QRect(280, 280, 150, 70))
        self.buttonSet.setMinimumSize(QSize(150, 70))
        self.buttonSet.setMaximumSize(QSize(130, 70))
        self.buttonModify = QPushButton(self.frame_7)
        self.buttonModify.setObjectName(u"buttonModify")
        self.buttonModify.setGeometry(QRect(281, 170, 150, 100))
        self.buttonModify.setMinimumSize(QSize(150, 100))
        self.buttonModify.setMaximumSize(QSize(130, 100))
        self.buttonBefore = QPushButton(self.frame_7)
        self.buttonBefore.setObjectName(u"buttonBefore")
        self.buttonBefore.setGeometry(QRect(280, 90, 150, 70))
        self.buttonBefore.setMinimumSize(QSize(150, 70))
        self.buttonBefore.setMaximumSize(QSize(130, 70))
        self.buttonNext = QPushButton(self.frame_7)
        self.buttonNext.setObjectName(u"buttonNext")
        self.buttonNext.setGeometry(QRect(280, 20, 150, 70))
        self.buttonNext.setMinimumSize(QSize(150, 70))
        self.buttonNext.setMaximumSize(QSize(130, 70))

        self.gridLayout_3.addWidget(self.frame_7, 1, 0, 1, 3)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 2, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button7.setText(QCoreApplication.translate("Form", u"7", None))
        self.button3.setText(QCoreApplication.translate("Form", u"3", None))
        self.button5.setText(QCoreApplication.translate("Form", u"5", None))
        self.button6.setText(QCoreApplication.translate("Form", u"6", None))
        self.button0.setText(QCoreApplication.translate("Form", u"0", None))
        self.button9.setText(QCoreApplication.translate("Form", u"9", None))
        self.button1.setText(QCoreApplication.translate("Form", u"1", None))
        self.button4.setText(QCoreApplication.translate("Form", u"4", None))
        self.button8.setText(QCoreApplication.translate("Form", u"8", None))
        self.button2.setText(QCoreApplication.translate("Form", u"2", None))
        self.buttonClear.setText(QCoreApplication.translate("Form", u"\uc815\uc815", None))
        self.buttonSet.setText(QCoreApplication.translate("Form", u"\uc644\ub8cc", None))
        self.buttonModify.setText(QCoreApplication.translate("Form", u"\uc218\uc815", None))
        self.buttonBefore.setText(QCoreApplication.translate("Form", u"\uc774\uc804", None))
        self.buttonNext.setText(QCoreApplication.translate("Form", u"\ub2e4\uc74c", None))
    # retranslateUi


