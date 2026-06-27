import os
import threading
from flask import Flask
import telebot
from telebot.types import ReplyKeyboardMarkup

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

def language_menu():
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("🇮🇷 فارسی", "🇬🇧 English")
    return menu

def fa_menu():
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("🛂 مشاوره مهاجرت", "🏠 اخذ اقامت")
    menu.add("🏢 ثبت شرکت", "💶 سرمایه‌گذاری")
    menu.add("📞 ارتباط با مشاور", "🔗 کانال رسمی")
    menu.add("🌐 تغییر زبان")
    return menu

def en_menu():
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("🛂 Immigration Consultation", "🏠 Residency")
    menu.add("🏢 Company Registration", "💶 Investment")
    menu.add("📞 Contact Advisor", "🔗 Official Channel")
    menu.add("🌐 Change Language")
    return menu

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🌍 به STAR BALKAN خوش آمدید\nWelcome to STAR BALKAN\n\nلطفاً زبان خود را انتخاب کنید:\nPlease choose your language:",
        reply_markup=language_menu()
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    chat_id = message.chat.id

    if text == "🇮🇷 فارسی":
        bot.send_message(chat_id, "لطفاً یکی از خدمات را انتخاب کنید:", reply_markup=fa_menu())

    elif text == "🇬🇧 English":
        bot.send_message(chat_id, "Please choose one of our services:", reply_markup=en_menu())

    elif text == "🛂 مشاوره مهاجرت":
        bot.send_message(chat_id, "🛂 مشاوره مهاجرت\n\nلطفاً نام، سن، کشور مقصد و شماره تماس خود را ارسال کنید.")

    elif text == "🏠 اخذ اقامت":
        bot.send_message(chat_id, "🏠 اخذ اقامت اروپا\n\nبرای بررسی مسیرهای اقامت اروپا با ما در ارتباط باشید.")

    elif text == "🏢 ثبت شرکت":
        bot.send_message(chat_id, "🏢 ثبت شرکت\n\nلطفاً کشور موردنظر و نوع فعالیت خود را ارسال کنید.")

    elif text == "💶 سرمایه‌گذاری":
        bot.send_message(chat_id, "💶 سرمایه‌گذاری\n\nلطفاً میزان سرمایه و کشور موردنظر خود را ارسال کنید.")

    elif text == "📞 ارتباط با مشاور":
        bot.send_message(chat_id, "📞 ارتباط با مشاور\n\nتلگرام:\n@StarBalkanVisa")

    elif text == "🔗 کانال رسمی":
        bot.send_message(chat_id, "🔗 کانال رسمی STAR BALKAN:\nhttps://t.me/StarBalkanVisa")

    elif text == "🛂 Immigration Consultation":
        bot.send_message(chat_id, "🛂 Immigration Consultation\n\nPlease send your name, age, destination country, and phone number.")

    elif text == "🏠 Residency":
        bot.send_message(chat_id, "🏠 European Residency\n\nContact us to review European residency options.")

    elif text == "🏢 Company Registration":
        bot.send_message(chat_id, "🏢 Company Registration\n\nPlease send your target country and business activity.")

    elif text == "💶 Investment":
        bot.send_message(chat_id, "💶 Investment\n\nPlease send your investment amount and preferred country.")

    elif text == "📞 Contact Advisor":
        bot.send_message(chat_id, "📞 Contact Advisor\n\nTelegram:\n@StarBalkanVisa")

    elif text == "🔗 Official Channel":
        bot.send_message(chat_id, "🔗 Official STAR BALKAN Channel:\nhttps://t.me/StarBalkanVisa")

    elif text in ["🌐 تغییر زبان", "🌐 Change Language"]:
        bot.send_message(chat_id, "لطفاً زبان را انتخاب کنید:\nPlease choose your language:", reply_markup=language_menu())

    else:
        bot.send_message(chat_id, "لطفاً از دکمه‌های منو استفاده کنید.\nPlease use the menu buttons.")

@app.route("/")
def home():
    return "STAR BALKAN bot is running."

def run_bot():
    bot.infinity_polling(skip_pending=True)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
