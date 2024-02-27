from aiogram import Router, Bot

from lexicon.lexicon_ru import LEXICON_ADMIN_RU

router = Router()

@router.startup()
async def start_bot(bot: Bot, admin_id):
    await bot.send_message(chat_id=admin_id, text=LEXICON_ADMIN_RU["start"])


@router.shutdown()
async def stop_bot(bot: Bot, admin_id):
    await bot.send_message(chat_id=admin_id, text=LEXICON_ADMIN_RU["stop"])