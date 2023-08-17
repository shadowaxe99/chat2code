from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton


class SearchBar(QWidget):
    def __init__(self, parent=None):
        super(SearchBar, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.search_input = QLineEdit(self)
        self.search_button = QPushButton('Search', self)
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.search_button)
