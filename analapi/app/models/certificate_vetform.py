from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class CertificateVetform(Base):
    __tablename__ = "certificate_vetform"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
