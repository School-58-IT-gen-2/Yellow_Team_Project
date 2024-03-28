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



    def player_move(self,move):
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
        if move == 'u' and self.player_pos_x > 0:
            self.player_pos_x -= 1
        if move == 'd' and self.player_pos_x < 8:
            self.player_pos_x += 1
        if move == 'r' and self.player_pos_y < 8:
            self.player_pos_y += 1
        if move == 'l' and self.player_pos_y > 0:
            self.player_pos_y -= 1
        self.progress = {"x" : self.player_pos_x,"y" : self.player_pos_y}
        move_request = f"""pos_x = {self.player_pos_x},pos_y = {self.player_pos_y}"""
        self.db.update("user_info",move_request,self.user_id)
        
    
    def next_turn(self):
        pass
    
    def build_smth(self,buiding):
        self.game.create_house(buiding,[self.progress["x"],self.progress["y"]])
        self.player_move('d')

    def player_info(self):
        return f"Ваши кириешки, Милорд - {self.player_money}\nКоличество ваших симпов, Милорд - {self.player_units}"
    
    