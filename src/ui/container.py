from PyQt5.QtWidgets import QWidget, QVBoxLayout


class Container(QWidget):
    def __init__(self, parent=None):
        super(Container, self).__init__(parent)
        self.layout = QVBoxLayout(self)

    def add_widget(self, widget):
        self.layout.addWidget(widget)
