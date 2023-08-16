from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class AnalyticsDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Analytics Dashboard')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel('Analytics Dashboard')
        self.layout.addWidget(self.label)