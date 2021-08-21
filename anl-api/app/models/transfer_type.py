from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class TransferType(Base):
    __tablename__ = "transfer_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
