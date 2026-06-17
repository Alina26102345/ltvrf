import pandas as pd

from database.db import SessionLocal

from models.user import User

file = "excel/user_import.xlsx"

data = pd.read_excel(file)

db = SessionLocal()

for index, row in data.iterrows():

    user = User(
        login=row["Логин"],
        password=row["Пароль"],
        role=row["Роль"]
    )

    db.add(user)

db.commit()

db.close()

print("Пользователи импортированы")