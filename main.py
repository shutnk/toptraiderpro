# Этот файл нужен, чтобы обмануть Gunicorn
from bot import app

# Если Gunicorn всё же запустится, он найдет этот файл и не выдаст ошибку

if __name__ == "__main__":
    print("⚠️ Запуск через main.py (для обхода ошибки Gunicorn)")
    # Запускаем твой основной код
    import bot
