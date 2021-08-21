from sqlalchemy.sql.expression import and_
from typing import Optional

import app.models as m
from app.services.postgres import session_scope
from .schemas import DoctorInfo
from sqlalchemy import func
from app.settings import settings


def get_repaid_doctor_info(doctor_id: int) -> Optional[DoctorInfo]:
    with session_scope() as session:
        result = (
            session.query(
                func.count(m.Certificate.id.distinct()).label("certificates_count"),
                func.count(m.CertificateScore.certificate_id.distinct()).label("mistakes_count"),
            )
            .outerjoin(
                m.CertificateScore,
                and_(
                    m.Certificate.id == m.CertificateScore.certificate_id,
                    m.CertificateScore.score > settings.SCORE_ERROR_THRESHOLD,
                ),
            )
            .filter(m.Certificate.repaid_doctor_id == doctor_id)
            .first()
        )

        mistakes_ratio = (
            result["mistakes_count"] / result["certificates_count"]
            if result["certificates_count"] != 0
            else 0
        )

        given_certificates = (
            session.query(
                func.date_trunc("day", m.Certificate.cert_date).label("date"),
                func.count(m.Certificate.id).label("count"),
            )
            .filter(m.Certificate.repaid_doctor_id == doctor_id)
            .group_by(func.date_trunc("day", m.Certificate.cert_date))
            .order_by("date")
            .all()
        )

        product_mistakes_ratio_data = (
            session.query(
                m.ProductType.name.label("product_type"),
                func.count(m.Certificate.id.distinct()).label("certificates_count"),
                func.count(m.CertificateScore.certificate_id.distinct()).label("mistakes_count"),
            )
            .outerjoin(
                m.CertificateScore,
                and_(
                    m.Certificate.id == m.CertificateScore.certificate_id,
                    m.CertificateScore.score > settings.SCORE_ERROR_THRESHOLD,
                ),
            )
            .outerjoin(m.ProductType)
            .filter(m.Certificate.repaid_doctor_id == doctor_id)
            .group_by(m.ProductType.name)
            .all()
        )

        product_mistakes_ratio = list(map(
            lambda data: {
                "product_type": data["product_type"],
                "mistakes_ratio": (
                    data["mistakes_count"] / data["certificates_count"]
                    if data["certificates_count"]
                    else 0
                ),
            },
            product_mistakes_ratio_data,
        ))

        return {
            "mistakes_ratio": mistakes_ratio,
            "given_certificates": given_certificates,
            "product_mistakes_ratio": product_mistakes_ratio,
        }
