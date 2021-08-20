from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base
from .country import Country


class Region(Base):
    __tablename__ = "region"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    guid = Column(String(36), unique=True)
    last = Column(Integer)
    federal_district = Column(Integer)
    guid_country = Column(ForeignKey(Country.guid))
