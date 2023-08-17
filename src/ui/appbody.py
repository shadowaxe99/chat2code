from PyQt5.QtWidgets import QWidget, QVBoxLayout


class AppBody(QWidget):
    def __init__(self, parent=None):
        super(AppBody, self).__init__(parent)
        self.layout = QVBoxLayout(self)

    def add_widget(self, widget):
        self.layout.addWidget(widget)
