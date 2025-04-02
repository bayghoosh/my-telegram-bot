from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters as Filters

def start(update: Update, context: CallbackContext):
    update.message.reply_text('سلام! به ربات من خوش اومدی! 😊')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"شما نوشتید: {update.message.text}")

def main():
    import os
    token = os.getenv('TOKEN') or "AAFdnqvhJu-AhgRu0oAEYpSwv0N9UfwwfKE"
    
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.TEXT & ~Filters.COMMAND, echo))
    
    updater.start_polling()
    updater.idle()

if name == 'main':  # 🚨 اصلاح این خط (با دو underline قبل و بعد از name)
    main()

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"شما نوشتید: {update.message.text}")

if name == 'main':
    main()
