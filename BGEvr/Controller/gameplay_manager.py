from Controller.Data_loader import Data
from View import render
from PIL import Image
from database_adapter import *
import json
class Game():
    def __init__(self, user_id,db,player):
        self.player = player
        self.db = db
        self.user_id = user_id
        self.data_loader = Data(self.user_id)
        self.building_data = self.data_loader.load_game_data()
        self.render = render.Render(self.db,self.user_id)

    def create_house(self, name, position):
        _building = self.building_data["buildings"][name]
        #_map = self.user_data["map_data"]



        with open("resources.json", encoding="utf-8") as f:
            house_res = json.load(f)



        map_posing = []
        for i in range(_building["size"]):
            _pos = [position[0]+i]
            _pos.append(position[1]+i)
            map_posing.append(_pos)
        if self.check_can_build():
            _building["position"] = map_posing[0]
            self.build_price = _building["price"]
            if self.player.player_money >= self.build_price:
                self.player.player_money -= self.build_price

                #self.user_data["map_data"] = _map
                #self.user_data["houses_data"].append(_building)
                _house_id = self.db.insert_batch("houses",[{"type" : _building["type"].split("_")[1],"pos_x" : self.player.player_pos_x,"pos_y" : self.player.player_pos_y,"house_level" : 1}],id_name = 'id')[0]
                str_of_houses = self.db.select_by_user_id("user_info",self.user_id)[0][3]
                if str_of_houses == 'no_buildings':
                    str_of_houses = str(_house_id[0]) 
                else:
                    t = str_of_houses.split(",")
                    t.append(str(_house_id[0]))
                    str_of_houses = f"'{",".join(t)}'"
                building_request = f"""house_id = {str_of_houses},money={self.player.player_money}"""
                self.db.update_by_user_id("user_info",building_request,self.user_id)
            #print(_building["position"], "building complete pos")
            #print(_building["position"], "Ready Pos\n\n")
            #print(self.user_data["houses_data"])
            #self.data_loader.save_user_data()
            #print(self.user_data)

        else:
            print("Can't Create")


    def check_can_build(self):
        _res_1 = True
        _res_2 = True
        _houses_id = self.db.select_by_user_id("user_info",self.user_id)[0][3]
        if _houses_id == 'no_buildings':
            return True
        _houses_id = list(map(int,_houses_id.split(',')))
        _res_id = list(map(int,self.db.select_by_user_id("user_info",self.user_id)[0][13].split(',')))
        player_pos_x = self.db.select_by_user_id("user_info",self.user_id)[0][0]
        player_pos_y = self.db.select_by_user_id("user_info",self.user_id)[0][1]
        houses_data = self.db.select("houses")
        res_data = self.db.select("resources")
        for i in houses_data:
            for j in _houses_id:
                if j in i:
                    if player_pos_x == i[1] and player_pos_y == i[2]:
                        _res_1 = False
                        break
        for i in res_data:
            for j in _res_id:
                if j in i:
                    if player_pos_x == i[1] and player_pos_y == i[2]:
                        _res_2 = False
                        break

        return (_res_1 and _res_2)

    def show_map(self):
        self.render.render(self.user_data).show()

    def save_pic(self):
        self.render.save_pic(self.user_id)






    """def delete_house(self,player_x,player_y):
        user_houses = self.db.select_by_user_id("user_info",self.user_id)[0][3]
        if user_houses == 'no_buildings':
            return 
        user_houses = list(map(int,user_houses.split(',')))
        #print(user_houses)
        for i in range(len(user_houses)):
            t = self.db.select_by_house_id("houses",user_houses[i])
            if t != []:
                print(t)
                if t[0][1] == player_x and t[0][2] == player_y:
                    self.db.delete_by_house_id("houses",t[0][4])
                k = f'{",".join(list(map(str,user_houses))).replace(str(user_houses[i]),'')}'
                print(k) # баги в этой штуке, появляется запятая дибильная >:(
                if k[0] == ',':
                    t = list(k)
                    t[0] = ''
                    k = ",".join(t)
                if k[-1] == ',':
                    t = list(k)
                    t[-1] = ''
                    k = ",".join(t)
                req = f""house_id = {k}""
                if req != "house_id = ''":
                    self.db.update_by_user_id("user_info",req,self.user_id)
                else:
                    self.db.update_by_user_id("user_info",""house_id = 'no_buildings'"",self.user_id)
            else:
                k = f'{",".join(list(map(str,user_houses))).replace(str(user_houses[i]),'')}'
                print(k)
                if k[0] == ',':
                    t = list(k)
                    t[0] = ''
                    k = ",".join(t)
                if k[-1] == ',':
                    t = list(k)
                    t[-1] = ''
                    k = ",".join(t)
                req = f""house_id = {k}""
                if req != "house_id = ''":
                    self.db.update_by_user_id("user_info",req,self.user_id)
                else:
                    self.db.update_by_user_id("user_info",""house_id = 'no_buildings'"",self.user_id)"""
    def upgrade_house(self,player_x,player_y):
        user_houses = self.db.select_by_user_id("user_info",self.user_id)[0][3]
        if user_houses == 'no_buildings':
            return 
        user_houses = list(map(int,user_houses.split(',')))
        #print(user_houses)
        for i in range(len(user_houses)):
            t = self.db.select_by_house_id("houses",user_houses[i])
            if t != []:
                print(t)
                if t[0][1] == player_x and t[0][2] == player_y:
                    if t[0][3] >=3:
                        return "больше нельзя строить - максимальный уровень"
                    else:
                        new_level = t[0][3] + 1
                    #print(t[0][3],'  ',new_level)
                    req = f"""house_level = {new_level}"""
                    self.db.update_by_house_id("houses",req,t[0][4])
                    break

        return f"Вы увеличили уровень данного сооружения на 1,\nтеперь его уровень - {new_level}"



