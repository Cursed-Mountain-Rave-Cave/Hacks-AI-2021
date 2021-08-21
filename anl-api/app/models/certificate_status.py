from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class CertificateStatus(Base):
    __tablename__ = "certificate_status"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
