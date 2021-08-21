from typing import Optional
from fastapi import Path
import app.models as m
from app.services.postgres import session_scope
from .schemas import Certificate
from .certificate_query_base import get_certificate_query_base


def get_certificate_by_id(certificate_id: int = Path(...)) -> Optional[Certificate]:
    with session_scope() as session:
        return (
            get_certificate_query_base(session).filter(m.Certificate.id == certificate_id).first()
        )
