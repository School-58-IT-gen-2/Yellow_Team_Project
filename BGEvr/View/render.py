from PIL import Image, ImageColor, ImageDraw
import random
class Render:
    def __init__(self):
        pass

    def render(self, data):
        _map = Image.new(mode="RGBA", size=(1080, 1080), color=000000)

        _map_size = data["map_size"]
        _user_buildings = data["houses_data"]
        _ground = ['ground1.png', 'ground2.png', 'ground3.png', 'ground4.png']

        _one_point_size = 1080//_map_size
        print(_one_point_size)

        for i in range(_map_size):
            for j in range(_map_size):
                _cycle_ground = Image.open(f"BGEvr/res/{_ground[random.randint(0, 3)]}").resize((_one_point_size, _one_point_size))
                _map.paste(_cycle_ground, (i*_one_point_size, j*_one_point_size))

        for i in range(len(_user_buildings)):
            _building_texture = Image.open(f'BGEvr/res/{_user_buildings[i]["texture"]}').resize((_one_point_size*_user_buildings[i]["size"], _one_point_size*_user_buildings[i]["size"]))
            _building_texture = _building_texture.convert('RGBA')
            _map.paste(_building_texture, (_user_buildings[i]["position"][0]*_one_point_size, _user_buildings[i]["position"][1]*_one_point_size), mask=_building_texture)

        _map.show()




