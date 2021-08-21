from typing import Optional
import app.models as m
from app.services.postgres import session_scope
from .schemas import Stats
from sqlalchemy import func


def get_stats() -> Optional[Stats]:
    with session_scope() as session:
        return session.query(
            func.count(m.Certificate.doctor_id.distinct()).label("doctors_count"),
            func.count(m.Certificate.id.distinct()).label("certificates_count"),
        ).first()
