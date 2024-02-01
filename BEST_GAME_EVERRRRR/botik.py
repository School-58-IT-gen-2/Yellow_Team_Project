from CONFIGI.config.load_all_data import LoadData
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Contact
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler,CallbackQueryHandler
class RunGameBot:
    def __init__(self):
        self.txt = ''
        self.dataloader = LoadData("BEST_GAME_EVERRRRR/CONFIGI/data/bot_data.json")
        self.token = self.dataloader.load_token()
        self.keyboard = [
            [InlineKeyboardButton("статистика", callback_data='info')],
            [InlineKeyboardButton("построить", callback_data='build')],
            [InlineKeyboardButton("🔼", callback_data='u')],
            [InlineKeyboardButton("◀️",callback_data="l"),
             InlineKeyboardButton("▶️",callback_data="r")],
            [InlineKeyboardButton("🔽", callback_data='d')],
            [InlineKeyboardButton("следующий ход",callback_data="next_move")],
            [InlineKeyboardButton("ЭТО МОДИФИКАЦИ АААААААААААААААААААА",callback_data='mod')]
        ]


    def play_game(self,update : Update,context:CallbackContext):
        reply_markup = InlineKeyboardMarkup(self.keyboard)
        update.message.reply_text(f"Чо делать будешь? \n {self.txt}",reply_markup=reply_markup)
    def move_button(self,update:Update,context:CallbackContext):
        query = update.callback_query
        query.answer()
        print(query.data)
        if query.data == 'mod':
            self.txt += ",".join(self.dataloader.load_player_id())
        else:
            self.txt += query.data
        update.callback_query.message.edit_text(f"Чо делать будешь? \n {self.txt}",reply_markup=InlineKeyboardMarkup(self.keyboard))
        self.txt = ''