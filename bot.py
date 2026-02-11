import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

# 👇 import your country-specific bots
from countries import mx, in_, arg  # add more later when ready

TOKEN = os.getenv("BOT_TOKEN")  # ⚠️ use env var in production

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ───────────────── COUNTRY STATE (IN-MEMORY) ─────────────────
user_country: dict[int, str] = {}

COUNTRY_HANDLERS = {
    "mx": mx,     # Mexico
    "in": in_,# India
    "arg": arg
}

def get_handler(user_id: int):
    country = user_country.get(user_id)
    if not country:
        return None
    return COUNTRY_HANDLERS.get(country)

# ───────────────── COUNTRY PICKER ─────────────────
def country_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇲🇽 Mexico", callback_data="country_mx")],
        [InlineKeyboardButton(text="🇮🇳 India", callback_data="country_in")],
        [InlineKeyboardButton(text="🇦🇷 Argentina", callback_data="country_arg")]
    ])

# ───────────────── /start ─────────────────
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🌍 Please select your country:",
        reply_markup=country_keyboard()
    )

# ───────────────── SET COUNTRY ─────────────────
@dp.callback_query(F.data.startswith("country_"))
async def set_country(call: types.CallbackQuery):
    country = call.data.split("_", 1)[1]

    if country not in COUNTRY_HANDLERS:
        await call.answer("This country is coming soon 🚀", show_alert=True)
        return

    user_country[call.from_user.id] = country
    handler = COUNTRY_HANDLERS[country]

    # Each country module MUST implement start(message)
    await handler.start(call.message)
    await call.answer()

# ───────────────── ROUTE ALL CALLBACKS ─────────────────
@dp.callback_query()
async def route_callbacks(call: types.CallbackQuery):
    handler = get_handler(call.from_user.id)

    # 🚨 No country selected → force country picker
    if handler is None:
        await call.message.edit_text(
            "🌍 Please select your country:",
            reply_markup=country_keyboard()
        )
        await call.answer()
        return

    # Normal routing
    if hasattr(handler, "handle_callback"):
        await handler.handle_callback(call)
    else:
        await call.answer("Unsupported action", show_alert=True)

# ───────────────── STARTUP SAFETY CHECK ─────────────────
def validate_country_modules():
    for code, module in COUNTRY_HANDLERS.items():
        if not hasattr(module, "start") or not hasattr(module, "handle_callback"):
            raise RuntimeError(
                f"Country module '{code}' is missing start() or handle_callback()"
            )

# ───────────────── RUN ─────────────────
async def main():
    validate_country_modules()
    print("CSR bot running (country selection required)")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
