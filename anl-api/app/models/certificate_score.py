from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, Boolean, DateTime, Float, String
from .base import Base
from .certificate import Certificate


class CertificateScore(Base):
    __tablename__ = "certificate_score"

    id = Column(BigInteger, primary_key=True)
    certificate_id = Column(ForeignKey(Certificate.id), nullable=False)
    active = Column(Boolean, server_default="True")
    approved = Column(Boolean, server_default="False")
    denied = Column(Boolean, server_default="False")
    score = Column(Float)
    score_violation_type = Column(String(100))
    score_date = Column(DateTime, server_default=current_timestamp())
    resolution_date = Column(DateTime)
