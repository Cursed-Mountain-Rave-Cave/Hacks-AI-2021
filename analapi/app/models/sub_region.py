from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base
from .country import Country
from .region import Region


class SubRegion(Base):
    __tablename__ = "sub_region"

    guid = Column(Integer, primary_key=True)
    name = Column(String(500))
    guid_country = Column(ForeignKey(Country.guid))
    iso_name = Column(String(3))
    region_num = Column(Integer)
    parent_guid = Column(ForeignKey(Region.guid))
