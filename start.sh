#!/bin/bash

# 1. Принудительно сбрасываем старые вебхуки и ставим новый через API (минуя Python)
echo "🔄 Устанавливаю Webhook через API..."
curl -X POST "https://api.telegram.org/bot8780787804:AAEyBdPF1gt1ayWcKeHwS86KPZ6fpA4HR2U/setWebhook?url=https://toptraiderpro.up.railway.app/webhook&drop_pending_updates=true"

# 2. Запускаем Gunicorn (держит контейнер открытым)
echo "🚀 Запускаю Gunicorn..."
gunicorn bot:app --bind 0.0.0.0:8080 --timeout 0
