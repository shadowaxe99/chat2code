from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit


class AgentMovementUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Agent Movement UI')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_area = QTextEdit()
        self.layout.addWidget(self.text_area)

        self.text_input = QLineEdit()
        self.layout.addWidget(self.text_input)

        self.send_button = QPushButton('Move')
        self.layout.addWidget(self.send_button)

        self.send_button.clicked.connect(self.move_agent)

    def move_agent(self):
        direction = self.text_input.text()
        self.text_area.append(f'Moving agent {direction}')
        self.text_input.clear()