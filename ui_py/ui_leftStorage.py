# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leftStorage.ui'
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


class Ui_leftStorage(object):
    def setupUi(self, leftStorage):
        if leftStorage.objectName():
            leftStorage.setObjectName(u"leftStorage")
        leftStorage.resize(102, 32)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(leftStorage.sizePolicy().hasHeightForWidth())
        leftStorage.setSizePolicy(sizePolicy)
        leftStorage.setMinimumSize(QSize(100, 30))
        leftStorage.setMaximumSize(QSize(102, 32))
        leftStorage.setLayoutDirection(Qt.RightToLeft)
        leftStorage.setFrameShape(QFrame.StyledPanel)
        leftStorage.setFrameShadow(QFrame.Raised)
        leftStorage.setLineWidth(3)
        self.gridLayout = QGridLayout(leftStorage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFloor = QFrame(leftStorage)
        self.leftFloor.setObjectName(u"leftFloor")
        sizePolicy.setHeightForWidth(self.leftFloor.sizePolicy().hasHeightForWidth())
        self.leftFloor.setSizePolicy(sizePolicy)
        self.leftFloor.setMinimumSize(QSize(100, 30))
        self.leftFloor.setMaximumSize(QSize(100, 30))
        self.leftFloor.setLayoutDirection(Qt.LeftToRight)
        self.leftFloor.setAutoFillBackground(True)
        self.leftFloor.setFrameShape(QFrame.Box)
        self.leftFloor.setFrameShadow(QFrame.Raised)
        self.gridLayout1 = QGridLayout(self.leftFloor)
        self.gridLayout1.setSpacing(0)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.labelCarIdx = QLabel(self.leftFloor)
        self.labelCarIdx.setObjectName(u"labelCarIdx")
        self.labelCarIdx.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarIdx, 0, 0, 1, 1)

        self.labelCarImg = QLabel(self.leftFloor)
        self.labelCarImg.setObjectName(u"labelCarImg")
        self.labelCarImg.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarImg, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.leftFloor, 0, 0, 1, 1)


        self.retranslateUi(leftStorage)

        QMetaObject.connectSlotsByName(leftStorage)
    # setupUi

    def retranslateUi(self, leftStorage):
        leftStorage.setWindowTitle(QCoreApplication.translate("leftStorage", u"Frame", None))
        self.labelCarIdx.setText(QCoreApplication.translate("leftStorage", u"<html><head/><body><p align=\"center\">Idx</p></body></html>", None))
        self.labelCarImg.setText(QCoreApplication.translate("leftStorage", u"img", None))
    # retranslateUi


