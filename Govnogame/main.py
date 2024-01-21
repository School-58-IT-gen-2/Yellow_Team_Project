import json


def map_debug():
    with open('Map.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for i in data:
        for j in data[i]:
            data[i][j]["debug_cords"] = [i, j]


    with open('Map.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

from Initial import Data_loader

loader = Data_loader.Data()

user = loader.load_user_data()

print(user)