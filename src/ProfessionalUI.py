from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit


class ProfessionalUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Professional and Engaging User Interface')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_area = QTextEdit()
        self.layout.addWidget(self.text_area)

        self.text_input = QLineEdit()
        self.layout.addWidget(self.text_input)

        self.send_button = QPushButton('Send')
        self.layout.addWidget(self.send_button)

        self.send_button.clicked.connect(self.navigate_interface)

    def navigate_interface(self):
        message = self.text_input.text()
        self.text_area.append(message)
        self.text_input.clear()