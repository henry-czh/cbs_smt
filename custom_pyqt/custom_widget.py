from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import time


class CustomQCB(QComboBox):
    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()


class CustomQSB(QSpinBox):
    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()

class QComboBox_czh(QComboBox):
    def __init__(self, parent=None):
        super(QComboBox_czh,self).__init__(parent)

    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()

class QSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super(QSpinBox,self).__init__(parent)

    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()

class ColoredTextBrowser(QTextBrowser):
    def __init__(self, parent=None):
        super(ColoredTextBrowser,self).__init__(parent)
        self.tips()

    def tips(self):
        # 获取当前文本光标
        cursor = self.textCursor()
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        # 创建文本字符格式，设置颜色
        char_format = QTextCharFormat()

        char_format.setForeground(QColor('blue'))
        # 在光标处应用字符格式
        cursor.setCharFormat(char_format)
        # 插入文本
        cursor.insertText('[%s]# ' % (t))

    def consel(self, text, color):
        # 获取当前文本光标
        cursor = self.textCursor()

        # 创建文本字符格式，设置颜色
        char_format = QTextCharFormat()

        char_format.setForeground(QColor(color))
        cursor.setCharFormat(char_format)
        cursor.insertText(text+'\n')

        self.tips()

        # 恢复默认字符格式
        cursor.setCharFormat(QTextCharFormat())

        # 每当文本内容更新时，滚动到底部
        cursor.movePosition(QTextCursor.End)
        self.setTextCursor(cursor)