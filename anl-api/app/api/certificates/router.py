from typing import Optional
from fastapi import APIRouter
from .schemas import Certificate, DoctorInfo, Stats
from .get_certificates import get_certificates
from .get_certificate_by_id import get_certificate_by_id
from .get_stats import get_stats
from .get_doctor_info import get_doctor_info
from .get_repaid_doctor_info import get_repaid_doctor_info


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
    path="/doctor_info/{doctor_id}",
    endpoint=get_doctor_info,
    response_model=Optional[DoctorInfo],
)
router.add_api_route(
    path="/repaid_doctor_info/{doctor_id}",
    endpoint=get_repaid_doctor_info,
    response_model=Optional[DoctorInfo],
)
router.add_api_route(
    path="/{certificate_id}",
    endpoint=get_certificate_by_id,
    response_model=Optional[Certificate],
    methods=["GET"],
)
