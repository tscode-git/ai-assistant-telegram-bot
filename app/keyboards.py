from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

main_menu=InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="💬 Новый диалог",callback_data="new")],
[InlineKeyboardButton(text="🧹 Очистить память",callback_data="clear")],
[InlineKeyboardButton(text="🧠 Выбор модели",callback_data="models")],
[InlineKeyboardButton(text="📊 Статистика",callback_data="stats")]
])

models=InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="⚡ Gemini Flash",callback_data="model:google/gemini-2.0-flash-exp:free")],
[InlineKeyboardButton(text="🧠 GPT Mini",callback_data="model:openai/gpt-4o-mini")],
[InlineKeyboardButton(text="🚀 Claude",callback_data="model:anthropic/claude-3.5-sonnet")]
])
