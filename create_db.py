from database.db import engine

from models.user import Base
from models.product import Product
from models.order import Order

Base.metadata.create_all(bind=engine)

print("База данных создана")