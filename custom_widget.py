from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QComboBox, QSpinBox


class CustomQCB(QComboBox):
    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()


class CustomQSB(QSpinBox):
    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()
