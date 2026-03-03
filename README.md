# 🚀 Binance Futures Testnet Trading Bot

A modular CLI-based trading bot built in Python using the Binance Futures Testnet API.

This project demonstrates clean architecture, API integration, input validation, and structured logging — designed for learning algorithmic trading system fundamentals.

---

## 📌 Features

* ✅ Place **MARKET** and **LIMIT** orders
* ✅ Binance **Futures Testnet** integration
* ✅ Secure API key handling via `.env`
* ✅ Input validation for safe execution
* ✅ Rotating file logging system
* ✅ Modular and scalable project structure

---

## 🏗 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── cli.py              # Command line interface entry point
│   ├── client.py           # Binance API client wrapper
│   ├── orders.py           # Order creation logic
│   ├── validators.py       # Input validation logic
│   └── logging_config.py   # Logging configuration
│
├── logs/                   # Log files (auto-generated)
├── .env                    # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Dewansh13Tyagi/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate (Windows PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Keys

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
```

API keys must be generated from:

👉 https://testnet.binancefuture.com/

⚠️ Never commit your `.env` file.

---

## ▶️ Usage

### MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.002
```

### LIMIT Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.002 --price 70000
```

---

## 📊 Example Output

```
Order Placed Successfully
Order ID: 12603300310
Status: NEW
Executed Qty: 0.002
Avg Price: 64231.40
```

---

## 🧠 Key Concepts Demonstrated

* REST API integration
* Futures trading mechanics
* Notional value validation
* Separation of concerns (modular design)
* Logging best practices
* Environment variable security

---

## 🔒 Safety Notice

This bot connects to the **Binance Futures Testnet** only.
No real funds are used.

---

## 🚀 Future Improvements

* Position tracking
* Stop-loss & Take-profit
* Automated strategy logic
* Risk management module
* Web dashboard interface

---

## 🛠 Tech Stack

* Python 3.10
* python-binance
* argparse
* python-dotenv
* logging

---

## 📄 License

This project is for educational purposes only.
