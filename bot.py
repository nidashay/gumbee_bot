from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import random
import datetime

import os
TOKEN = os.environ.get("BOT_TOKEN")

# ===== COMMANDS =====

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey 👋 I'm GethiBot 🤖\n"
        "I can chat, give time, and help you.\n"
        "Try /help"
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/help - Show commands\n"
        "/time - Current time\n"
        "/about - About this bot"
    )


async def time_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f"🕒 Current time: {now}")


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 NidaBot\n"
        "Made with Python by Clinton\n"
        "Lightweight, free, and cool 😎"
    )


# ===== CHAT LOGIC =====

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "hello" in text or "hi" in text:
        replies = [
            "Hey there! 👋",
            "Hello 😄",
            "Hi! How can I help?"
        ]
        await update.message.reply_text(random.choice(replies))

    elif "how are you" in text:
        await update.message.reply_text("I'm doing great 😎 Thanks for asking!")

    elif "bye" in text:
        await update.message.reply_text("Bye 👋 See you later!")

    else:
        await update.message.reply_text(
            "Hmm 🤔 I don’t understand that yet.\n"
            "Try /help"
        )


# ===== MAIN =====

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("time", time_cmd))
    app.add_handler(CommandHandler("about", about))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
