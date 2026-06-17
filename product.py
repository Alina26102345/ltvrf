from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    price = Column(Float)

    description = Column(String)

    quantity = Column(Integer)

    discount = Column(Float)

    image = Column(String)