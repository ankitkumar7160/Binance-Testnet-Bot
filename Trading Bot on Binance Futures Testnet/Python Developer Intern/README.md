# Binance Futures Testnet Trading Bot

## Overview

This project is a simple Python-based trading bot developed for Binance Futures Testnet (USDT-M).

The application allows users to place MARKET and LIMIT orders from the command line. It supports both BUY and SELL operations and includes input validation, logging, and error handling.

The purpose of this project is to demonstrate clean code structure, API integration, and basic trading automation.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Support BUY and SELL sides
- Command Line Interface (CLI)
- Input validation
- Error handling
- API request and response logging
- Binance Futures Testnet integration
- Clean and reusable project structure

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   ├── market_order.log
│   └── limit_order.log
│
├── cli.py
├── requirements.txt
├── .env
├── example.env
└── README.md
```

---

## Requirements

- Python 3.9 or higher
- Binance Futures Testnet Account
- Binance Testnet API Key
- Binance Testnet Secret Key

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd trading_bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root directory.

Example:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_SECRET_KEY
```

You can also rename `example.env` to `.env` and update the values.

---

## How to Get Binance Testnet API Keys

1. Create/Login to Binance Futures Testnet account.
2. Open API Management.
3. Create a new API key.
4. Copy API Key and Secret Key.
5. Add them to the `.env` file.

---

## Running the Application

### MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Command Parameters

| Parameter | Description | Example |
|------------|------------|------------|
| --symbol | Trading pair | BTCUSDT |
| --side | BUY or SELL | BUY |
| --type | MARKET or LIMIT | MARKET |
| --quantity | Order quantity | 0.001 |
| --price | Required for LIMIT orders | 120000 |

---

## Sample Output

```text
ORDER SUMMARY
--------------------------------
Symbol : BTCUSDT
Side : BUY
Type : MARKET
Quantity : 0.001

SUCCESS

Order ID : 12345678
Status : FILLED
Executed Qty : 0.001
Average Price : 105000
```

---

## Logging

All API requests, responses, and errors are stored in log files.

Example:

```text
logs/market_order.log
logs/limit_order.log
```

Logs help with debugging and tracking order activity.

---

## Error Handling

The application handles:

- Invalid order side
- Invalid order type
- Invalid quantity
- Missing price for LIMIT orders
- API errors
- Network issues
- Missing API credentials

---

## Assumptions

- User has a valid Binance Futures Testnet account.
- API credentials are active and have correct permissions.
- Internet connection is available.
- Orders are placed only on Binance Futures Testnet and not on the live exchange.

---

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- argparse
- logging

---

## Author

Ankit Kumar

Python Developer Internship Assignment Submission