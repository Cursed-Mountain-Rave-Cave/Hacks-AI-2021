from fastapi import APIRouter
from .certificates import router as certificates_router

router = APIRouter()
router.include_router(certificates_router)
