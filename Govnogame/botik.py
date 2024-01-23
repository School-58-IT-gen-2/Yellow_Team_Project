from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Contact
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler,CallbackQueryHandler
class RunGameBot:
    def __init__(self):
        self.token = '6583693836:AAEROQHgoNPrYyv5ZPMaunNjxWx5P1k4oBI'
        self.keyboard = [
            [InlineKeyboardButton("статистика", callback_data='info')],
            [InlineKeyboardButton("построить", callback_data='build')],
            [InlineKeyboardButton("🔼", callback_data='u')],
            [InlineKeyboardButton("◀️",callback_data="l"),
             InlineKeyboardButton("▶️",callback_data="r")],
            [InlineKeyboardButton("🔽", callback_data='d')],
            [InlineKeyboardButton("следующий ход",callback_data="next_move")]
        ]


    def play_game(self,update : Update,context:CallbackContext):
        reply_markup = InlineKeyboardMarkup(self.keyboard)
        update.message.reply_text("Чо делать будешь?",reply_markup=reply_markup)

    def move_button(self,update:Update,context:CallbackContext):
        query = update.callback_query
        query.answer()
        print(query.data)