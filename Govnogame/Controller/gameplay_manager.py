from Controller import Data_loader
from View import render

class Game():
    def __init__(self, user_id=-1):
        self.data_loader = Data_loader.Data()
        self.user_data = self.data_loader.load_user_data(user_id=user_id)
        self.building_data = self.data_loader.load_game_data()
        self.render = render.Render()

    async def create_house(self, name, position):
        _building = self.building_data["buildings"][name]
        _map = self.user_data["map_data"]

        map_posing = []
        for i in range(_building["size"]):
            _pos = [position[0]]
            _pos.append(position[1])
            map_posing.append(_pos)
        print(map_posing, "dsds")
        if self.check_can_build(map_posing):
            print("True")
            _building["position"] = position

            for i in range(len(map_posing)):
                _map[map_posing[i][0]][map_posing[i][1]] = 1
            self.user_data["map_data"] = _map
            self.user_data["houses_data"].append(_building)
            print(_building["position"])
            print(self.user_data["houses_data"])
            self.data_loader.save_user_data(user_id=-1, data=self.user_data)


        else:
            print("False")


    def check_can_build(self, maping):
        _map = self.user_data["map_data"]

        for i in range(len(maping)):
            for j in range(len(maping[i])):
                if _map[maping[i][0]][maping[i][1]] == 1:
                    return False
        return True

    def show_map(self):
        self.render.render(self.user_data)

