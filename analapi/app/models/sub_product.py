from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base
from .product import Product
from .milk_type import MilkType


class SubProduct(Base):
    __tablename__ = "sub_product"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    product_id = Column(ForeignKey(Product.id))
    guid = Column(String(36), unique=True)
    last = Column(Integer)
    milk_type_id = Column(ForeignKey(MilkType.id))
    uuid = Column(String(36))
    code = Column(String(20))
