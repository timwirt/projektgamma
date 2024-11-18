# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ein_auszahlen.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Ein_Auszahlen(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 20, 71, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 20, 381, 41))
        self.label_2.setFont(font)
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(160, 80, 116, 22))
        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(160, 120, 116, 22))
        self.radioButton_3 = QRadioButton(Dialog)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(160, 160, 116, 22))
        self.radioButton_4 = QRadioButton(Dialog)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(160, 200, 141, 22))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 240, 121, 29))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 280, 121, 29))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ein-/Auszahlen", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Coins:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"0\u00a7", None))

        self.radioButton.setText(QCoreApplication.translate("Dialog", u"0\u00a7", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"100\u00a7", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"250\u00a7", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"500\u00a7", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Fertig", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Zurück", None))
    # retranslateUi

