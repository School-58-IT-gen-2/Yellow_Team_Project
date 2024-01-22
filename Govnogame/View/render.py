from PIL import Image, ImageColor, ImageDraw
import random
class Render:
    def __init__(self):
        pass

    def render(self, data):
        _image = Image.new(mode="RGBA", size=(1080, 1080), color=000000)
        _image.show()

        _map_size = data["map_size"]
        _ground = ['ground1.png', 'ground2.png', 'ground3.png', 'ground4.png']

        _one_point_size = 1080//_map_size
        


