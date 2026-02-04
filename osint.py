from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.helpers import escape_markdown
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("BOT_TOKEN")

def build_search_url(query_text):
    encoded = urllib.parse.quote(query_text)
    return f"https://www.google.com/search?q={encoded}"

def build_site_filter(sites):
    # Daha temiz bir birleştirme yöntemi
    return " OR ".join([f"site:{s}" for s in sites])

def query_name(full_name):
    name = full_name.strip()
    social_sites = [
        "instagram.com", "facebook.com", "x.com", 
        "github.com", "linkedin.com", "tiktok.com"
    ]
    social_filter = build_site_filter(social_sites)

    items = [
        ("General", f'"{name}"'),
        ("Linkedin", f'site:linkedin.com/in "{name}"'),
        ("Github", f'site:github.com "{name}"'),
        ("Social (All)", f'"{name}" ({social_filter})')
    ]

    results = []
    for label, query_text in items:
        url = build_search_url(query_text)
        results.append((label, url))
    return results # Döngü bittikten sonra döndür

def username_queries(username):
    u = username.strip().lstrip("@").strip("/")
    return [
        ("Github", f"https://github.com/{u}"),
        ("X (Twitter)", f"https://x.com/{u}"),
        ("Instagram", f"https://instagram.com/{u}"),
        ("Reddit", f"https://reddit.com/user/{u}"),
        ("Tiktok", f"https://tiktok.com/@{u}"),
    ]

def email_queries(email):
    mail = email.strip()
    social_sites = ["instagram.com", "facebook.com", "x.com", "github.com", "linkedin.com", "tiktok.com"]
    social_filters = build_site_filter(social_sites)

    items = [
        ("General", f'"{mail}"'),
        ("Social", f'"{mail}" ({social_filters})'),
        ("Developer", f'"{mail}" site:github.com OR site:gitlab.com'),
        ("Paste", f'"{mail}" site:pastebin.com OR site:ghostbin.fun'),
        ("Forum", f'"{mail}" site:reddit.com OR site:stackoverflow.com')
    ]

    results = []
    for label, query_text in items:
        url = build_search_url(query_text)
        results.append((label, url))
    return results

def phone_queries(number):
    n = number.strip()
    items = [
        ("General", f'"{n}"'),
        ("Paste", f'"{n}" site:pastebin.com OR site:ghostbin.fun')
    ]
    results = []
    for label, query_text in items:
        url = build_search_url(query_text)
        results.append((label, url))
    return results

# --- Telegram Functions ---

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Hello\\, this is a OSINT bot\n\nYou can type /help to see how to use it\\."
    await update.message.reply_text(text, parse_mode="MarkdownV2")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "*OSINT HELP MENU*\n\n"
        "Commands you can use:\n"
        "/osintname `<name>` \\- search by name\n"
        "/osintuser `<username>` \\- search by username\n"
        "/osintmail `<email>` \\- search by email\n"
        "/osintphone `<phone>` \\- search by phone"
    )
    await update.message.reply_text(text, parse_mode="MarkdownV2")

async def send_results(update: Update, data, title):
    message = f"{title}\n\n"
    for i, (label, url) in enumerate(data, 1):
        safe_label = escape_markdown(label, version=2)
        # URL'leri Markdown formatında [Etiket](link) şeklinde gönderiyoruz
        message += f"{i}\\. [{safe_label}]({url})\n"

    await update.message.reply_text(message, parse_mode="MarkdownV2", disable_web_page_preview=True)

async def osint_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: `/osintname Full Name`", parse_mode="MarkdownV2")
        return
    full_name = " ".join(context.args)
    results = query_name(full_name)
    await send_results(update, results, f"*Search Results for:* {escape_markdown(full_name, 2)}")

async def osint_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: `/osintuser username`", parse_mode="MarkdownV2")
        return
    username = context.args[0]
    results = username_queries(username)
    await send_results(update, results, f"*Profile Links for:* {escape_markdown(username, 2)}")

async def osint_mail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: `/osintmail email@example.com`", parse_mode="MarkdownV2")
        return
    email = context.args[0]
    results = email_queries(email)
    await send_results(update, results, f"*Email Search for:* {escape_markdown(email, 2)}")

async def osint_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: `/osintphone 05xx`", parse_mode="MarkdownV2")
        return
    number = context.args[0]
    results = phone_queries(number)
    await send_results(update, results, f"*Phone Search for:* {escape_markdown(number, 2)}")

