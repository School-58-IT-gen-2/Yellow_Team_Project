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
from Controller.GetRes import *
load_dotenv()

class RunGameBot:
    def __init__(self):
        self.help_text = "Итак, вы попали в незабываемый и удивительный мир строительства - Industrio!\nВ ней вы можете ходить красным курсором, который представляет вашу безграничную силу, нажимая на стрелочки.\nТак же вы можете строить и улучшать дома построенные вами в вкладке 'строительство'\nНу и кнопка следующий ход - следующий ход, что сказать.\nЖелаем приятной игры, разработчики йеллоу тиме <3!"
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
        self.setting_keyboard = [
            [InlineKeyboardButton("хелп ми плз", callback_data='help')],
            [InlineKeyboardButton("новая игра", callback_data='new_game')],
            [InlineKeyboardButton("назад", callback_data='main_page')]]
        self.main_keyboard = [
            [InlineKeyboardButton("настройки", callback_data='settings')],
            [InlineKeyboardButton("построить", callback_data='build')],
            [InlineKeyboardButton("🔼", callback_data='u')],
            [InlineKeyboardButton("◀️",callback_data="l"),
             InlineKeyboardButton("▶️",callback_data="r")],
            [InlineKeyboardButton("🔽", callback_data='d')],
            [InlineKeyboardButton("следующий ход",callback_data="next_move")]
        ]
        self.build_keyboard = [
            [InlineKeyboardButton(f"домик - 10 кириешек", callback_data='house')],
            [InlineKeyboardButton("заводик - 20 кириешек", callback_data='factory')],
            [InlineKeyboardButton("банк - 15 кириешек", callback_data='bank')],
            [InlineKeyboardButton("улучшить выбранное строение - 100 кириешек", callback_data='upgrade')],
            #[InlineKeyboardButton("удалить выбранное строение - 15 кириешек", callback_data='delete')],
            [InlineKeyboardButton("назад", callback_data='main_page')]
        ]


    def play_game(self,update : Update,context:CallbackContext):
        self.used_keyboard = self.main_keyboard
        self.user = update.message.from_user
        self.generator_res = GetRes(self.user.id,self.db)
        _res = 0
        for i in self.db.select("user_info"):
            if self.user.id in i:
                _res += 1
        
        if _res == 0:
            user_res = self.generator_res.generate_res()
            self.db.insert_batch("user_info",[{"pos_x" : 1,"pos_y" : 1, "units" : 10, "house_id" : 'no_buildings', "chat_id" : self.user.id,"user_id" : self.user.id,"created" : int(datetime.now().timestamp()), "updated" : int(datetime.now().timestamp()),"money" : 100,"user_nickname" : self.user.full_name, "wood": 10, "iron": 10, "last_img_id": 0,"res_id" : user_res,"player_level" : 1}],id_name='user_id')
        self.data_loader = Data(self.user.id)
        self.render = Render(self.db,self.user.id)
        self.game_data = self.data_loader.load_game_data()
        self.player = Player(self.user.id,self.db)
        self.render.render(self.player.progress, self.user.id)
        self.render.save_pic(self.user.id)
        self.player_view = ViewTG(self.user.id,self.token)
        message = self.player_view.send_pic(update=update,callback=CallbackContext, user_id=self.user.id, message_id=None)
        reply_markup = InlineKeyboardMarkup(self.used_keyboard)
        update.message.reply_text(f"Чё делать будешь? \n {self.txt}",reply_markup=reply_markup)
        get_request = f"""updated={int(datetime.now().timestamp())},last_img_id = {message.message_id}"""
        self.db.update_by_user_id("user_info", get_request, self.user.id)



    def move_button(self,update:Update,context:CallbackContext):
        update_usage = False
        query = update.callback_query
        query.answer()
        print(query.data)
        player = Player(query.from_user.id, self.db)
        #if query.data == 'mod':
        #    self.txt += ",".join(self.dataloader.load_player_id())
        if query.data == 'settings':
            self.used_keyboard = self.setting_keyboard
        if query.data == 'new_game':
            t = self.db.select_by_user_id("user_info",self.user.id)[0][12]
            self.db.delete_by_user_id("user_info",self.user.id)
            user_res = self.generator_res.generate_res()
            self.db.insert_batch("user_info",[{"pos_x" : 1,"pos_y" : 1, "units" : 10, "house_id" : 'no_buildings', "chat_id" : self.user.id,"user_id" : self.user.id,"created" : int(datetime.now().timestamp()), "updated" : int(datetime.now().timestamp()),"money" : 100,"user_nickname" : self.user.full_name, "wood": 10, "iron": 10, "last_img_id": t,"res_id" : user_res,"player_level" : 1}],id_name='user_id')
            update_usage = True
        """if query.data == 'delete':
            self.player.delete_house()
            update_usage = True"""
        if query.data == 'help':
            self.txt += self.help_text
        if query.data == 'next_move':
            player.next_turn(query.from_user.id)
            print("Ходы игрока - ",player.turn_counter)
            update_usage = True
        if query.data == 'build':
            self.used_keyboard = self.build_keyboard
        if query.data == 'main_page':
            self.used_keyboard = self.main_keyboard
        if query.data == 'u':
            player.player_move("u", query.from_user.id)
            update_usage = True
        if query.data == 'r':
            player.player_move("r", query.from_user.id)
            update_usage = True
        if query.data == 'l':
            player.player_move("l", query.from_user.id)
            update_usage = True
        if query.data == 'd':
            player.player_move("d", query.from_user.id)
            update_usage = True
        if query.data == 'factory':
            player.build_smth("small_factory", query.from_user.id)
            update_usage = True
            #self.txt += f'Вы протратили много кириешек,зайдите в статистику для того, чтобы узнать сколько у вас осталось'
        if query.data == 'house':
            player.build_smth("small_house", query.from_user.id)
            update_usage = True
            #self.txt += f'Вы протратили очень много кириешек,зайдите в статистику для того, чтобы узнать сколько у вас осталось'
        if query.data == 'bank':
            player.build_smth("small_bank", query.from_user.id)
            update_usage = True
            #self.txt += "А фигушки, механика пока не работает :("

        if query.data == 'upgrade':
            self.txt+=self.player.update_house()
            update_usage = True
        #self.player.next_turn()
        self.render.render(self.player.progress, query.from_user.id)
        self.render.save_pic(query.from_user.id)
        if update_usage:
            self.player_view.send_pic(Update,CallbackContext, query.from_user.id, query.message.message_id, db=self.db)
        #REQUEST = f"""var_1 = {...},var_2 = {...}"""
        get_request = f"""updated={int(datetime.now().timestamp())}"""
        self.db.update_by_user_id("user_info",get_request,self.user.id)
        #if query.message.text != "Чё делать будешь?":
        update.callback_query.message.edit_text(f"Чё делать будешь?\n{self.txt}",reply_markup=InlineKeyboardMarkup(self.used_keyboard))
        self.txt = ''