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
from database_adapter import *
from datetime import datetime
from Model import player
load_dotenv()

class RunGameBot:
    def __init__(self):
        self.new_gamer = False
        self.txt = ''
        self.player_view =None
        self.token = os.getenv("TOKEN")
        self.player = None
        self.progress = None
        self.game_data = None
        self.data_loader = None
        self.db = Adapter(schema_name="Yellow_Team_Project",host="rc1d-9cjee2y71olglqhg.mdb.yandexcloud.net",port="6432",dbname="sch58_db",sslmode=None,user="Admin",password="atdhfkm2024",target_session_attrs="read-write")
        self.db.connect()
        self.render = Render
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
        _res = 0
        for i in self.db.select("user_info"):
            if self.user.id in i:
                _res += 1
        if _res == 0:
            self.db.insert_batch("user_info",[{"pos_x" : 1,"pos_y" : 1, "units" : 10, "house_id" : 'no_buildings', "chat_id" : self.user.id,"user_id" : self.user.id,"created" : int(datetime.now().timestamp()), "updated" : int(datetime.now().timestamp()),"money" : 100,"user_nickname" : self.user.full_name, "wood": 10, "iron": 10}],id_name='user_id')
        self.data_loader = Data(self.user.id)
        self.render = Render(self.db,self.user.id)
        self.game_data = self.data_loader.load_game_data()
        self.player = Player(self.user.id,self.db)
        self.render.render(self.player.progress, self.user.id)
        self.render.save_pic(self.user.id)
        self.player_view = ViewTG(self.user.id,self.token)
        self.player_view.send_pic(update=update,callback=CallbackContext, user_id=self.user.id)
        reply_markup = InlineKeyboardMarkup(self.used_keyboard)
        update.message.reply_text(f"Чё делать будешь? \n {self.txt}",reply_markup=reply_markup)



    def move_button(self,update:Update,context:CallbackContext):
        update_usage = False
        query = update.callback_query
        query.answer()
        print(query.data)
        self.player = Player(query.from_user.id, self.db)
        #if query.data == 'mod':
        #    self.txt += ",".join(self.dataloader.load_player_id())
        if query.data == 'next_move':
            self.player.next_turn(query.from_user.id)
            update_usage = True
        if query.data == 'build':
            self.used_keyboard = self.build_keyboard
        if query.data == 'main_page':
            self.used_keyboard = self.main_keyboard
        if query.data == 'info':
            self.txt += self.player.player_info(query.from_user.id)
        if query.data == 'u':
            self.player.player_move("u", query.from_user.id)
            update_usage = True
        if query.data == 'r':
            self.player.player_move("r", query.from_user.id)
            update_usage = True
        if query.data == 'l':
            self.player.player_move("l", query.from_user.id)
            update_usage = True
        if query.data == 'd':
            self.player.player_move("d", query.from_user.id)
            update_usage = True
        if query.data == 'factory':
            self.player.build_smth("small_factory", query.from_user.id)
            update_usage = True
            self.txt += f'Вы протратили много кириешек,зайдите в статистику для того, чтобы узнать сколько у вас осталось'
        if query.data == 'house_lvl_1':
            self.player.build_smth("small_house", query.from_user.id)
            update_usage = True
            self.txt += f'Вы протратили очень много кириешек,зайдите в статистику для того, чтобы узнать сколько у вас осталось'
        if query.data == 'bank':
            self.player.build_smth("small_shop", query.from_user.id)
            update_usage = True
            self.txt += f'Вы протратили достаточно кириешек,зайдите в статистику для того, чтобы узнать сколько у вас осталось'
        #self.player.next_turn()
        self.render.render(self.player.progress, query.from_user.id)
        self.render.save_pic(query.from_user.id)
        if update_usage:
            self.player_view.send_pic(Update,CallbackContext, query.from_user.id)
        #REQUEST = f"""var_1 = {...},var_2 = {...}"""
        get_request = f"""updated={int(datetime.now().timestamp())},pos_x = {self.player.player_pos_x},pos_y = {self.player.player_pos_y}"""
        self.db.update("user_info",get_request,self.user.id)
        update.callback_query.message.edit_text(f"Чё делать будешь? \n {self.txt}",reply_markup=InlineKeyboardMarkup(self.used_keyboard))
        self.txt = ''