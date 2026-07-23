#!/bin/bash
# Устанавливаем webhook (асинхронно) и запускаем бота в фоне
python bot.py &

# Запускаем Gunicorn для Flask
gunicorn bot:app --bind 0.0.0.0:8080 --timeout 120
