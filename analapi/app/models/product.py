from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base
from .product_type import ProductType


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    product_type_id = Column(ForeignKey(ProductType.id))
    guid = Column(String(36))
