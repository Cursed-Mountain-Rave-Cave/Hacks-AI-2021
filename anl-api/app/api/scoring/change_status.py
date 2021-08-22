import datetime
from app.services import session_scope
import app.models as m


def approve(id: int):
    with session_scope() as session:
        (
            session.query(m.CertificateScore)
            .filter(m.CertificateScore.id == id)
            .update(
                {
                    m.CertificateScore.denied: False,
                    m.CertificateScore.active: False,
                    m.CertificateScore.approved: True,
                    m.CertificateScore.resolution_date: datetime.datetime.now(),
                }
            )
        )


def deny(id: int):
    with session_scope() as session:
        (
            session.query(m.CertificateScore)
            .filter(m.CertificateScore.id == id)
            .update(
                {
                    m.CertificateScore.denied: True,
                    m.CertificateScore.active: False,
                    m.CertificateScore.approved: False,
                    m.CertificateScore.resolution_date: datetime.datetime.now(),
                }
            )
        )
