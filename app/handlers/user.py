from aiogram import Router,types
from aiogram.filters import Command
from app.database.db import *
from app.keyboards import main_menu
from app.services.openrouter import ask

router=Router()

@router.message(Command("start"))
async def start(m:types.Message):
    add_user(m.from_user.id)
    await m.answer("🤖 AI Assistant\n\nВыберите действие:",reply_markup=main_menu)

@router.message()
async def chat(m:types.Message):
    save(m.from_user.id,"user",m.text)
    msgs=[{"role":a,"content":b} for a,b in history(m.from_user.id)]
    answer=await ask(msgs,get_model(m.from_user.id))
    save(m.from_user.id,"assistant",answer)
    await m.answer(answer)
