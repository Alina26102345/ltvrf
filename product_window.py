from PyQt5.QtWidgets import *

class ProductWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Список товаров"
        )

        layout = QVBoxLayout()

        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "Поиск..."
        )

        self.table = QTableWidget()

        layout.addWidget(self.search)

        layout.addWidget(self.table)

        self.setLayout(layout)