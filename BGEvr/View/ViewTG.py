from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Contact,Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler,CallbackQueryHandler
from telegram.files.inputmedia import InputMediaPhoto
from database_adapter import *
import os

class ViewTG():
    def __init__(self,user_id,bot_id):
        self.bot_id = bot_id
        self.user_id = user_id
        self.message = None
        self.file_size = None
        self._first_pic = True
    def send_pic(self,update:Update,callback:CallbackContext, user_id, message_id=None, db=None):
        bot = Bot(self.bot_id)
        self.user_id = user_id
        self.db = Adapter(schema_name="Yellow_team", host="85.208.86.99",
                          port="6432", dbname="sch58_db", sslmode=None, user="Admin", password="atdhfkm2024",
                          target_session_attrs="read-write")
        self.db.connect()
        self.last_img_id = self.db.select_by_user_id("user_info", user_id)[0][10]
        try:
            if self._first_pic and message_id==None:
                self.message = bot.send_photo(self.user_id,photo=open(f'players_images/{self.user_id}.png','rb'))
                self._first_pic = False
            else:
                media_file = InputMediaPhoto(open(f'players_images/{self.user_id}.png','rb'))
                file_size = os.path.getsize(f'players_images/{self.user_id}.png')
                #logger.warning(file_size)
                self.message = bot.edit_message_media(chat_id=self.user_id,message_id=self.last_img_id,media=media_file)
                self.file_size = file_size

            return self.message

        except Exception as error:
            #logger.critical(error)
            print(error)
            bot.send_message(self.user_id,"oh no, something did wrong :(")
