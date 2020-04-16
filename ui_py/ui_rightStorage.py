# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rightStorage.ui'
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


class Ui_rightStorage(object):
    def setupUi(self, rightStorage):
        if rightStorage.objectName():
            rightStorage.setObjectName(u"rightStorage")
        rightStorage.resize(102, 32)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rightStorage.sizePolicy().hasHeightForWidth())
        rightStorage.setSizePolicy(sizePolicy)
        rightStorage.setMinimumSize(QSize(100, 30))
        rightStorage.setMaximumSize(QSize(102, 32))
        rightStorage.setFrameShape(QFrame.StyledPanel)
        rightStorage.setFrameShadow(QFrame.Raised)
        rightStorage.setLineWidth(3)
        self.gridLayout = QGridLayout(rightStorage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.rightFloor = QFrame(rightStorage)
        self.rightFloor.setObjectName(u"rightFloor")
        sizePolicy.setHeightForWidth(self.rightFloor.sizePolicy().hasHeightForWidth())
        self.rightFloor.setSizePolicy(sizePolicy)
        self.rightFloor.setMinimumSize(QSize(100, 30))
        self.rightFloor.setMaximumSize(QSize(100, 30))
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

        self.gridLayout1.addWidget(self.labelCarImg, 0, 0, 1, 1)

        self.labelCarIdx = QLabel(self.rightFloor)
        self.labelCarIdx.setObjectName(u"labelCarIdx")
        self.labelCarIdx.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelCarIdx, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.rightFloor, 0, 0, 1, 1)


        self.retranslateUi(rightStorage)

        QMetaObject.connectSlotsByName(rightStorage)
    # setupUi

    def retranslateUi(self, rightStorage):
        rightStorage.setWindowTitle(QCoreApplication.translate("rightStorage", u"Frame", None))
        self.labelCarImg.setText(QCoreApplication.translate("rightStorage", u"img", None))
        self.labelCarIdx.setText(QCoreApplication.translate("rightStorage", u"<html><head/><body><p align=\"center\">Idx</p></body></html>", None))
    # retranslateUi


