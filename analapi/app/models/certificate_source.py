from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class CertificateSource(Base):
    __tablename__ = "certificate_source"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
