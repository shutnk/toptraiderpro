#!/bin/bash
# Запускаем бота в фоне
python bot.py &

# Запускаем веб-сервер (gunicorn)
gunicorn app:app --bind 0.0.0.0:8080
