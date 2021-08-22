from fastapi import APIRouter
from .certificates import router as certificates_router
from .scoring import router as scoring_router

router = APIRouter()
router.include_router(certificates_router)
router.include_router(scoring_router)
