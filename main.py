from osint import start_command, help_command,osint_name,osint_mail,osint_phone,osint_user,token
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def main():
    if not token:
        print("Error: BOT_TOKEN not found in .env file")
        return

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("osintname", osint_name))
    app.add_handler(CommandHandler("osintuser", osint_user))
    app.add_handler(CommandHandler("osintemail", osint_mail))
    app.add_handler(CommandHandler("osintphone", osint_phone))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
