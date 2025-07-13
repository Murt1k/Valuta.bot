import aiogram
from aiogram import Router , F

from aiogram.types import CallbackQuery


callbacks_router = Router()


@callbacks_router.callback_query(F.data == "query")
async def get_query(callback: CallbackQuery):
    await callback.answer()
    q_message = "we got query"
    await callback.message.answer(text=q_message)


@callbacks_router.callback_query(F.data == "test")
async def handle_test(t : CallbackQuery):
    await t.answer("GOAL TEXT")
    q_message = "we got query"
    await callback.message.answer(text=q_message)


