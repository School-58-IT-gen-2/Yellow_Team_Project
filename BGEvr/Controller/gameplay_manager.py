from Controller.Data_loader import Data
from View import render
from PIL import Image

class Game():
    def __init__(self, user_id,db,player):
        self.player = player
        self.db = db
        self.user_id = user_id
        self.data_loader = Data(self.user_id)
        self.building_data = self.data_loader.load_game_data()
        self.render = render.Render()

    def create_house(self, name, position):
        _building = self.building_data["buildings"][name]
        #_map = self.user_data["map_data"]

        map_posing = []
        for i in range(_building["size"]):
            _pos = [position[0]+i]
            _pos.append(position[1]+i)
            map_posing.append(_pos)
        print(map_posing, 'Mathed MapPos')
        if self.check_can_build(map_posing):
            print("Creating")
            _building["position"] = map_posing[0]
            self.build_price = _building["price"]
            print(_building["price"])
            self.player.player_money -= self.build_price

            #self.user_data["map_data"] = _map
            #self.user_data["houses_data"].append(_building)
            _house_id = self.db.insert_batch("houses",[{"type" : _building["type"],"pos_x" : self.player.player_pos_x,"pos_y" : self.player.player_pos_y,"house_level" : 1}])[0]
            str_of_houses = self.db.select_by_user_id("user_info",self.user_id)[3]
            if str_of_houses == 'no_buildings':
                str_of_houses = str(_house_id)
            else:
                str_of_houses += ','
                str_of_houses += str(_house_id)
            building_request = f"""house_id = {str_of_houses}"""
            
            self.db.update("user_info",building_request,self.user_id)
            #print(_building["position"], "building complete pos")
            #print(_building["position"], "Ready Pos\n\n")
            #print(self.user_data["houses_data"])
            #self.data_loader.save_user_data()
            #print(self.user_data)

        else:
            print("Can't Create")


    def check_can_build(self, maping):
        return 1

    def show_map(self):
        self.render.render(self.user_data).show()

    def save_pic(self):
        self.render.save_pic(self.user_id)

