from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://financialmodelingprep.com/api/v3/quote-short/{ticker}"


def fetch_price(ticker):
    data = requests.get(
        API_URL.format(ticker=ticker),
        params={"apikey": "4e2c458b64cdb0f6c94c9598264c63b4"},
    ).json()
    return data[0]["price"]


# http://localhost:5000/stock/AAPL


@app.route("/stock/<ticker>")
def stock(ticker):
    price = fetch_price(ticker)
    return render_template("stock_quote.html", ticker=ticker, stock_price=price)


@app.route("/")
def home_page():
    return render_template("index.html")
