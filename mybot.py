from telegram import Update
     from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

     def start(update: Update, context: CallbackContext):
         update.message.reply_text('”·«„! »Â —»«  „‰ ŒÊ‘ «Ê„œÌ! ??')

     def main():
         updater = Updater("AAFdnqvhJu-AhgRu0oAEYpSwv0N9UfwwfKE", use_context=True)
         dispatcher = updater.dispatcher
         dispatcher.add_handler(CommandHandler("start", start))
         updater.start_polling()
         updater.idle()

     if name == 'main':
         main()