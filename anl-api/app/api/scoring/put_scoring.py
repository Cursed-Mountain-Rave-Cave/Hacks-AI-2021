from app.api.scoring.schemas import PutScoring
from app.services import session_scope
from app.models import CertificateScore


def put_scoring(request: PutScoring) -> None:
    with session_scope() as session:
        score = CertificateScore({"certificate_id": request.certificate_id})
        session.add(score)
