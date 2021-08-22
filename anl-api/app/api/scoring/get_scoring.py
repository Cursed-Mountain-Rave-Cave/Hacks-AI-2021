from app.api.scoring.schemas import Scoring
from app.services import session_scope
from sqlalchemy import or_
import app.models as m


def get_scoring(active: bool = True, approved: bool = False, denied: bool = False) -> list[Scoring]:
    with session_scope() as session:
        return (
            session.query(
                m.CertificateScore.id.label("id"),
                m.CertificateScore.certificate_id.label("certificate_id"),
                m.CertificateScore.active.label("active"),
                m.CertificateScore.approved.label("approved"),
                m.CertificateScore.denied.label("denied"),
                m.CertificateScore.score.label("score"),
                m.CertificateScore.score_violation_type.label("score_violation_type"),
                m.CertificateScore.score_date.label("score_data"),
                m.CertificateScore.resolution_date.label("resolution_date"),
            )
            .filter(
                or_(
                    m.CertificateScore.denied if denied else False,
                    m.CertificateScore.approved if approved else False,
                    m.CertificateScore.active if active else False,
                )
            )
            .all()
        )
