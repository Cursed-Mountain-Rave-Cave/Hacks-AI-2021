from typing import Optional
from fastapi import APIRouter
from .schemas import Certificate, DoctorsCount
from .get_certificates import get_certificates
from .get_certificate_by_id import get_certificate_by_id
from .get_doctors_count import get_doctors_count


router = APIRouter(prefix="/certificates")

router.add_api_route(
    path="", endpoint=get_certificates, response_model=list[Certificate], methods=["GET"]
)
router.add_api_route(
    path="/doctors_count",
    endpoint=get_doctors_count,
    response_model=Optional[DoctorsCount],
)
router.add_api_route(
    path="/{certificate_id}",
    endpoint=get_certificate_by_id,
    response_model=Optional[Certificate],
    methods=["GET"],
)
