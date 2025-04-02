from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters

def start(update: Update, context: CallbackContext):
    update.message.reply_text('سلام! به ربات من خوش اومدی! 😊')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"شما نوشتید: {update.message.text}")

def main():
    import os
    token = os.getenv('TOKEN') or "AAFdnqvhJu-AhgRu0oAEYpSwv0N9UfwwfKE"
    
    updater = Updater(token)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("ربات در حال اجراست...")
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
