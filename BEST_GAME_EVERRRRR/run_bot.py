from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Contact
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler,CallbackQueryHandler
from botik import *
botik = RunGameBot()

def main():
    
    updater = Updater(botik.token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start',botik.play_game))
    dispatcher.add_handler(CallbackQueryHandler(botik.move_button))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()