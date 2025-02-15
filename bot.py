print("Bot is running...")
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7600292732:AAF3Uwu9Rri3vVlCeXZn93y1rAlhCaGwhsM"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("سلام! من یه بات یادآوری هستم. از /set برای تنظیم یادآوری استفاده کن.")

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
