from Controller import Data_loader
from View import render

class Game():
    def __init__(self, user_id=-1):
        self.data_loader = Data_loader.Data()
        self.user_data = self.data_loader.load_user_data(user_id=user_id)
        self.building_data = self.data_loader.load_game_data()
        self.render = render.Render()

    def create_house(self, name, position):
        _building = self.building_data["buildings"][name]
        _map = self.user_data["map_data"]

        map_posing = []
        for i in range(_building["size"]-1):
            _pos = [i+position[0]]
            _pos.append(i+position[1])
            map_posing.append(_pos)

        if self.check_can_build(map_posing):
            print("True")
            _building["position"] = position

            self.user_data["houses_data"].append(_building)
            self.data_loader.save_user_data(user_id=-1, data=self.user_data)

            self.render.render(self.user_data)
        else:
            print("False")

    def check_can_build(self, maping):
        _map = self.user_data["map_data"]

        for i in range(len(maping)):
            for j in range(len(maping[i])):
                print(maping)
                if _map[maping[i][0]][maping[i][1]] == 1:
                    return False
        return True

