# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leftCar.ui'
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


class Ui_leftCar(object):
    def setupUi(self, leftCar):
        if leftCar.objectName():
            leftCar.setObjectName(u"leftCar")
        leftCar.resize(202, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(leftCar.sizePolicy().hasHeightForWidth())
        leftCar.setSizePolicy(sizePolicy)
        leftCar.setMinimumSize(QSize(200, 100))
        leftCar.setMaximumSize(QSize(202, 100))
        leftCar.setLayoutDirection(Qt.RightToLeft)
        leftCar.setFrameShape(QFrame.StyledPanel)
        leftCar.setFrameShadow(QFrame.Raised)
        leftCar.setLineWidth(3)
        self.gridLayout = QGridLayout(leftCar)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFloor = QFrame(leftCar)
        self.leftFloor.setObjectName(u"leftFloor")
        sizePolicy.setHeightForWidth(self.leftFloor.sizePolicy().hasHeightForWidth())
        self.leftFloor.setSizePolicy(sizePolicy)
        self.leftFloor.setMinimumSize(QSize(200, 80))
        self.leftFloor.setMaximumSize(QSize(200, 80))
        self.leftFloor.setLayoutDirection(Qt.LeftToRight)
        self.leftFloor.setAutoFillBackground(True)
        self.leftFloor.setFrameShape(QFrame.Box)
        self.leftFloor.setFrameShadow(QFrame.Raised)
        self.gridLayout1 = QGridLayout(self.leftFloor)
        self.gridLayout1.setSpacing(0)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.labelCarImg = QLabel(self.leftFloor)
        self.labelCarImg.setObjectName(u"labelCarImg")
        self.labelCarImg.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarImg, 0, 2, 1, 1)

        self.labelCarNum = QLabel(self.leftFloor)
        self.labelCarNum.setObjectName(u"labelCarNum")
        self.labelCarNum.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarNum, 0, 0, 1, 1)

        self.labelCarIdx = QLabel(self.leftFloor)
        self.labelCarIdx.setObjectName(u"labelCarIdx")
        self.labelCarIdx.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarIdx, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.leftFloor, 0, 0, 1, 1)


        self.retranslateUi(leftCar)

        QMetaObject.connectSlotsByName(leftCar)
    # setupUi

    def retranslateUi(self, leftCar):
        leftCar.setWindowTitle(QCoreApplication.translate("leftCar", u"Frame", None))
        self.labelCarImg.setText(QCoreApplication.translate("leftCar", u"\ucc28\ub7c9 \uc774\ubbf8\uc9c0", None))
        self.labelCarNum.setText(QCoreApplication.translate("leftCar", u"XXXX", None))
        self.labelCarIdx.setText(QCoreApplication.translate("leftCar", u"<html><head/><body><p align=\"center\">\uc2b9\uc6a9</p><p align=\"center\">123</p></body></html>", None))
    # retranslateUi


