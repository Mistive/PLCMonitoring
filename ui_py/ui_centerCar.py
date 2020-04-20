# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'centerCar.ui'
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


class Ui_centerCar(object):
    def setupUi(self, centerCar):
        if centerCar.objectName():
            centerCar.setObjectName(u"centerCar")
        centerCar.resize(100, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(centerCar.sizePolicy().hasHeightForWidth())
        centerCar.setSizePolicy(sizePolicy)
        centerCar.setMinimumSize(QSize(100, 100))
        centerCar.setMaximumSize(QSize(100, 100))
        centerCar.setLayoutDirection(Qt.LeftToRight)
        centerCar.setFrameShape(QFrame.NoFrame)
        centerCar.setFrameShadow(QFrame.Raised)
        centerCar.setLineWidth(3)
        self.gridLayout = QGridLayout(centerCar)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.centerFloor = QFrame(centerCar)
        self.centerFloor.setObjectName(u"centerFloor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centerFloor.sizePolicy().hasHeightForWidth())
        self.centerFloor.setSizePolicy(sizePolicy1)
        self.centerFloor.setMinimumSize(QSize(80, 80))
        self.centerFloor.setMaximumSize(QSize(80, 80))
        self.centerFloor.setAutoFillBackground(True)
        self.centerFloor.setFrameShape(QFrame.NoFrame)
        self.centerFloor.setFrameShadow(QFrame.Raised)
        self.centerFloor.setLineWidth(1)
        self.gridLayout1 = QGridLayout(self.centerFloor)
        self.gridLayout1.setSpacing(0)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.labelCarImg = QLabel(self.centerFloor)
        self.labelCarImg.setObjectName(u"labelCarImg")
        self.labelCarImg.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarImg, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.centerFloor, 0, 0, 1, 1)


        self.retranslateUi(centerCar)

        QMetaObject.connectSlotsByName(centerCar)
    # setupUi

    def retranslateUi(self, centerCar):
        centerCar.setWindowTitle(QCoreApplication.translate("centerCar", u"Frame", None))
        self.labelCarImg.setText(QCoreApplication.translate("centerCar", u"\ucc28\ub7c9 \uc774\ubbf8\uc9c0", None))
    # retranslateUi


