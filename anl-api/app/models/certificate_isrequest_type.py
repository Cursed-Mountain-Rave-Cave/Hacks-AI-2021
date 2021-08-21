from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class CertificateIsrequestType(Base):
    __tablename__ = "certificate_isrequest_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
