from fastapi import Query
import app.models as m
from app.services.postgres import session_scope
from .schemas import Certificate
from .certificate_query_base import get_certificate_query_base


def get_certificates(
    offset: int = Query(0),
    limit: int = Query(50),
) -> list[Certificate]:
    with session_scope() as session:
        return (
            get_certificate_query_base(session)
            .order_by(m.Certificate.cert_date)
            .offset(offset)
            .limit(limit)
            .all()
        )
