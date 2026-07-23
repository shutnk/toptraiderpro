#!/bin/bash

# Устанавливаем вебхук через Python в фоне (он быстро выполнится и выйдет)
python -c "
import asyncio
from telegram import Bot
async def setup():
    await Bot('8780787804:AAEyBdPF1gt1ayWcKeHwS86KPZ6fpA4HR2U').set_webhook(
        url='https://toptraiderpro.up.railway.app/webhook',
        drop_pending_updates=True
    )
    print('✅ Webhook установлен успешно!')
asyncio.run(setup())
" &

# Основной процесс: запускаем Gunicorn (этот процесс будет жить вечно)
exec gunicorn bot:app --bind 0.0.0.0:8080 --timeout 0
