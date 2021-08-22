from .schemas import Scoring
from fastapi import APIRouter
from .get_scoring import get_scoring
from .put_scoring import put_scoring
from .change_status import approve, deny


router = APIRouter(prefix="/scoring")

router.add_api_route(path="", endpoint=put_scoring, methods=["POST"])

router.add_api_route(path="", endpoint=get_scoring, response_model=list[Scoring], methods=["GET"])

router.add_api_route(path="/{id}/approve", endpoint=approve, methods=["POST"])

router.add_api_route(path="/{id}/deny", endpoint=deny, methods=["POST"])
