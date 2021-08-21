from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .base import Base


class Former(Base):
    __tablename__ = "former"

    id = Column(Integer, primary_key=True)
    id2 = Column(String(30))
    name = Column(String(500))
