from typing import Optional
from fastapi import APIRouter
from .schemas import Certificate, Stats
from .get_certificates import get_certificates
from .get_certificate_by_id import get_certificate_by_id
from .get_stats import get_stats


router = APIRouter(prefix="/certificates")

router.add_api_route(
    path="", endpoint=get_certificates, response_model=list[Certificate], methods=["GET"]
)
router.add_api_route(
    path="/stats",
    endpoint=get_stats,
    response_model=Optional[Stats],
)
router.add_api_route(
    path="/{certificate_id}",
    endpoint=get_certificate_by_id,
    response_model=Optional[Certificate],
    methods=["GET"],
)
