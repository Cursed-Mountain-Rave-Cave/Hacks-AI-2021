from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class Unit(Base):
    __tablename__ = "unit"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    base_unit_id = Column(Integer)
    ratio = Column(Integer)
    guid = Column(String(36), unique=True)
    last = Column(Integer)
    uuid = Column(String(36))
    base_unit_uuid = Column(String(36))
    base_unit_guid = Column(String(36))
