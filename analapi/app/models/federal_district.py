from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class FederalDistrict(Base):
    __tablename__ = "federal_district"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
