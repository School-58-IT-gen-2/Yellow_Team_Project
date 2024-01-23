import asyncio
import Controller.gameplay_manager
import time
game = Controller.gameplay_manager.Game()
asyncio.run(game.create_house(name="small_factory", position=[4,4]))
asyncio.run(game.create_house(name="small_factory", position=[3,3]))
asyncio.run(game.create_house(name="small_factory", position=[2,2]))
asyncio.run(game.create_house(name="small_house", position=[0, 0]))

game.show_map()
print("я лох")
