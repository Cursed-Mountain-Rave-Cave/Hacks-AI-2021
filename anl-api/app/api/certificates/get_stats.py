from app.models.certificate_score import CertificateScore
from typing import Optional

from sqlalchemy.sql.expression import outerjoin
import app.models as m
from app.services.postgres import session_scope
from .schemas import Stats
from sqlalchemy import func


def get_stats() -> Optional[Stats]:
    with session_scope() as session:
        result = (session.query(
            func.count(m.Certificate.doctor_id.distinct()).label("doctors_count"),
            func.count(m.Certificate.id.distinct()).label("certificates_count"),
            func.count(m.CertificateScore.certificate_id.distinct()).label("mistakes_count"),
        )
            .outerjoin(CertificateScore)
            .first()
        )

        result = dict(result)
        result["mistakes_ratio"] = (
            result["mistakes_count"] / result["certificates_count"]
            if result["certificates_count"] != 0
            else 0
        )
        return result
