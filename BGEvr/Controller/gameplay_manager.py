from Controller import Data_loader
from View import render
from PIL import Image

class Game():
    def __init__(self, user_id=-1):
        self.user_id = user_id
        self.data_loader = Data_loader.Data(self.user_id)
        self.user_data = self.data_loader.load_user_data()
        self.building_data = self.data_loader.load_game_data()
        self.render = render.Render()
        self.build_price = 0

    def create_house(self, name, position):
        self.building_data = self.data_loader.load_game_data()
        _building = self.building_data["buildings"][name]
        _map = self.user_data["map_data"]

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
            self.user_data["money"] -= self.build_price

            self.user_data["map_data"] = _map
            self.user_data["houses_data"].append(_building)
            print(_building["position"], "building complete pos")
            print(_building["position"], "Ready Pos\n\n")
            #print(self.user_data["houses_data"])
            self.data_loader.save_user_data()
            print(self.user_data)


        else:
            print("Can't Create")


    def check_can_build(self, maping):
        _map = self.user_data["map_data"]

        for i in range(len(maping)):
            for j in range(len(maping[i])):
                if _map[maping[i][0]][maping[i][1]] == 1:
                    return False
        return True

    def show_map(self):
        self.render.render(self.user_data).show()

    def save_pic(self):
        self.render.save_pic(self.user_id)

