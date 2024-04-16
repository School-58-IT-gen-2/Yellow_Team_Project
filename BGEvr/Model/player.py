from Controller.Data_loader import *
from Controller.gameplay_manager import *
from database_adapter import *
class Player:
    def __init__(self,user_id,db):
        self.db = db
        self.user_id = user_id
        self.game = Game(self.user_id,self.db,self)
        self.dataloader = Data(self.user_id)
        #self.progress = self.dataloader.load_user_data()
        print(self.db.select_by_user_id("user_info",self.user_id))
        self.player_pos_x = self.db.select_by_user_id("user_info",self.user_id)[0][0]
        self.player_pos_y = self.db.select_by_user_id("user_info",self.user_id)[0][1]
        self.player_money = self.db.select_by_user_id("user_info",self.user_id)[0][8]
        self.player_units = self.db.select_by_user_id("user_info",self.user_id)[0][2]
        self.progress = {"x" : self.player_pos_x,"y" : self.player_pos_y}
        t = self.db.select_by_user_id("user_info",self.user_id)[0][3]
        self.pay_for_turn = len(t.split(","))
        #print(self.pay_for_turn)

    def player_move(self,move, user_id):
        db = Adapter(schema_name="Yellow_Team_Project", host="rc1d-9cjee2y71olglqhg.mdb.yandexcloud.net",
                          port="6432", dbname="sch58_db", sslmode=None, user="Admin", password="atdhfkm2024",
                          target_session_attrs="read-write")
        db.connect()
        player_pos_x = db.select_by_user_id("user_info", user_id)[0][0]
        player_pos_y = db.select_by_user_id("user_info", user_id)[0][1]
        print(f"DO : x {player_pos_x} y {player_pos_y}")
        progress = {"x": player_pos_x, "y": player_pos_y}

        #print(len(self.progress["map_data"][0]))
        """self.progress = self.dataloader.load_user_data()
        if move == 'u' and self.progress["player_position"][1] > 0:
            self.progress["player_position"][1] -= 1 
        elif move == 'd' and self.progress["player_position"][1] < 8:
            self.progress["player_position"][1] += 1 
        elif move == 'r' and self.progress["player_position"][0] < 8:
            self.progress["player_position"][0] += 1 
        elif move == 'l ' and self.progress["player_position"][0] > 0:
            self.progress["player_position"][0] -= 1 
        else:
            print("куда валишь??77?7??777777?77?7")
        self.dataloader.save_user_data("""
        if move == 'u' and player_pos_x > 0:
            player_pos_x -= 1
        if move == 'd' and player_pos_x < 7:
            player_pos_x += 1
        if move == 'r' and player_pos_y < 7:
            player_pos_y += 1
        if move == 'l' and player_pos_y > 0:
            player_pos_y -= 1
        progress = {"x" : player_pos_x,"y" : player_pos_y}
        move_request = f"""pos_x = {player_pos_x},pos_y = {player_pos_y}"""
        db.update("user_info",move_request,user_id)
        print(f"POSLE : x {player_pos_x} y {player_pos_y}")
        
    
    def next_turn(self, user_id):
        houses_data = {
            "small_house": [0, 10],
            "small_factory": [10, 0]
        }

        self.db = Adapter(schema_name="Yellow_Team_Project", host="rc1d-9cjee2y71olglqhg.mdb.yandexcloud.net",
                          port="6432", dbname="sch58_db", sslmode=None, user="Admin", password="atdhfkm2024",
                          target_session_attrs="read-write")
        self.db.connect()
        
        self.player_money = self.db.select_by_user_id("user_info", user_id)[0][8]
        self.player_units = self.db.select_by_user_id("user_info", user_id)[0][2]
        self.player_money = self.db.select_by_user_id("user_info", user_id)[0][8]
        self.player_units = self.db.select_by_user_id("user_info", user_id)[0][2]

        user_houses = self.db.select_by_user_id("user_info", user_id)[0][3]
        if user_houses == "no_buildings":
            return
        user_houses = list(map(int, user_houses.split(',')))

        for i in user_houses:
            house = self.db.select_by_house_id(table="houses", house_id=i)[0][0]
            print(house)
            self.player_money += houses_data[house][0]
            self.player_units += houses_data[house][1]

        req = f"""money = {self.player_money},units = {self.player_units}"""
        self.db.update("user_info", req, id=user_id)

    
    def build_smth(self,buiding, user_id):
        self.game.create_house(buiding,[self.progress["x"],self.progress["y"]])

    def player_info(self, user_id):
        self.player_money = self.db.select_by_user_id("user_info",self.user_id)[0][8]
        self.player_units = self.db.select_by_user_id("user_info",self.user_id)[0][2]
        return f"Ваши кириешки, Милорд - {self.player_money}\nКоличество ваших жителей, Милорд - {self.player_units}"