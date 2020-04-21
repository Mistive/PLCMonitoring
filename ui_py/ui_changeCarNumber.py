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


class Ui_changeCarNumber(object):
    def setupUi(self, changeCarNumber):
        if changeCarNumber.objectName():
            changeCarNumber.setObjectName(u"changeCarNumber")
        changeCarNumber.resize(844, 660)
        changeCarNumber.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(changeCarNumber)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(changeCarNumber)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(826, 60))
        self.frame_2.setMaximumSize(QSize(826, 60))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(242, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.buttonReturn = QPushButton(self.frame_2)
        self.buttonReturn.setObjectName(u"buttonReturn")
        self.buttonReturn.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.buttonReturn, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(241, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(19)
        self.label.setFont(font)

        self.gridLayout_4.addWidget(self.label, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame = QFrame(changeCarNumber)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(826, 576))
        self.frame.setMaximumSize(QSize(826, 576))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(460, 540))
        self.frame_3.setMaximumSize(QSize(460, 560))
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(350, 400))
        self.frame_7.setMaximumSize(QSize(10000, 10000))
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.gridLayout_7 = QGridLayout(self.frame_7)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.button1 = QPushButton(self.frame_7)
        self.button1.setObjectName(u"button1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy1)
        self.button1.setMinimumSize(QSize(80, 80))
        self.button1.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button1, 0, 0, 1, 1)

        self.button2 = QPushButton(self.frame_7)
        self.button2.setObjectName(u"button2")
        sizePolicy1.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy1)
        self.button2.setMinimumSize(QSize(80, 80))
        self.button2.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button2, 0, 1, 1, 1)

        self.button3 = QPushButton(self.frame_7)
        self.button3.setObjectName(u"button3")
        sizePolicy1.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy1)
        self.button3.setMinimumSize(QSize(80, 80))
        self.button3.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button3, 0, 2, 1, 1)

        self.button4 = QPushButton(self.frame_7)
        self.button4.setObjectName(u"button4")
        sizePolicy1.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy1)
        self.button4.setMinimumSize(QSize(80, 80))
        self.button4.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button4, 1, 0, 1, 1)

        self.button5 = QPushButton(self.frame_7)
        self.button5.setObjectName(u"button5")
        sizePolicy1.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy1)
        self.button5.setMinimumSize(QSize(80, 80))
        self.button5.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button5, 1, 1, 1, 1)

        self.button6 = QPushButton(self.frame_7)
        self.button6.setObjectName(u"button6")
        sizePolicy1.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy1)
        self.button6.setMinimumSize(QSize(80, 80))
        self.button6.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button6, 1, 2, 1, 1)

        self.button7 = QPushButton(self.frame_7)
        self.button7.setObjectName(u"button7")
        sizePolicy1.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy1)
        self.button7.setMinimumSize(QSize(80, 80))
        self.button7.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button7, 2, 0, 1, 1)

        self.button8 = QPushButton(self.frame_7)
        self.button8.setObjectName(u"button8")
        sizePolicy1.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy1)
        self.button8.setMinimumSize(QSize(80, 80))
        self.button8.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button8, 2, 1, 1, 1)

        self.button9 = QPushButton(self.frame_7)
        self.button9.setObjectName(u"button9")
        sizePolicy1.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy1)
        self.button9.setMinimumSize(QSize(80, 80))
        self.button9.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button9, 2, 2, 1, 1)

        self.button0 = QPushButton(self.frame_7)
        self.button0.setObjectName(u"button0")
        sizePolicy1.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy1)
        self.button0.setMinimumSize(QSize(80, 80))
        self.button0.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.button0, 3, 0, 1, 1)

        self.buttonClear = QPushButton(self.frame_7)
        self.buttonClear.setObjectName(u"buttonClear")
        self.buttonClear.setMinimumSize(QSize(170, 80))
        self.buttonClear.setMaximumSize(QSize(170, 80))

        self.gridLayout_5.addWidget(self.buttonClear, 3, 1, 1, 2)


        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.buttonNext = QPushButton(self.frame_7)
        self.buttonNext.setObjectName(u"buttonNext")
        self.buttonNext.setMinimumSize(QSize(170, 60))
        self.buttonNext.setMaximumSize(QSize(170, 60))

        self.gridLayout_6.addWidget(self.buttonNext, 0, 0, 1, 1)

        self.buttonBefore = QPushButton(self.frame_7)
        self.buttonBefore.setObjectName(u"buttonBefore")
        self.buttonBefore.setMinimumSize(QSize(170, 60))
        self.buttonBefore.setMaximumSize(QSize(170, 60))

        self.gridLayout_6.addWidget(self.buttonBefore, 1, 0, 1, 1)

        self.buttonModify = QPushButton(self.frame_7)
        self.buttonModify.setObjectName(u"buttonModify")
        self.buttonModify.setMinimumSize(QSize(170, 130))
        self.buttonModify.setMaximumSize(QSize(170, 130))
        self.buttonModify.setAutoFillBackground(True)
        self.buttonModify.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.buttonModify, 2, 0, 1, 1)

        self.buttonSet = QPushButton(self.frame_7)
        self.buttonSet.setObjectName(u"buttonSet")
        self.buttonSet.setMinimumSize(QSize(170, 80))
        self.buttonSet.setMaximumSize(QSize(170, 80))

        self.gridLayout_6.addWidget(self.buttonSet, 3, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_7, 2, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.labelCarNumber = QLabel(self.frame_3)
        self.labelCarNumber.setObjectName(u"labelCarNumber")
        self.labelCarNumber.setMinimumSize(QSize(252, 130))
        font1 = QFont()
        font1.setPointSize(75)
        self.labelCarNumber.setFont(font1)
        self.labelCarNumber.setLayoutDirection(Qt.LeftToRight)
        self.labelCarNumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelCarNumber, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 2, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(340, 340))
        self.frame_5.setMaximumSize(QSize(340, 340))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_3.setFont(font2)

        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)

        self.gridLayout_8.addWidget(self.pushButton, 1, 2, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_8.addWidget(self.label_5, 2, 0, 1, 1)

        self.labelCurrentCar = QLabel(self.frame_5)
        self.labelCurrentCar.setObjectName(u"labelCurrentCar")
        self.labelCurrentCar.setFont(font2)

        self.gridLayout_8.addWidget(self.labelCurrentCar, 1, 1, 1, 1, Qt.AlignRight)

        self.labelCurrentPallet = QLabel(self.frame_5)
        self.labelCurrentPallet.setObjectName(u"labelCurrentPallet")
        self.labelCurrentPallet.setFont(font2)

        self.gridLayout_8.addWidget(self.labelCurrentPallet, 2, 1, 1, 1, Qt.AlignRight)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font2)

        self.gridLayout_8.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(69)
        self.label_7.setFont(font3)

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 3, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(340, 210))
        self.frame_4.setMaximumSize(QSize(16777215, 210))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.gridLayout_9 = QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setFont(font3)

        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1, Qt.AlignHCenter)


        self.retranslateUi(changeCarNumber)

        QMetaObject.connectSlotsByName(changeCarNumber)
    # setupUi

    def retranslateUi(self, changeCarNumber):
        changeCarNumber.setWindowTitle(QCoreApplication.translate("changeCarNumber", u"Form", None))
        self.buttonReturn.setText(QCoreApplication.translate("changeCarNumber", u"<", None))
        self.label.setText(QCoreApplication.translate("changeCarNumber", u"\ucc28\ub7c9 \ubc88\ud638 \uc218\uc815 \ud654\uba74", None))
        self.button1.setText(QCoreApplication.translate("changeCarNumber", u"1", None))
        self.button2.setText(QCoreApplication.translate("changeCarNumber", u"2", None))
        self.button3.setText(QCoreApplication.translate("changeCarNumber", u"3", None))
        self.button4.setText(QCoreApplication.translate("changeCarNumber", u"4", None))
        self.button5.setText(QCoreApplication.translate("changeCarNumber", u"5", None))
        self.button6.setText(QCoreApplication.translate("changeCarNumber", u"6", None))
        self.button7.setText(QCoreApplication.translate("changeCarNumber", u"7", None))
        self.button8.setText(QCoreApplication.translate("changeCarNumber", u"8", None))
        self.button9.setText(QCoreApplication.translate("changeCarNumber", u"9", None))
        self.button0.setText(QCoreApplication.translate("changeCarNumber", u"0", None))
        self.buttonClear.setText(QCoreApplication.translate("changeCarNumber", u"\uc815\uc815", None))
        self.buttonNext.setText(QCoreApplication.translate("changeCarNumber", u"\ub2e4\uc74c", None))
        self.buttonBefore.setText(QCoreApplication.translate("changeCarNumber", u"\uc774\uc804", None))
        self.buttonModify.setText(QCoreApplication.translate("changeCarNumber", u"\uc218\uc815", None))
        self.buttonSet.setText(QCoreApplication.translate("changeCarNumber", u"\uc644\ub8cc", None))
        self.labelCarNumber.setText("")
        self.label_3.setText(QCoreApplication.translate("changeCarNumber", u"\ucc28\ub7c9 \ubc88\ud638.", None))
        self.pushButton.setText(QCoreApplication.translate("changeCarNumber", u"\uc801  \uc7ac", None))
        self.label_5.setText(QCoreApplication.translate("changeCarNumber", u"\ud30c\ub808\ud2b8 \ubc88\ud638.", None))
        self.labelCurrentCar.setText(QCoreApplication.translate("changeCarNumber", u"XX", None))
        self.labelCurrentPallet.setText(QCoreApplication.translate("changeCarNumber", u"XX", None))
        self.pushButton_2.setText(QCoreApplication.translate("changeCarNumber", u"\uc0ad  \uc81c", None))
        self.label_7.setText(QCoreApplication.translate("changeCarNumber", u"IMG", None))
        self.label_8.setText(QCoreApplication.translate("changeCarNumber", u"IMG", None))
    # retranslateUi


