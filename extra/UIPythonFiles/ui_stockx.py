# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stockx.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_StockX(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1587, 1005)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 111, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-10, 130, 1601, 881))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1599, 879))
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 30, 1471, 701))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 30, 341, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1485, 30, 91, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_3.setFont(font1)
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setLineWidth(2)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1070, 30, 151, 51))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1240, 30, 151, 51))
        self.pushButton_2.setFont(font2)
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1480, 80, 101, 31))
        self.pushButton_3.setFont(font2)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(700, 10, 181, 61))
        font3 = QFont()
        font3.setFamilies([u"Purisa"])
        font3.setPointSize(28)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(True)
        self.label_5.setFont(font3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Stockx", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Coins:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"0\u00a7", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"tim_w", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Einzahlen", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Auszahlen", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Abmelden", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Stockx", None))
    # retranslateUi

