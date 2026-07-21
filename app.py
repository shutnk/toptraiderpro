from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>B2B Arbitrage</title></head>
<body>
<h1>🔥 B2B Арбитраж</h1>
<p>Текущий спред: <span id="spread">0.8%</span></p>
<p>Рекомендация: Купить BTC на Binance</p>
<a href="https://t.me/toptraderprobot">Перейти в бот</a>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
