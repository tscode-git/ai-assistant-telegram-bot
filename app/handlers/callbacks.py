from aiogram import Router,types
from app.keyboards import main_menu,models
from app.database.db import *

router=Router()

@router.callback_query()
async def callbacks(c:types.CallbackQuery):
    uid=c.from_user.id

    if c.data=="new" or c.data=="clear":
        clear(uid)
        await c.message.answer("🗑 Память очищена",reply_markup=main_menu)

    elif c.data=="models":
        await c.message.answer("Выберите модель:",reply_markup=models)

    elif c.data.startswith("model:"):
        set_model(uid,c.data.replace("model:",""))
        await c.message.answer("✅ Модель изменена")

    elif c.data=="stats":
        await c.message.answer(f"📊 Сообщений: {count_messages(uid)}")

    await c.answer()
