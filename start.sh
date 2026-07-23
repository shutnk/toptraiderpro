#!/bin/bash

# 1. Запускаем бота в фоновом режиме
python bot.py &

# 2. Запускаем Gunicorn в "foreground" (он будет держать контейнер открытым)
# --timeout 0 означает "никогда не завершайся"
gunicorn bot:app --bind 0.0.0.0:8080 --timeout 0 --log-level debug
