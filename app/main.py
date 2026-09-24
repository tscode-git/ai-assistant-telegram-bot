import asyncio
from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.handlers.user import router as user_router
from app.handlers.callbacks import router as callback_router

async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN missing")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(user_router)
    dp.include_router(callback_router)

    print("AI Assistant v2 started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
