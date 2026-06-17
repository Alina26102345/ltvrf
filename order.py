from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    customer = Column(String)

    product = Column(String)

    count = Column(Integer)

    status = Column(String)