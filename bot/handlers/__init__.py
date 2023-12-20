from aiogram import Router

from .comic_inline_handler import reading_router
from .main_hand import comics_router
from .start_handlers import start_router
from .admins_handlers import admin_router

# union handlers
main_router = Router()

main_router.include_router(start_router)
main_router.include_router(comics_router)
main_router.include_router(reading_router)
main_router.include_router(admin_router)
