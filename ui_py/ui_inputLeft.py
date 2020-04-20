# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputLeft.ui'
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


class Ui_inputLeft(object):
    def setupUi(self, inputLeft):
        if inputLeft.objectName():
            inputLeft.setObjectName(u"inputLeft")
        inputLeft.resize(400, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(inputLeft.sizePolicy().hasHeightForWidth())
        inputLeft.setSizePolicy(sizePolicy)
        inputLeft.setMinimumSize(QSize(400, 100))
        inputLeft.setMaximumSize(QSize(400, 100))
        inputLeft.setFrameShape(QFrame.NoFrame)
        inputLeft.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(inputLeft)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFloor = QFrame(inputLeft)
        self.leftFloor.setObjectName(u"leftFloor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftFloor.sizePolicy().hasHeightForWidth())
        self.leftFloor.setSizePolicy(sizePolicy1)
        self.leftFloor.setMinimumSize(QSize(400, 80))
        self.leftFloor.setMaximumSize(QSize(400, 80))
        self.leftFloor.setAutoFillBackground(True)
        self.leftFloor.setFrameShape(QFrame.NoFrame)
        self.leftFloor.setFrameShadow(QFrame.Raised)
        self._2 = QGridLayout(self.leftFloor)
        self._2.setSpacing(0)
        self._2.setObjectName(u"_2")
        self._2.setSizeConstraint(QLayout.SetMinimumSize)
        self._2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.leftFloor)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self._2.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.leftFloor, 0, 0, 1, 1)


        self.retranslateUi(inputLeft)

        QMetaObject.connectSlotsByName(inputLeft)
    # setupUi

    def retranslateUi(self, inputLeft):
        inputLeft.setWindowTitle(QCoreApplication.translate("inputLeft", u"Frame", None))
        self.label.setText(QCoreApplication.translate("inputLeft", u"\uc9c4\uc785\uce35 >>", None))
    # retranslateUi


