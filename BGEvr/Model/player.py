from Controller.Data_loader import *
from Controller.gameplay_manager import *
class Player:
    def __init__(self,user_id):
        self.user_id = user_id
        self.game = Game(self.user_id)
        self.dataloader = Data(self.user_id)
        self.progress = self.dataloader.load_user_data()

    def player_move(self,move):
        print(len(self.progress["map_data"][0]))
        if self.progress["player_position"][1] > 0 and self.progress["player_position"][1] <= len(self.progress["map_data"][0]) and self.progress["player_position"][0] > 0 and self.progress["player_position"][0] <= len(self.progress["map_data"][0]):
            if move == 'u':
                self.progress["player_position"][1] -= 1 
            if move == 'd':
                self.progress["player_position"][1] += 1 
            if move == 'r':
                self.progress["player_position"][0] += 1 
            if move == 'l':
                self.progress["player_position"][0] -= 1 
            self.dataloader.save_user_data()
        else:
            print("куда валишь??77?7??777777?77?7")
    
    def next_turn(self):
        pass
    
    def build_smth(self,buiding):
        if self.game.check_can_build():
            self.game.create_house(buiding,self.progress["player_position"])

    def player_info(self):
        return f"{self.progress["money"]} - деняк, \n{self.progress["units"]} - жителей"
    