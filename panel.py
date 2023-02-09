# -*- coding: utf-8 -*-
import os
import sys

import HotKeys
import keyboard  # using module keyboard

# eslint-disable-next-line
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QLabel)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        lbl = QLabel('right', self)
        lbl.move(100,0)
        # lcd = QLCDNumber(self)
        # sld = QSlider(Qt.Horizontal, self)

        # vbox = QVBoxLayout()
        # vbox.addWidget(lcd)
        # vbox.addWidget(sld)

        # self.setLayout(vbox)
        # sld.valueChanged.connect(lcd.display)

        # window = QtWidgets.QWidget()
        desktop = QtWidgets.QApplication.desktop()
        self.setStyleSheet("background-color: #3b3b3b")

        # print("xw:", window.width(), "yw:", window.height(), "xd:", desktop.width(), "yd:", desktop.height(), )
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # окно без рамки
        
        
        self.setGeometry(0, 0, desktop.width(), 30)
        self.setWindowTitle('Signal & slot')
        self.show()
        


if __name__ == '__main__':
    keyboard.add_hotkey("ctrl+alt+t", lambda: HotKeys.console())
    keyboard.add_hotkey("home", lambda: HotKeys.closeExp())
    keyboard.add_hotkey("win", lambda: HotKeys.startExp())
    keyboard.add_hotkey("end", lambda: QApplication.quit()) #taskkill -f -im explorer.exe

    keyboard.add_abbreviation("@em", "ivantrofimov2001@yandex.ru")

    app = QApplication(sys.argv)

    ex = Example()
    sys.exit(app.exec_())
