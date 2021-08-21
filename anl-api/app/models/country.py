from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String
from .base import Base


class Country(Base):
    __tablename__ = "country"

    guid = Column(String(36), primary_key=True)
    name = Column(String(500))
    alpha2 = Column(String(2))
    alpha3 = Column(String(3))
    numCode = Column(String(10))
