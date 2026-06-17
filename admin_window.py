from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

from services.product_service import load_products


class AdminWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Администратор"
        )

        self.resize(1500, 750)

        layout = QVBoxLayout()

        buttons = QHBoxLayout()

        add_btn = QPushButton(
            "Добавить"
        )

        edit_btn = QPushButton(
            "Редактировать"
        )

        delete_btn = QPushButton(
            "Удалить"
        )

        buttons.addWidget(add_btn)

        buttons.addWidget(edit_btn)

        buttons.addWidget(delete_btn)

        self.table = QTableWidget()

        layout.addLayout(buttons)

        layout.addWidget(self.table)

        self.setLayout(layout)

        self.load_products()

    def load_products(self):

        data = load_products()

        self.table.setRowCount(
            len(data)
        )

        self.table.setColumnCount(
            len(data.columns)
        )

        self.table.setHorizontalHeaderLabels(
            data.columns
        )

        for row in range(len(data)):

            for col in range(len(data.columns)):

                column_name = str(
                    data.columns[col]
                )

                if "фото" in column_name.lower():

                    image_path = str(
                        data.iloc[row, col]
                    ).strip()

                    label = QLabel()

                    label.setAlignment(
                        Qt.AlignCenter
                    )

                    if os.path.exists(image_path):

                        pixmap = QPixmap(
                            image_path
                        )

                        label.setPixmap(
                            pixmap.scaled(
                                180,
                                120,
                                Qt.KeepAspectRatio,
                                Qt.SmoothTransformation
                            )
                        )

                    else:

                        label.setText(
                            "Нет фото"
                        )

                    self.table.setCellWidget(
                        row,
                        col,
                        label
                    )

                else:

                    self.table.setItem(
                        row,
                        col,
                        QTableWidgetItem(
                            str(
                                data.iloc[row, col]
                            )
                        )
                    )

        self.table.verticalHeader().setDefaultSectionSize(
            130
        )

        self.table.resizeColumnsToContents()