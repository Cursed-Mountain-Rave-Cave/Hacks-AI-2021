from typing import Optional
import app.models as m
from app.services.postgres import session_scope
from .schemas import DoctorsCount
from sqlalchemy import func


def get_doctors_count() -> Optional[DoctorsCount]:
    with session_scope() as session:
        return session.query(
            func.count(m.Certificate.doctor_id.distinct()).label("count")
        ).first()
