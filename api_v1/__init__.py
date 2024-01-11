from fastapi import APIRouter
from .billboards.views import router as billboards_router

router = APIRouter()
router.include_router(router=billboards_router, prefix="/billboards")
