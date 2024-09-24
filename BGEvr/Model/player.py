from Controller.Data_loader import *
from Controller.gameplay_manager import *
from database_adapter import *
from Controller.GetRes import *
class Player:
    def __init__(self,user_id,db):
        self.db = db
        self.user_id = user_id
        self.gr = GetRes(self.user_id,self.db)
        self.game = Game(self.user_id,self.db,self)
        self.dataloader = Data(self.user_id)
        #self.progress = self.dataloader.load_user_data()
        print(self.db.select_by_user_id("user_info",self.user_id))
        self.player_pos_x = self.db.select_by_user_id("user_info",self.user_id)[0][0]
        self.player_pos_y = self.db.select_by_user_id("user_info",self.user_id)[0][1]
        self.player_money = self.db.select_by_user_id("user_info",self.user_id)[0][8]
        self.player_units = self.db.select_by_user_id("user_info",self.user_id)[0][2]
        self.player_res = self.db.select_by_user_id("user_info",self.user_id)[0][11]
        self.speed_mining = self.db.select_by_user_id("user_info",self.user_id)[0][13]
        self.player_level = 1
        self.turn_counter = self.db.select_by_user_id("user_info",self.user_id)[0][17]
        self.progress = {"x" : self.player_pos_x,"y" : self.player_pos_y}
        t = self.db.select_by_user_id("user_info",self.user_id)[0][3]
        self.pay_for_turn = len(t.split(","))
        #print(self.pay_for_turn)

    def convert_units_to_speed(self):
        self.player_units = self.db.select_by_user_id("user_info",self.user_id)[0][2]
        return int((self.player_units+4)/14.1014)

    def player_move(self,move, user_id):
        db = Adapter(schema_name="Yellow_team", host="85.208.86.99",
                          port="6432", dbname="sch58_db", sslmode=None, user="Admin", password="atdhfkm2024",
                          target_session_attrs="read-write")
        db.connect()
        player_pos_x = db.select_by_user_id("user_info", user_id)[0][0]
        player_pos_y = db.select_by_user_id("user_info", user_id)[0][1]
        #print(f"DO : x {player_pos_x} y {player_pos_y}")
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
        db.update_by_user_id("user_info",move_request,user_id)
        #print(f"POSLE : x {player_pos_x} y {player_pos_y}")
        
    
    def next_turn(self, user_id):
        self.send_kudos = False
        self.user_id = user_id
        self.turn_counter += 1
        houses_data = {
            "small_house": [0, 10],
            "small_factory": [10, 0],
            "middle_house": [5,25],
            "middle_factory": [25,0],
            "big_house": [10,50],
            "big_factory": [50,0],
            "small_bank": [0,0],
            "middle_bank":[0,0]
        }

        self.db = Adapter(schema_name="Yellow_team", host="85.208.86.99",
                          port="6432", dbname="sch58_db", sslmode=None, user="Admin", password="atdhfkm2024",
                          target_session_attrs="read-write")
        self.db.connect()
        
        self.player_money = self.db.select_by_user_id("user_info", user_id)[0][8]
        self.player_units = self.db.select_by_user_id("user_info", user_id)[0][2]
        self.player_money = self.db.select_by_user_id("user_info", user_id)[0][8]
        self.player_units = self.db.select_by_user_id("user_info", user_id)[0][2]

        user_houses = self.db.select_by_user_id("user_info", user_id)[0][3]
        
        if self.turn_counter % 4 == 3:
            t = self.gr.generate_res_by_turn(self.player_level)
            q = self.db.select_by_user_id("user_info",user_id)[0][11] + ',' + t
            #self.turn_counter = 0
            req = f"""res_id = '{q}',turn_counter = {self.turn_counter}"""
            #print(t)
            #print(q)
            #print(req)
            self.db.update_by_user_id("user_info", req, id=user_id)

        self.db.update_by_user_id("user_info",f"""turn_counter = {self.turn_counter}""",user_id)
        #self.previous_level = self.db.select_by_user_id("user_info",self.user_id)[0][18]
        if self.turn_counter in [10,25,50,100]:
            self.player_level += 1
            self.send_kudos = True
        else:
            self.send_kudos = False
        #etc

        if user_houses == "no_buildings":
            return
        user_houses = list(map(int, user_houses.split(',')))

        for i in user_houses:
            _house = self.db.select_by_house_id(table="houses", house_id=i)[0][4]
            house = ["small","middle","big"][self.db.select_by_house_id(table="houses", house_id=i)[0][3]-1] +"_"+ _house
            self.player_money += houses_data[house][0]
            self.player_units += houses_data[house][1]
        self.game.mine_resources()
        req = f"""money = {self.player_money + (100*self.player_level * self.send_kudos)},units = {self.player_units},player_level = {self.player_level},mining_speed={self.convert_units_to_speed()}"""
        self.db.update_by_user_id("user_info", req, id=user_id)
        if self.player_level == 4:
            return f"Поздравляю, вы прошли нашу игру.\n Вы потратили 185 ходов для этого и это круто, надеюсь Вам понравилось :)"
        if self.send_kudos:
            return f"Поздравляю, вы увеличили свой уровень на 1,теперь он стал {self.player_level} / 4\nИ в честь этого мы отправляем вам небольшой подарок - немного кириешек.\nУдачного миросозерцания :)"
        return f"Еще один ничего не значащий ход{"." * self.turn_counter}"
    
    def build_smth(self,buiding, user_id):
        return self.game.create_house(buiding,[self.progress["x"],self.progress["y"]])

    def player_info(self):
        self.player_money = self.db.select_by_user_id("user_info",self.user_id)[0][8]
        self.player_units = self.db.select_by_user_id("user_info",self.user_id)[0][2]
        return f"Ваш уровень - {self.player_level}\n\n\nДа и все..."
    


    """def delete_house(self):
        self.game.delete_house(self.player_pos_x,self.player_pos_y)
        self.player_money -= 15
        req = f""money = {self.player_money}""
        self.db.update_by_user_id("user_info",req,self.user_id)"""


    def update_house(self):
        self.player_money = self.db.select_by_user_id("user_info", self.user_id)[0][8]
        if self.player_money >= 100:
            self.player_money -= 100
            req = f"""money = {self.player_money}"""
            self.db.update_by_user_id("user_info",req,self.user_id)
            return self.game.upgrade_house(self.player_pos_x,self.player_pos_y)
        else:
            return "Нету денег :("
        
    def check_bank(self):
        user_houses = self.db.select_by_user_id("user_info", self.user_id)[0][3]
        if user_houses == "no_buildings":
            return 0
        user_houses = list(map(int, user_houses.split(',')))
        n = 0
        for i in user_houses:
            t = self.db.select_by_house_id("houses",i)[0]
            if t[0] == "bank":
                n += t[3]
        return n

    def trade(self,res_type):
        res = {"wood" : self.db.select_by_user_id("user_info",self.user_id)[0][10],
               "coal" : self.db.select_by_user_id("user_info",self.user_id)[0][11],
               "gold" : self.db.select_by_user_id("user_info",self.user_id)[0][16]}
        self.player_money += res[res_type] * (1+self.check_bank())//2
        res[res_type] = 0
        req = f"""coal = {res["coal"]},gold = {res["gold"]},wood = {res["wood"]},money = {self.player_money}"""
        self.db.update_by_user_id("user_info",req,self.user_id)
        return f"Вы успешно продали данный ресурс, на вашем балансе - {self.player_money} кириешек!"