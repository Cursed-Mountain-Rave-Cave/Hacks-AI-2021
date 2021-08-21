from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class MilkType(Base):
    __tablename__ = "milk_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
