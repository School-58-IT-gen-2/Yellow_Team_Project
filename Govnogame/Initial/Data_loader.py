#imports
import json


#Game Class
class Data():
    def __init__(self, user_id=-1):
        pass

    def load_user_data(self, user_id=-1):
        try:
            with open(f'saves/{user_id}.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        
        except:
            with open(f'saves/{user_id}.json', 'w', encoding='utf-8') as f:
                self.data = {
                    "position": [0, 0],
                    "inventory": [1, 2]
                }
                json.dump(self.data, f, ensure_ascii=False, indent=4)
        
        return self.data
        


