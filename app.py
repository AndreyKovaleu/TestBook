import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config_data.config import Config, load_config
from keyboards.main_menu import set_main_menu


# from handlers import router as main_handlers_router
from handlers.user_handlers import router as user_router
from handlers.other_handlers import router as other_router


async def main() -> None:
    config: Config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_routers(user_router, other_router)

    # dp.workflow_data.update({"admin_id": config.tg_bot.admin_ids[0]})
    # dp.include_router(main_handlers_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(filename)s:%(lineno)d #%(levelname)-8s "
                                                   "[%(asctime)s] - %(name)s - %(message)s")
    asyncio.run(main())
