# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ARES_GUI.ui'
##
# Created by: Qt User Interface Compiler version 6.8.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 710)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Display = QLabel(self.centralwidget)
        self.Display.setObjectName(u"Display")
        self.Display.setGeometry(QRect(370, 180, 361, 241))
        self.Enter_button = QPushButton(self.centralwidget)
        self.Enter_button.setObjectName(u"Enter_button")
        self.Enter_button.setGeometry(QRect(530, 150, 75, 23))
        self.User_input = QLineEdit(self.centralwidget)
        self.User_input.setObjectName(u"User_input")
        self.User_input.setGeometry(QRect(400, 100, 331, 41))
        self.testing_gif = QLabel(self.centralwidget)
        self.testing_gif.setObjectName(u"testing_gif")
        self.testing_gif.setGeometry(QRect(40, 50, 241, 311))
        self.testing_gif.setPixmap(QPixmap(u"Assets/testing_gif.gif"))
        self.testing_gif.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.Display.setText(QCoreApplication.translate(
            "MainWindow", u"PENIS", None))
        self.Enter_button.setText(QCoreApplication.translate(
            "MainWindow", u"PushButton", None))
        self.testing_gif.setText("")
    # retranslateUi
