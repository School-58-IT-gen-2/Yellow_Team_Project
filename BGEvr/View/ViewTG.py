from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Contact,Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler,CallbackQueryHandler
from CONFIGI.config.load_all_data import LoadData


class ViewTG():
    def __init__(self,user_id):
        self._dataload = LoadData
        self.user_id = user_id
        #self.bot_id = self._dataload.load_token("BEST_GAME_EVERRRRR/CONFIGI/data/bot_data.json")["token"]
        self.bot_id = "6583693836:AAEROQHgoNPrYyv5ZPMaunNjxWx5P1k4oBI"
        self.bot =  Bot(self.bot_id)
    def send_pic(self,update : Update):
        self.bot.send_photo(self.user_id,photo=open(f'BGEvr/players_images/papa.png','rb'))
    