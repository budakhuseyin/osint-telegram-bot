from flask import Flask
from threading import Thread
from osint import start_command, help_command, osint_name, osint_mail, osint_phone, osint_user, token
from telegram.ext import ApplicationBuilder, CommandHandler

app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is running!"

def run():

    app_flask.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()


def main():
    if not token:
        print("Error: BOT_TOKEN not found!")
        return

    keep_alive()

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("osintname", osint_name))
    app.add_handler(CommandHandler("osintuser", osint_user))
    app.add_handler(CommandHandler("osintmail", osint_mail))
    app.add_handler(CommandHandler("osintphone", osint_phone))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
