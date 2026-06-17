from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from services.auth_service import login_user

from windows.guest_window import GuestWindow
from windows.manager_window import ManagerWindow
from windows.admin_window import AdminWindow


class LoginWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Вход в систему")

        self.resize(500, 600)

        layout = QVBoxLayout()

        # Логотип
        logo = QLabel()

        logo.setAlignment(Qt.AlignCenter)

        try:
            pixmap = QPixmap("resources/logo.png")

            logo.setPixmap(
                pixmap.scaled(
                    250,
                    150,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

        except:
            logo.setText("ВЕЛОСИПЕДДРАЙВ")

        # Заголовок
        title = QLabel("Авторизация")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
        """)

        # Поля ввода
        self.login_edit = QLineEdit()

        self.login_edit.setPlaceholderText(
            "Введите логин"
        )

        self.password_edit = QLineEdit()

        self.password_edit.setPlaceholderText(
            "Введите пароль"
        )

        self.password_edit.setEchoMode(
            QLineEdit.Password
        )

        # Кнопки
        login_btn = QPushButton("Войти")

        guest_btn = QPushButton(
            "Войти как гость"
        )

        login_btn.clicked.connect(
            self.login
        )

        guest_btn.clicked.connect(
            self.open_guest
        )

        layout.addWidget(logo)

        layout.addWidget(title)

        layout.addWidget(
            QLabel("Логин")
        )

        layout.addWidget(
            self.login_edit
        )

        layout.addWidget(
            QLabel("Пароль")
        )

        layout.addWidget(
            self.password_edit
        )

        layout.addWidget(
            login_btn
        )

        layout.addWidget(
            guest_btn
        )

        self.setLayout(layout)

    def login(self):

        login = self.login_edit.text().strip()

        password = self.password_edit.text().strip()

        user = login_user(
            login,
            password
        )

        if user is None:

            QMessageBox.warning(
                self,
                "Ошибка",
                "Неверный логин или пароль"
            )

            return

        role = str(
            user["role"]
        ).lower()

        fio = user["fio"]

        if "администратор" in role:

            self.window = AdminWindow()

        elif "менеджер" in role:

            self.window = ManagerWindow()

        elif "клиент" in role:

            self.window = GuestWindow()

        else:

            self.window = GuestWindow()

        self.window.setWindowTitle(
            f"{fio} ({user['role']})"
        )

        self.window.show()

        self.close()

    def open_guest(self):

        self.window = GuestWindow()

        self.window.show()

        self.close()