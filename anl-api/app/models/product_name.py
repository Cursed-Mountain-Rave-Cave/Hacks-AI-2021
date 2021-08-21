from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base
from .sub_product import SubProduct


class ProductName(Base):
    __tablename__ = "product_name"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    sub_product_id = Column(ForeignKey(SubProduct.id))
    fit_gost = Column(Integer)
    sub_product_guid = Column(ForeignKey(SubProduct.guid))
    is_last = Column(Integer)
    active = Column(Integer)
