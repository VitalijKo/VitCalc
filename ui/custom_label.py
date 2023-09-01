from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import pyqtSignal


class CustomLabel(QLabel):
    textChanged = pyqtSignal()

    def setText(self, text):
        super().setText(text)
        
        self.textChanged.emit()
