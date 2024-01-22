#imports
import json


#Game Class
class Data():
    def __init__(self):
        pass

    def save_user_data(self, user_id=-1, data=None):
        with open(f'saves/{user_id}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_user_data(self, user_id=-1):
        try:
            with open(f'saves/{user_id}.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        
        except:
            with open(f'saves/{user_id}.json', 'w', encoding='utf-8') as f:
                self.data = {
                    "money":  100,
                    "units": 0,
                    "map": "default",
                    "map_size": 16,

                    "houses_data": [],
                    "map_data": self.create_map(size=16)
                }
                json.dump(self.data, f, ensure_ascii=False, indent=4)
        
        return self.data

    def create_map(self, size=16):
        map = []

        for i in range(size):
            map_x = []
            for j in range(size):
                map_x.append(0)
            map.append(map_x)
            print(map[i], "\n")

        return map

    def load_game_data(self):
        with open('Game_Data.json', 'r', encoding="utf-8") as f:
            data = json.load(f)

        return data

