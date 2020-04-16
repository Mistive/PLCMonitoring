# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monitor.ui'
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


class Ui_monitor(object):
    def setupUi(self, monitor):
        if monitor.objectName():
            monitor.setObjectName(u"monitor")
        monitor.resize(1460, 857)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(monitor.sizePolicy().hasHeightForWidth())
        monitor.setSizePolicy(sizePolicy)
        monitor.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(monitor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, -1)
        self.frameInfo = QFrame(self.groupBox)
        self.frameInfo.setObjectName(u"frameInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frameInfo.sizePolicy().hasHeightForWidth())
        self.frameInfo.setSizePolicy(sizePolicy2)
        self.frameInfo.setFrameShape(QFrame.StyledPanel)
        self.frameInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frameInfo)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.BoxInfo = QGroupBox(self.frameInfo)
        self.BoxInfo.setObjectName(u"BoxInfo")
        self.BoxInfo.setMinimumSize(QSize(420, 300))
        self.BoxInfo.setMaximumSize(QSize(420, 300))
        self.gridLayout_7 = QGridLayout(self.BoxInfo)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.BoxInfo)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.labelParkingNum = QLabel(self.BoxInfo)
        self.labelParkingNum.setObjectName(u"labelParkingNum")
        font1 = QFont()
        font1.setPointSize(13)
        self.labelParkingNum.setFont(font1)

        self.horizontalLayout_3.addWidget(self.labelParkingNum)

        self.label_8 = QLabel(self.BoxInfo)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.labelEmptyNum = QLabel(self.BoxInfo)
        self.labelEmptyNum.setObjectName(u"labelEmptyNum")
        self.labelEmptyNum.setFont(font1)

        self.horizontalLayout_3.addWidget(self.labelEmptyNum)


        self.gridLayout_7.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_10 = QLabel(self.BoxInfo)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_6.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QLabel(self.BoxInfo)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_6.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_12 = QLabel(self.BoxInfo)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_6.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_13 = QLabel(self.BoxInfo)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_6.addWidget(self.label_13, 0, 3, 1, 1)

        self.labelSedanParkingNum = QLabel(self.BoxInfo)
        self.labelSedanParkingNum.setObjectName(u"labelSedanParkingNum")
        self.labelSedanParkingNum.setFont(font1)

        self.gridLayout_6.addWidget(self.labelSedanParkingNum, 1, 0, 1, 1)

        self.labelSedanEmptyNum = QLabel(self.BoxInfo)
        self.labelSedanEmptyNum.setObjectName(u"labelSedanEmptyNum")
        self.labelSedanEmptyNum.setFont(font1)

        self.gridLayout_6.addWidget(self.labelSedanEmptyNum, 1, 1, 1, 1)

        self.labelRVParkingNum = QLabel(self.BoxInfo)
        self.labelRVParkingNum.setObjectName(u"labelRVParkingNum")
        self.labelRVParkingNum.setFont(font1)

        self.gridLayout_6.addWidget(self.labelRVParkingNum, 1, 2, 1, 1)

        self.labelRVEmptyNum = QLabel(self.BoxInfo)
        self.labelRVEmptyNum.setObjectName(u"labelRVEmptyNum")
        self.labelRVEmptyNum.setFont(font1)

        self.gridLayout_6.addWidget(self.labelRVEmptyNum, 1, 3, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_18 = QLabel(self.BoxInfo)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout.addWidget(self.label_18)

        self.label_19 = QLabel(self.BoxInfo)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout.addWidget(self.label_19)

        self.label_20 = QLabel(self.BoxInfo)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout.addWidget(self.label_20)

        self.label_21 = QLabel(self.BoxInfo)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.verticalLayout.addWidget(self.label_21)

        self.label_22 = QLabel(self.BoxInfo)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.verticalLayout.addWidget(self.label_22)

        self.label_23 = QLabel(self.BoxInfo)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.verticalLayout.addWidget(self.label_23)


        self.gridLayout_7.addLayout(self.verticalLayout, 2, 0, 1, 1)


        self.gridLayout_8.addWidget(self.BoxInfo, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.InputButton = QGroupBox(self.frameInfo)
        self.InputButton.setObjectName(u"InputButton")
        self.InputButton.setMinimumSize(QSize(420, 400))
        self.InputButton.setMaximumSize(QSize(420, 400))
        self.InputButton.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.gridLayout_2 = QGridLayout(self.InputButton)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.label = QLabel(self.InputButton)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(50, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.labelINSell = QLabel(self.InputButton)
        self.labelINSell.setObjectName(u"labelINSell")
        sizePolicy3.setHeightForWidth(self.labelINSell.sizePolicy().hasHeightForWidth())
        self.labelINSell.setSizePolicy(sizePolicy3)
        self.labelINSell.setMinimumSize(QSize(50, 20))
        self.labelINSell.setFont(font2)
        self.labelINSell.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelINSell, 0, 1, 1, 1)

        self.label_2 = QLabel(self.InputButton)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(50, 20))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.labelOUTSell = QLabel(self.InputButton)
        self.labelOUTSell.setObjectName(u"labelOUTSell")
        sizePolicy3.setHeightForWidth(self.labelOUTSell.sizePolicy().hasHeightForWidth())
        self.labelOUTSell.setSizePolicy(sizePolicy3)
        self.labelOUTSell.setMinimumSize(QSize(50, 20))
        self.labelOUTSell.setFont(font2)
        self.labelOUTSell.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelOUTSell, 1, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.InputButton)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(50, 20))
        font3 = QFont()
        font3.setPointSize(14)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.labelCNum = QLabel(self.InputButton)
        self.labelCNum.setObjectName(u"labelCNum")
        sizePolicy3.setHeightForWidth(self.labelCNum.sizePolicy().hasHeightForWidth())
        self.labelCNum.setSizePolicy(sizePolicy3)
        self.labelCNum.setMinimumSize(QSize(50, 20))
        font4 = QFont()
        font4.setPointSize(25)
        self.labelCNum.setFont(font4)
        self.labelCNum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelCNum)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.button2 = QPushButton(self.InputButton)
        self.button2.setObjectName(u"button2")
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setMinimumSize(QSize(70, 70))
        self.button2.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button2, 0, 1, 1, 1)

        self.button3 = QPushButton(self.InputButton)
        self.button3.setObjectName(u"button3")
        sizePolicy.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy)
        self.button3.setMinimumSize(QSize(70, 70))
        self.button3.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button3, 0, 2, 1, 1)

        self.buttonIn = QPushButton(self.InputButton)
        self.buttonIn.setObjectName(u"buttonIn")
        self.buttonIn.setMinimumSize(QSize(150, 100))
        self.buttonIn.setMaximumSize(QSize(130, 100))

        self.gridLayout_4.addWidget(self.buttonIn, 0, 3, 2, 1)

        self.button4 = QPushButton(self.InputButton)
        self.button4.setObjectName(u"button4")
        sizePolicy.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy)
        self.button4.setMinimumSize(QSize(70, 70))
        self.button4.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button4, 1, 0, 2, 1)

        self.button5 = QPushButton(self.InputButton)
        self.button5.setObjectName(u"button5")
        sizePolicy.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy)
        self.button5.setMinimumSize(QSize(70, 70))
        self.button5.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button5, 1, 1, 2, 1)

        self.button6 = QPushButton(self.InputButton)
        self.button6.setObjectName(u"button6")
        sizePolicy.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy)
        self.button6.setMinimumSize(QSize(70, 70))
        self.button6.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button6, 1, 2, 2, 1)

        self.buttonOut = QPushButton(self.InputButton)
        self.buttonOut.setObjectName(u"buttonOut")
        self.buttonOut.setMinimumSize(QSize(150, 100))
        self.buttonOut.setMaximumSize(QSize(130, 100))

        self.gridLayout_4.addWidget(self.buttonOut, 2, 3, 2, 1)

        self.button7 = QPushButton(self.InputButton)
        self.button7.setObjectName(u"button7")
        sizePolicy.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy)
        self.button7.setMinimumSize(QSize(70, 70))
        self.button7.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button7, 3, 0, 1, 1)

        self.button8 = QPushButton(self.InputButton)
        self.button8.setObjectName(u"button8")
        sizePolicy.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy)
        self.button8.setMinimumSize(QSize(70, 70))
        self.button8.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button8, 3, 1, 1, 1)

        self.button9 = QPushButton(self.InputButton)
        self.button9.setObjectName(u"button9")
        sizePolicy.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy)
        self.button9.setMinimumSize(QSize(70, 70))
        self.button9.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button9, 3, 2, 1, 1)

        self.button0 = QPushButton(self.InputButton)
        self.button0.setObjectName(u"button0")
        sizePolicy.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy)
        self.button0.setMinimumSize(QSize(70, 70))
        self.button0.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button0, 4, 0, 1, 1)

        self.buttonClear = QPushButton(self.InputButton)
        self.buttonClear.setObjectName(u"buttonClear")
        self.buttonClear.setMinimumSize(QSize(150, 70))
        self.buttonClear.setMaximumSize(QSize(130, 70))

        self.gridLayout_4.addWidget(self.buttonClear, 4, 1, 1, 2)

        self.buttonSet = QPushButton(self.InputButton)
        self.buttonSet.setObjectName(u"buttonSet")
        self.buttonSet.setMinimumSize(QSize(150, 70))
        self.buttonSet.setMaximumSize(QSize(130, 70))

        self.gridLayout_4.addWidget(self.buttonSet, 4, 3, 1, 1)

        self.button1 = QPushButton(self.InputButton)
        self.button1.setObjectName(u"button1")
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setMinimumSize(QSize(70, 70))
        self.button1.setMaximumSize(QSize(70, 70))

        self.gridLayout_4.addWidget(self.button1, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 0, 1, 1)


        self.gridLayout_8.addWidget(self.InputButton, 3, 1, 1, 1)

        self.frame = QFrame(self.frameInfo)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setMinimumSize(QSize(50, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(5)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_9.setVerticalSpacing(6)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelConnectCheck = QLabel(self.frame)
        self.labelConnectCheck.setObjectName(u"labelConnectCheck")
        self.labelConnectCheck.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.labelConnectCheck)

        self.buttonConnect = QPushButton(self.frame)
        self.buttonConnect.setObjectName(u"buttonConnect")
        sizePolicy1.setHeightForWidth(self.buttonConnect.sizePolicy().hasHeightForWidth())
        self.buttonConnect.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.buttonConnect)


        self.gridLayout_9.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frameInfo, 5, 2, 1, 1)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setMinimumSize(QSize(1000, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 998, 826))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frameMonitor = QFrame(self.scrollAreaWidgetContents)
        self.frameMonitor.setObjectName(u"frameMonitor")
        self.frameMonitor.setFrameShape(QFrame.Box)
        self.frameMonitor.setFrameShadow(QFrame.Plain)
        self.gridLayout_11 = QGridLayout(self.frameMonitor)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.frameCenter = QFrame(self.frameMonitor)
        self.frameCenter.setObjectName(u"frameCenter")
        sizePolicy.setHeightForWidth(self.frameCenter.sizePolicy().hasHeightForWidth())
        self.frameCenter.setSizePolicy(sizePolicy)
        self.frameCenter.setMinimumSize(QSize(0, 0))
        self.frameCenter.setFrameShape(QFrame.Box)
        self.frameCenter.setLineWidth(3)

        self.gridLayout_11.addWidget(self.frameCenter, 0, 2, 1, 1)

        self.frameLeft = QFrame(self.frameMonitor)
        self.frameLeft.setObjectName(u"frameLeft")
        sizePolicy.setHeightForWidth(self.frameLeft.sizePolicy().hasHeightForWidth())
        self.frameLeft.setSizePolicy(sizePolicy)
        self.frameLeft.setMinimumSize(QSize(0, 0))
        self.frameLeft.setLayoutDirection(Qt.LeftToRight)
        self.frameLeft.setFrameShape(QFrame.NoFrame)

        self.gridLayout_11.addWidget(self.frameLeft, 0, 1, 1, 1)

        self.frameRight = QFrame(self.frameMonitor)
        self.frameRight.setObjectName(u"frameRight")
        sizePolicy.setHeightForWidth(self.frameRight.sizePolicy().hasHeightForWidth())
        self.frameRight.setSizePolicy(sizePolicy)
        self.frameRight.setMinimumSize(QSize(0, 0))
        self.frameRight.setFrameShape(QFrame.NoFrame)

        self.gridLayout_11.addWidget(self.frameRight, 0, 3, 1, 1)


        self.gridLayout_10.addWidget(self.frameMonitor, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 5, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        monitor.setCentralWidget(self.centralwidget)

        self.retranslateUi(monitor)

        QMetaObject.connectSlotsByName(monitor)
    # setupUi

    def retranslateUi(self, monitor):
        monitor.setWindowTitle(QCoreApplication.translate("monitor", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.BoxInfo.setTitle("")
        self.label_6.setText(QCoreApplication.translate("monitor", u"\uc804\uccb4 \uc8fc\ucc28", None))
        self.labelParkingNum.setText(QCoreApplication.translate("monitor", u"48", None))
        self.label_8.setText(QCoreApplication.translate("monitor", u"\uc804\uccb4 \uacf5\ucc28", None))
        self.labelEmptyNum.setText(QCoreApplication.translate("monitor", u"48", None))
        self.label_10.setText(QCoreApplication.translate("monitor", u"\uc77c\ubc18\uc8fc\ucc28", None))
        self.label_11.setText(QCoreApplication.translate("monitor", u"\uc77c\ubc18\uacf5\ucc28", None))
        self.label_12.setText(QCoreApplication.translate("monitor", u"RV\uc8fc\ucc28", None))
        self.label_13.setText(QCoreApplication.translate("monitor", u"RV\uacf5\ucc28", None))
#if QT_CONFIG(tooltip)
        self.labelSedanParkingNum.setToolTip(QCoreApplication.translate("monitor", u"<html><head/><body><p>D0072</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelSedanParkingNum.setText(QCoreApplication.translate("monitor", u"48", None))
#if QT_CONFIG(whatsthis)
        self.labelSedanEmptyNum.setWhatsThis(QCoreApplication.translate("monitor", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.labelSedanEmptyNum.setText(QCoreApplication.translate("monitor", u"48", None))
        self.labelRVParkingNum.setText(QCoreApplication.translate("monitor", u"48", None))
        self.labelRVEmptyNum.setText(QCoreApplication.translate("monitor", u"48", None))
        self.label_18.setText(QCoreApplication.translate("monitor", u"\uc2dc\uc2a4\ud15c \uc0c1\ud0dc \uba54\uc2dc\uc9c0", None))
        self.label_19.setText(QCoreApplication.translate("monitor", u"\ud1b5\uc2e0 \uc548\ub428", None))
        self.label_20.setText(QCoreApplication.translate("monitor", u"\ub3d9\uc791 \uc0c1\ud0dc \uba54\uc2dc\uc9c0", None))
        self.label_21.setText(QCoreApplication.translate("monitor", u"\ud1b5\uc2e0 \uc548\ub428", None))
        self.label_22.setText(QCoreApplication.translate("monitor", u"\uc5d0\ub7ec \uc0c1\ud0dc \uba54\uc2dc\uc9c0", None))
        self.label_23.setText(QCoreApplication.translate("monitor", u"\ud1b5\uc2e0 \uc548\ub428", None))
        self.label.setText(QCoreApplication.translate("monitor", u"\uc801\uc7ac \ud30c\ub81b", None))
        self.labelINSell.setText(QCoreApplication.translate("monitor", u"000", None))
        self.label_2.setText(QCoreApplication.translate("monitor", u"\ucd9c\uace0 \ud30c\ub81b", None))
        self.labelOUTSell.setText(QCoreApplication.translate("monitor", u"000", None))
        self.label_5.setText(QCoreApplication.translate("monitor", u"\ucc28\ub7c9\ubc88\ud638", None))
        self.labelCNum.setText(QCoreApplication.translate("monitor", u"0000", None))
        self.button2.setText(QCoreApplication.translate("monitor", u"2", None))
        self.button3.setText(QCoreApplication.translate("monitor", u"3", None))
        self.buttonIn.setText(QCoreApplication.translate("monitor", u"\uc785\uace0", None))
        self.button4.setText(QCoreApplication.translate("monitor", u"4", None))
        self.button5.setText(QCoreApplication.translate("monitor", u"5", None))
        self.button6.setText(QCoreApplication.translate("monitor", u"6", None))
        self.buttonOut.setText(QCoreApplication.translate("monitor", u"\ucd9c\uace0", None))
        self.button7.setText(QCoreApplication.translate("monitor", u"7", None))
        self.button8.setText(QCoreApplication.translate("monitor", u"8", None))
        self.button9.setText(QCoreApplication.translate("monitor", u"9", None))
        self.button0.setText(QCoreApplication.translate("monitor", u"0", None))
        self.buttonClear.setText(QCoreApplication.translate("monitor", u"\uc815\uc815", None))
        self.buttonSet.setText(QCoreApplication.translate("monitor", u"\uc644\ub8cc", None))
        self.button1.setText(QCoreApplication.translate("monitor", u"1", None))
        self.labelConnectCheck.setText(QCoreApplication.translate("monitor", u"Disconnected", None))
        self.buttonConnect.setText(QCoreApplication.translate("monitor", u"\uc5f0\uacb0 \ud558\uae30", None))
    # retranslateUi


