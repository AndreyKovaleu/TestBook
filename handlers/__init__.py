from aiogram import Router

from .admin_handlers import router as admin_router
from .user_handlers import router as user_router

router = Router(name=__name__)

router.include_routers(admin_router,
                       user_router)

__all__ = ["router"]
