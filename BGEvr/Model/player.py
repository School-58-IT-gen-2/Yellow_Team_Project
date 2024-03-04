from Controller.Data_loader import *
from Controller.gameplay_manager import *
class Player:
    def __init__(self,user_id):
        self.user_id = user_id
        self.game = Game(self.user_id)
        self.dataloader = Data(self.user_id)
        self.progress = self.dataloader.load_user_data()

    def player_move(self,move):
        #print(len(self.progress["map_data"][0]))
        self.progress = self.dataloader.load_user_data()
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
        self.dataloader.save_user_data()
    
    def next_turn(self):
        pass
    
    def build_smth(self,buiding):
        self.game.create_house(buiding,self.progress["player_position"])
        self.player_move('d')

    def player_info(self):
        return f"{self.progress["money"]} - деняк, \n{self.progress["units"]} - жителей"
    
    