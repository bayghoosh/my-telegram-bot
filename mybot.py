from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text('ربات با موفقیت راه‌اندازی شد!')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f'پیام شما: {update.message.text}')

def main():
    import os
    TOKEN = os.getenv('TOKEN', 'AAFdnqvhJu-AhgRu0oAEYpSwv0N9UfwwfKE')
    
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print('✅ ربات فعال شد!')
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
