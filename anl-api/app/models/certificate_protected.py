from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class CertificateProtected(Base):
    __tablename__ = "certificate_protected"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
