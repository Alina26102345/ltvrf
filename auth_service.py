import pandas as pd


def login_user(login, password):

    data = pd.read_excel(
        "excel/user_import.xlsx"
    )

    for _, row in data.iterrows():

        file_login = str(
            row["Логин"]
        ).strip()

        file_password = str(
            row["Пароль"]
        ).strip()

        if (
            login == file_login
            and
            password == file_password
        ):

            return {
                "role": row["Роль сотрудника"],
                "fio": row["ФИО"]
            }

    return None