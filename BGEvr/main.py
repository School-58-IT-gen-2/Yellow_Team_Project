'''import Controller.gameplay_manager
game = Controller.gameplay_manager.Game()
game.create_house(name="small_factory", position=[4,7])
game.create_house(name="small_factory", position=[3,4])
game.create_house(name="small_factory", position=[2,3])
game.create_house(name="small_house", position=[6, 4])

game.show_map()'''
from Model.player import *
Dima = Player("-1")
Dima.player_move("u")