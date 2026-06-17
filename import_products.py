import pandas as pd

from database.db import SessionLocal

from models.product import Product

file = "excel/Tovar.xlsx"

data = pd.read_excel(file)

db = SessionLocal()

for index, row in data.iterrows():

    product = Product(
        name=row["Название"],
        price=row["Стоимость"],
        description=row["Описание"],
        quantity=row["Количество"],
        discount=row["Скидка"]
    )

    db.add(product)

db.commit()

db.close()