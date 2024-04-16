from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Contact,Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler,CallbackQueryHandler
from telegram.files.inputmedia import InputMediaPhoto
import os

class ViewTG():
    def __init__(self,user_id,bot_id):
        self.bot_id = bot_id
        self.user_id = user_id
        self.message = None
        self.file_size = None
        self._first_pic = True
    def send_pic(self,update:Update,callback:CallbackContext, user_id):
        bot = Bot(self.bot_id)
        self.user_id = user_id
        try:
            if self._first_pic:
                self.message = bot.send_photo(self.user_id,photo=open(f'players_images/{self.user_id}.png','rb'))
                self._first_pic = False
            else:
                media_file = InputMediaPhoto(open(f'players_images/{self.user_id}.png','rb'))
                file_size = os.path.getsize(f'players_images/{self.user_id}.png')
                #logger.warning(file_size)
                bot.edit_message_media(chat_id=self.user_id,message_id=self.message.message_id,media=media_file)
                self.file_size = file_size
        except Exception as error:
            #logger.critical(error)
            bot.send_message(self.user_id,"oh no, something did wrong :(")
    