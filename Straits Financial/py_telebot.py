# Import libraries
import os
import telebot
from telebot import types
from dotenv import load_dotenv
import requests

# Load config file .env
load_dotenv()

# Telegram Bot Token
TOKEN = os.getenv('API_KEY')
BOT_USERNAME = os.getenv('BOT_USERNAME')

# Creating a instance
bot = telebot.TeleBot(TOKEN) 

# Commands
@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id, \
    """
    /greet -> Welcome to the telebot
    /hello -> Hello chatID
    /help -> Get helping
    /price -> Get the current bitcoin and ethereum price
    /game -> start markup
    /close -> close markup
    """
    )
    
@bot.message_handler(commands = ['greet'])
def greet(message):
    print(type(message))
    print(message)
    bot.reply_to(message, 'Hey! How is it going?')
    
@bot.message_handler(commands = ['hello'])
def hello(message):
    bot.send_message(message.chat.id, f'Hello {message.chat.id}')
 
@bot.message_handler(content_types = ['photo', 'sticker'])
def send_content_message(message):
    bot.reply_to(message, 'That is not a text message!')

@bot.message_handler(func=lambda message: message.chat.id is not None)
def send_user_name(message):
    chat_id = message.chat.id
    username = message.from_user.username
    if username:
        try:
            bot.send_message(chat_id = message.chat.id, text = f'Your username is {username}')
        except telebot.apihelper.ApiTelegramException as e:
            print(f"Error sending message to chat {chat_id}: {e}")
    
    try:
        bot.send_dice(chat_id = message.chat.id)
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Error sending dice to chat {chat_id}: {e}")

@bot.edited_message_handler(commands = ['noice'])
def send_edit_message(message):
    bot.send_message(chat_id=message.chat.id, text= 'WOW! I saw what you did')  

@bot.edited_message_handler(commands = ['close'])
def close_message(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(chat_id=message.chat.id, text= 'Good riddence!', reply_markup=markup)  
        
@bot.message_handler(commands = ['game'])
def send_game_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton("/greet")
    btn2 = types.KeyboardButton("/hello")
    btn3 = types.KeyboardButton("/close")  
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id=message.chat.id, text= 'What do you want?', reply_markup=markup)  
#
@bot.message_handler(commands = ['price'])
def get_crypto_prices():
    response = requests.get(COINGECKO_API_URL, params={"ids": "bitcoin,ethereum", "vs_currencies": "usd"})
    if response.status_code == 200:
        data = response.json()
        btc_price = data["bitcoin"]["usd"]
        eth_price = data["ethereum"]["usd"]
        time_btc = datetime.fromtimestamp(data["bitcoin"]["last_updated_at"]).strftime("%Y-%m-%d %H:%M:%S")
        time_eth = datetime.fromtimestamp(data["ethereum"]["last_updated_at"]).strftime("%Y-%m-%d %H:%M:%S")
        bot.reply_to(f"BTC Price: ${btc_price} updated at {time_btc} \
                                        \nETH Price: ${eth_price} updated at {time_eth}")
    else:
        return "Sorry, something went wrong. Please try again later."



def main():
    bot.polling() # looking for message

if __name__ == '__main__':
    main() 