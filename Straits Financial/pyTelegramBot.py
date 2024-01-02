# Import libraries
import telegram
import os
import requests
import environs
import pandas as pd
import json
from telegram.ext import Application, Updater, CallbackContext, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update
from dotenv import load_dotenv
from datetime import datetime
import telebot

# Load config file .env
load_dotenv()

# Telegram Bot Token
TOKEN = os.getenv('API_KEY')
BOT_USERNAME = os.getenv('BOT_USERNAME')

# CoinGecko API URL
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Crypto Price Bot!")
    print(type(update.message))
    print(update.message)
    print(update.message.from_user)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
    /start -> Welcome to the telebot
    /help -> Get helping
    /price -> Get the current bitcoin and ethereum price
    """
    )

# Set the bot in a telegram group with permission 'Promote to admin' in telegram


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot: ', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


async def get_crypto_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(COINGECKO_API_URL, params={
                            "ids": "bitcoin,ethereum", "vs_currencies": "usd", "include_last_updated_at": 'true'})
    if response.status_code == 200:
        data = response.json()
        btc_price = data["bitcoin"]["usd"]
        eth_price = data["ethereum"]["usd"]
        time_btc = datetime.fromtimestamp(
            data["bitcoin"]["last_updated_at"]).strftime("%Y-%m-%d %H:%M:%S")
        time_eth = datetime.fromtimestamp(
            data["ethereum"]["last_updated_at"]).strftime("%Y-%m-%d %H:%M:%S")
        await update.message.reply_text(f"BTC Price: ${btc_price} updated at {time_btc} \
                                        \nETH Price: ${eth_price} updated at {time_eth}")
    else:
        await update.message.reply_text("Sorry, something went wrong. Please try again later.")


def main():
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    # Command
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)
    price_handler = CommandHandler("price", get_crypto_prices)
    message_handler = MessageHandler(filters.TEXT, handle_message)

    app.add_handler(start_handler)
    app.add_handler(help_handler)
    app.add_handler(price_handler)
    app.add_handler(message_handler)

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
