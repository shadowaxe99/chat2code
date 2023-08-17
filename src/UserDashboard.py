from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class UserDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('User Dashboard')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel('User Dashboard')
        self.layout.addWidget(self.label)