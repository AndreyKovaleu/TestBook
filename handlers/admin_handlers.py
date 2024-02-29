from aiogram import Router, Bot

from lexicon.lexicon import LEXICON_ADMIN

router = Router()


@router.startup()
async def start_bot(bot: Bot, admin_id):
    await bot.send_message(chat_id=admin_id, text=LEXICON_ADMIN["start"])


@router.shutdown()
async def stop_bot(bot: Bot, admin_id):
    await bot.send_message(chat_id=admin_id, text=LEXICON_ADMIN["stop"])
