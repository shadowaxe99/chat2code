from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton


class FilterBar(QWidget):
    def __init__(self, parent=None):
        super(FilterBar, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.filter_input = QLineEdit(self)
        self.filter_button = QPushButton('Filter', self)
        self.layout.addWidget(self.filter_input)
        self.layout.addWidget(self.filter_button)
