from PIL import Image, ImageColor, ImageDraw

import random
class Render:
    def __init__(self,db,user_id):
        self._map = None
        self._one_point_size = 0
        self.db = db
        self.user_id = user_id

    def render(self, data):
        self._map = Image.new(mode="RGBA", size=(1080, 1080), color=(0,0,0))

        _map_size = 8 #data["map_size"]
        #_user_buildings = data["houses_data"]
        _ground = ['ground1.png', 'ground2.png', 'ground3.png', 'ground4.png']

        self._one_point_size = 1080//_map_size
        _selected = Image.open("./res/selected.png").resize((self._one_point_size, self._one_point_size))
        for i in range(_map_size):
            for j in range(_map_size):
                _cycle_ground = Image.open(f"./res/{_ground[random.randint(0, 3)]}").resize((self._one_point_size, self._one_point_size))
                self._map.paste(_cycle_ground, (i*self._one_point_size, j*self._one_point_size))
                if j == data["x"] and i == data["y"]:
                    self._map.paste(_selected,(i*self._one_point_size, j*self._one_point_size))
        self.render_houses_by_user_data()
        return self._map
    def save_pic(self,user_id):
        self._map.save(f"./players_images/{user_id}.png")



    def render_houses_by_user_data(self):
        _ground = ['ground1.png', 'ground2.png', 'ground3.png', 'ground4.png']
        user_houses = self.db.select_by_user_id("user_info",self.user_id)[0][3]
        print(user_houses)
        if user_houses == "no_buildings":
            return 
        user_houses = list(map(int,user_houses.split(',')))
        all_houses = self.db.select("houses")
        for i in all_houses:
            for j in user_houses:
                if j == i[-1]:
                    _pos_x = i[2]
                    _pos_y = i[1]
                    build_type = i[0]
                    _cycle_ground = Image.open(f"./res/{_ground[random.randint(0, 3)]}").convert(mode="RGBA").resize((self._one_point_size, self._one_point_size))
                    _house = Image.open(f"./res/{build_type}.png").convert(mode="RGBA").resize((self._one_point_size,self._one_point_size))
                    _cycle_ground.paste(_house,(0,0),_house)
                    self._map.paste(_cycle_ground,(_pos_x*self._one_point_size,_pos_y*self._one_point_size))




