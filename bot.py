import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask
import threading

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def language_menu():
markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton("🇮🇷 فارسی"), KeyboardButton("🇬🇧 English"))
return markup

def fa_menu():
markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add("🛂 مشاوره مهاجرت", "🏠 اخذ اقامت")
markup.add("🏢 ثبت شرکت", "💶 سرمایه‌گذاری")
markup.add("📞 ارتباط با مشاور", "🔗 کانال رسمی")
markup.add("🌐 Change Language")
return markup

def en_menu():
markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add("🛂 Immigration Consultation", "🏠 Residency")
markup.add("🏢 Company Registration", "💶 Investment")
markup.add("📞 Contact Advisor", "🔗 Official Channel")
markup.add("🌐 تغییر زبان")
return markup

@bot.message_handler(commands=["start"])
def start(message):
bot.send_message(
message.chat.id,
"🌍 به STAR BALKAN خوش آمدید\nWelcome to STAR BALKAN\n\nلطفاً زبان خود را انتخاب کنید:\nPlease choose your language:",
reply_markup=language_menu()
)

@bot.message_handler(func=lambda m: True)
def reply(message):
text = message.text
chat_id = message.chat.id

if text == "🇮🇷 فارسی":
    bot.send_message(chat_id, "زبان فارسی انتخاب شد.\nلطفاً یکی از خدمات را انتخاب کنید:", reply_markup=fa_menu())

elif text == "🇬🇧 English":
    bot.send_message(chat_id, "English selected.\nPlease choose one of our services:", reply_markup=en_menu())

elif text == "🛂 مشاوره مهاجرت":
    bot.send_message(chat_id, "🛂 مشاوره مهاجرت\n\nبرای بررسی شرایط مهاجرت، لطفاً نام، سن، کشور مقصد و شماره تماس خود را ارسال کنید.")

elif text == "🏠 اخذ اقامت":
    bot.send_message(chat_id, "🏠 اخذ اقامت اروپا\n\nSTAR BALKAN در زمینه بررسی مسیرهای اقامت اروپا راهنمایی ارائه می‌دهد.")

elif text == "🏢 ثبت شرکت":
    bot.send_message(chat_id, "🏢 ثبت شرکت\n\nبرای اطلاعات درباره ثبت شرکت در اروپا، لطفاً کشور موردنظر و نوع فعالیت خود را ارسال کنید.")

elif text == "💶 سرمایه‌گذاری":
    bot.send_message(chat_id, "💶 سرمایه‌گذاری\n\nبرای بررسی فرصت‌های سرمایه‌گذاری، لطفاً میزان سرمایه و کشور موردنظر را ارسال کنید.")

elif text == "📞 ارتباط با مشاور":
    bot.send_message(chat_id, "📞 ارتباط با مشاور\n\nبرای ارتباط مستقیم، لطفاً پیام خود را ارسال کنید.\nتلگرام: @StarBalkanVisa")

elif text == "🔗 کانال رسمی":
    bot.send_message(chat_id, "🔗 کانال رسمی STAR BALKAN:\nhttps://t.me/StarBalkanVisa")

elif text == "🛂 Immigration Consultation":
    bot.send_message(chat_id, "🛂 Immigration Consultation\n\nPlease send your name, age, destination country, and phone number.")

elif text == "🏠 Residency":
    bot.send_message(chat_id, "🏠 European Residency\n\nSTAR BALKAN provides guidance for European residency options.")

elif text == "🏢 Company Registration":
    bot.send_message(chat_id, "🏢 Company Registration\n\nPlease send your target country and business activity.")

elif text == "💶 Investment":
    bot.send_message(chat_id, "💶 Investment Opportunities\n\nPlease send your investment amount and preferred country.")

elif text == "📞 Contact Advisor":
    bot.send_message(chat_id, "📞 Contact Advisor\n\nTelegram: @StarBalkanVisa")

elif text == "🔗 Official Channel":
    bot.send_message(chat_id, "🔗 Official STAR BALKAN Channel:\nhttps://t.me/StarBalkanVisa")

elif text in ["🌐 Change Language", "🌐 تغییر زبان"]:
    bot.send_message(chat_id, "Please choose your language:\nلطفاً زبان خود را انتخاب کنید:", reply_markup=language_menu())

else:
    bot.send_message(chat_id, "لطفاً از دکمه‌های منو استفاده کنید.\nPlease use the menu buttons.")

app = Flask(name)

@app.route("/")
def home():
return "STAR BALKAN bot is running."

def run_bot():
bot.infinity_polling()

threading.Thread(target=run_bot).start()

if name == "main":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
