from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class MainNav(QWidget):
    def __init__(self, parent=None):
        super(MainNav, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.home_button = QPushButton('Home', self)
        self.settings_button = QPushButton('Settings', self)
        self.layout.addWidget(self.home_button)
        self.layout.addWidget(self.settings_button)
