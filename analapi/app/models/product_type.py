from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class ProductType(Base):
    __tablename__ = "product_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    uuid = Column(String(36))
