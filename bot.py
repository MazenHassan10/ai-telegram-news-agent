from telegram.ext import ApplicationBuilder, CommandHandler
from db import init_db, add_topic, remove_topic, get_topics
import os
from dotenv import load_dotenv

load_dotenv()  # <-- this loads .env into os.environ

BOT_TOKEN = os.environ["BOT_TOKEN"]

init_db()

async def add(update, context):
    topic = " ".join(context.args).lower()
    add_topic(topic)
    await update.message.reply_text(f"✅ Added: {topic}")

async def remove(update, context):
    topic = " ".join(context.args).lower()
    remove_topic(topic)
    await update.message.reply_text(f"🗑 Removed: {topic}")

async def list_topics(update, context):
    topics = get_topics()
    await update.message.reply_text("📌 Topics:\n" + "\n".join(topics))

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("remove", remove))
    app.add_handler(CommandHandler("list", list_topics))
    app.run_polling()

if __name__ == "__main__":
    main()
