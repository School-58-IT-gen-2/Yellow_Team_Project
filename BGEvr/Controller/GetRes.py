import random
class GetRes:
    def __init__(self,user_id,db):
        self.user_id = user_id
        self.db = db
        self.res_count = random.randint(3,5)
        self.res_list = ["tree","coal","copper"]
    def get_data(self):
        x = random.randint(0,7)
        y = random.randint(0,7)
        while x == y:
            x = random.randint(0,7)
            y = random.randint(0,7)
        return dict([("res_type",self.res_list[random.randint(0,2)]),("volume",100),("pos_x",x),("pos_y",y)])
    def generate_res(self):
        all_data = []
        user_resources = []
        for i in range(self.res_count):
            data = self.get_data()
            all_data.append(data)
            user_resources.append(self.db.insert_batch(table="resources",data=[all_data[i]],id_name="id")[0][0])
        all_user_res = ",".join(list(map(str,user_resources)))
        req = f"""res_id = '{all_user_res}'"""
        self.db.update_by_user_id("user_info",req,id=self.user_id)