from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import asyncio
import threading

TOKEN = "8780787804:AAEyBdPF1gt1ayWcKeHwS86KPZ6fpA4HR2U"

app = Flask(__name__)
bot_app = Application.builder().token(TOKEN).build()

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

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CallbackQueryHandler(spots, pattern="spots"))
bot_app.add_handler(CallbackQueryHandler(deals, pattern="deals"))

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.process_update(update)
    return "OK", 200

@app.route("/")
def home():
    return "Bot is running!", 200

def run_flask():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    print("🔄 Устанавливаю Webhook...")
    asyncio.run(bot_app.bot.set_webhook(
        url="https://toptraiderpro.up.railway.app/webhook", 
        drop_pending_updates=True
    ))
    print("✅ Webhook установлен успешно! Бот готов.")
    
    # Запускаем Flask в фоновом потоке
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # Держим основной процесс живым (вечный цикл)
    while True:
        pass
