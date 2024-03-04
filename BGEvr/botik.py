from CONFIGI.config.load_all_data import LoadData
from Model.player import *
from View.ViewTG import ViewTG
from Controller.Data_loader import Data
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Contact
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler,CallbackQueryHandler
import os
from dotenv import load_dotenv
from View.render import *
from Controller.Data_loader import *
#from database_adapter import *

load_dotenv()

class RunGameBot:
    def __init__(self):
        self.render = Render()
        self.txt = ''
        self.player_view =None
        self.token = os.getenv("TOKEN")
        self.player = None
        self.progress = None
        self.game_data = None
        self.data_loader = None
        self.used_keyboard = []
        self.main_keyboard = [
            [InlineKeyboardButton("статистика", callback_data='info')],
            [InlineKeyboardButton("построить", callback_data='build')],
            [InlineKeyboardButton("🔼", callback_data='u')],
            [InlineKeyboardButton("◀️",callback_data="l"),
             InlineKeyboardButton("▶️",callback_data="r")],
            [InlineKeyboardButton("🔽", callback_data='d')],
            [InlineKeyboardButton("следующий ход",callback_data="next_move")],
            #[InlineKeyboardButton("ЭТО МОДИФИКАЦИ АААААААААААААААААААА",callback_data='mod')]
        ]
        self.build_keyboard = [
            [InlineKeyboardButton(f"домик - 10 кириешек", callback_data='house_lvl_1')],
            [InlineKeyboardButton("заводик - 20 кириешек", callback_data='factory')],
            [InlineKeyboardButton("банк - 15 кириешек", callback_data='bank')],
            [InlineKeyboardButton("улучшить выбранное строение - 20 кириешек", callback_data='upgrade')],
            [InlineKeyboardButton("назад", callback_data='main_page')]
        ]



    def play_game(self,update : Update,context:CallbackContext):
        self.used_keyboard = self.main_keyboard
        self.user = update.message.from_user
        self.data_loader = Data(self.user.id)
        self.game_data = self.data_loader.load_game_data()
        self.progress = self.data_loader.load_user_data()
        self.player = Player(self.user.id)
        self.render.render(self.player.progress)
        self.render.save_pic(self.user.id)
        self.player_view = ViewTG(self.user.id,self.token)
        self.player_view.send_pic(update=update,callback=CallbackContext)
        reply_markup = InlineKeyboardMarkup(self.used_keyboard)
        update.message.reply_text(f"Чё делать будешь? \n {self.txt}",reply_markup=reply_markup)
    def move_button(self,update:Update,context:CallbackContext):
        query = update.callback_query
        query.answer()
        print(query.data)
        #if query.data == 'mod':
        #    self.txt += ",".join(self.dataloader.load_player_id())
        if query.data == 'build':
            self.used_keyboard = self.build_keyboard
        if query.data == 'main_page':
            self.used_keyboard = self.main_keyboard
        if query.data == 'info':
            self.txt += self.player.player_info()
        if query.data == 'u':
            self.player.player_move("u")
        if query.data == 'r':
            self.player.player_move("r")
        if query.data == 'l':
            self.player.player_move("l")
        if query.data == 'd':
            self.player.player_move("d")
        if query.data == 'factory':
            self.player.build_smth("small_factory")
            self.txt += f'Вы протратили много кириешек,зайдите в статистику для того, чтобы узнать сколько у вас осталось'
        if query.data == 'house_lvl_1':
            self.player.build_smth("small_house")
            self.txt += f'Вы протратили очень много кириешек,зайдите в статистику для того, чтобы узнать сколько у вас осталось'
        if query.data == 'bank':
            self.player.build_smth("small_shop")
            self.txt += f'Вы протратили достаточно кириешек,зайдите в статистику для того, чтобы узнать сколько у вас осталось'
        self.render.render(self.player.progress)
        self.render.save_pic(self.user.id)
        self.player_view.send_pic(Update,CallbackContext)
        update.callback_query.message.edit_text(f"Чё делать будешь? \n {self.txt}",reply_markup=InlineKeyboardMarkup(self.used_keyboard))
        self.txt = ''