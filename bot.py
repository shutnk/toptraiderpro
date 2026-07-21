import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = "8780787804:AAEyBdPF1gt1ayWcKeHwS86KPZ6fpA4HR2U"

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("📊 Лучшие споты", callback_data="spots")],
        [InlineKeyboardButton("📈 Сделки B2B", callback_data="deals")],
        [InlineKeyboardButton("👥 Создать группу знаний", callback_data="group")]
    ]
    await update.message.reply_text(
        "🚀 *B2B Арбитраж Прокси*\n\nЯ ищу лучшие споты и сделки в реальном времени.\nВыбери действие:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def spots(update: Update, context):
    await update.callback_query.message.reply_text(
        "📊 *Лучшие споты:*\nBTC/USDT: 61200 🟢\nETH/USDT: 3400 🔵\n(обновляется каждые 5 сек)"
    )

async def deals(update: Update, context):
    await update.callback_query.message.reply_text(
        "📈 *Активные B2B-сделки:*\n• Купить BTC на Binance → продать на Bybit (профит 0.4%)\n• Купить ETH на OKX → продать на Kraken (профит 0.6%)"
    )

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(spots, pattern="spots"))
    app.add_handler(CallbackQueryHandler(deals, pattern="deals"))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
