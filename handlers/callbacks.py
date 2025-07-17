import aiogram
from aiogram import Router , F

from aiogram.types import CallbackQuery


callbacks_router = Router()





@callbacks_router.callback_query(F.data == "test")
async def handle_test(t : CallbackQuery):
    await t.answer("GOAL TEXT")
    q_message = "we got query"
    await t.message.answer(text=q_message)


