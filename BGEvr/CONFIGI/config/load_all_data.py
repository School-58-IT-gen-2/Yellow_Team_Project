import json
class LoadData:
    def __init__(self,path):
        self.path = path
        with open(self.path, "r",encoding = 'utf-8') as f:
            self.file = json.load(f)
    
    def load_token(self):
        return self.file["token"]
    
    def load_player_id(self):
        return self.file["player_id"]