from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import os

TOKEN = "8780787804:AAEyBdPF1gt1ayWcKeHwS86KPZ6fpA4HR2U"

# Создаём приложение Flask
app = Flask(__name__)

# Создаём бота
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

# Добавляем обработчики
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CallbackQueryHandler(spots, pattern="spots"))
bot_app.add_handler(CallbackQueryHandler(deals, pattern="deals"))

# Flask роут для приёма обновлений от Telegram
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.process_update(update)
    return "OK", 200

# Главная страница (для проверки)
@app.route("/")
def home():
    return "Bot is running!", 200

# Настройка вебхука при запуске (вместо before_first_request)
def setup_webhook():
    try:
        # Сбрасываем старые вебхуки и ставим новый
        bot_app.bot.set_webhook(url="https://toptraiderpro.up.railway.app/webhook", drop_pending_updates=True)
        print("✅ Webhook установлен успешно!")
    except Exception as e:
        print(f"❌ Ошибка установки webhook: {e}")

if __name__ == "__main__":
    # Сначала устанавливаем вебхук
    setup_webhook()
    # Затем запускаем Flask
    app.run(host="0.0.0.0", port=8080)
