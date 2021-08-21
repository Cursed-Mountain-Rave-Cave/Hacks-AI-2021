from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class CertificateType(Base):
    __tablename__ = "certificate_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
