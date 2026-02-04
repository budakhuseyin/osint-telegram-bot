# OSINT Search Telegram Bot

## Disclaimer
This tool is developed for educational and ethical security research purposes only. The developer is not responsible for any misuse or damage caused by this application. Users are required to comply with local and international laws regarding information gathering and privacy.

---

## Overview
This is a specialized Open Source Intelligence (OSINT) tool integrated with Telegram. It automates the process of reconnaissance by utilizing advanced search engine operators (Google Dorking) and direct link generation to identify digital footprints across various platforms.

## Core Features
- Name Search: Generates targeted queries to locate mentions of individuals in public records and social networks.
- Username Reconnaissance: Provides direct access to potential profiles on GitHub, X (Twitter), Instagram, Reddit, and TikTok.
- Email Intelligence: Identifies links between email addresses and public databases or developer platforms.
- Phone Number Investigation: Scours public directories and paste sites for references to specific phone numbers.

## Project Structure
- bot.py: The main entry point. Handles the Telegram bot initialization and manages the command handlers.
- requirements.txt: Specifies the Python dependencies for environment consistency.
- .env: Local configuration for sensitive credentials (API tokens).
- .gitignore: Ensures sensitive files like .env are not tracked by version control.

## Installation

1. Clone the repository:
   git clone https://github.com/budakhuseyin/osint-telegram-bot.git
   cd osint-telegram-bot

2. Install required dependencies:
   pip install -r requirements.txt

3. Configure Environment Variables:
   Create a .env file in the root directory:
   BOT_TOKEN=your_telegram_bot_token_here

## Command Reference

| Command | Argument | Description |
| :--- | :--- | :--- |
| /start | None | Initializes the bot session. |
| /help | None | Lists available commands and usage instructions. |
| /osintname | [Full Name] | Executes a name-based search across indexed sites. |
| /osintuser | [Username] | Verifies presence on major social media platforms. |
| /osintmail | [Email] | Investigates public data linked to the email address. |
| /osintphone | [Phone] | Checks for phone number mentions in public pastes. |

## Technical Stack
- Language: Python 3.x
- Framework: python-telegram-bot
- Environment: python-dotenv
- API: Telegram Bot API

## License
Distributed under the MIT License.
