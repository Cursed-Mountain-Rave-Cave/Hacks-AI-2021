import app.models as models
from random import random
from app.services import session_scope, Session


IDS = [
    4354025555,
    4354025563,
    4354025572,
    4354025573,
    4354025591,
    4354025597,
    4354025598,
    4354025599,
    4354025600,
    4354025601,
    4354025602,
    4354025603,
    4354025604,
    4354025605,
    4354025606,
    4354025607,
    4354025608,
]

VIOLATION_TYPES = [
    "Несвоевременное гашение ВСД",
    "Оборот товаров с использованием фантомных площадок",
    "Сертификация продукции с авансовыми датами выработки",
    "Сертификация продукции с истекшим сроком годности",
]


def insert_certificates_head(session: Session):
    for violation_type in VIOLATION_TYPES:
        session.bulk_insert_mappings(
            models.CertificateScore,
            [
                {
                    "certificate_id": id,
                    "score": random() ** 5,
                    "score_violation_type": violation_type,
                }
                for id in IDS
            ],
        )


if __name__ == "__main__":
    with session_scope() as session:
        insert_certificates_head(session)
