# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rightCar.ui'
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


class Ui_rightCar(object):
    def setupUi(self, rightCar):
        if rightCar.objectName():
            rightCar.setObjectName(u"rightCar")
        rightCar.resize(202, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rightCar.sizePolicy().hasHeightForWidth())
        rightCar.setSizePolicy(sizePolicy)
        rightCar.setMinimumSize(QSize(200, 100))
        rightCar.setMaximumSize(QSize(202, 100))
        rightCar.setFrameShape(QFrame.StyledPanel)
        rightCar.setFrameShadow(QFrame.Raised)
        rightCar.setLineWidth(3)
        self.gridLayout = QGridLayout(rightCar)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.rightFloor = QFrame(rightCar)
        self.rightFloor.setObjectName(u"rightFloor")
        sizePolicy.setHeightForWidth(self.rightFloor.sizePolicy().hasHeightForWidth())
        self.rightFloor.setSizePolicy(sizePolicy)
        self.rightFloor.setMinimumSize(QSize(200, 80))
        self.rightFloor.setMaximumSize(QSize(200, 80))
        self.rightFloor.setAutoFillBackground(True)
        self.rightFloor.setFrameShape(QFrame.Box)
        self.rightFloor.setFrameShadow(QFrame.Raised)
        self.gridLayout1 = QGridLayout(self.rightFloor)
        self.gridLayout1.setSpacing(0)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.labelCarImg = QLabel(self.rightFloor)
        self.labelCarImg.setObjectName(u"labelCarImg")
        self.labelCarImg.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarImg, 0, 2, 1, 1)

        self.labelCarNum = QLabel(self.rightFloor)
        self.labelCarNum.setObjectName(u"labelCarNum")
        self.labelCarNum.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarNum, 0, 0, 1, 1)

        self.labelCarIdx = QLabel(self.rightFloor)
        self.labelCarIdx.setObjectName(u"labelCarIdx")
        self.labelCarIdx.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarIdx, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.rightFloor, 0, 0, 1, 1)


        self.retranslateUi(rightCar)

        QMetaObject.connectSlotsByName(rightCar)
    # setupUi

    def retranslateUi(self, rightCar):
        rightCar.setWindowTitle(QCoreApplication.translate("rightCar", u"Frame", None))
        self.labelCarImg.setText(QCoreApplication.translate("rightCar", u"XXXX", None))
        self.labelCarNum.setText(QCoreApplication.translate("rightCar", u"\ucc28\ub7c9 \uc774\ubbf8\uc9c0", None))
        self.labelCarIdx.setText(QCoreApplication.translate("rightCar", u"<html><head/><body><p align=\"center\">\uc2b9\uc6a9</p><p align=\"center\">123</p></body></html>", None))
    # retranslateUi


