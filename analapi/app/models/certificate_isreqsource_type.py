from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class CertificateIsreqsourceType(Base):
    __tablename__ = "certificate_isreqsource_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
