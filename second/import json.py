import json
import os

print("ssasas")
print("\033[H\033[J")
print("Загрузка данных")

with open("save.json", "r") as f:
  data = json.load(f)
  f.close()

while True:
  if data["hash"] == 0:
    print("Вы получили достижение: Welcome!")
    data["ach"].append("Welcome!")

  elif data["hash"] == 100:
    print("Вы получили достижение: Первая сотня!!")
    data["ach"].append("100!")
    
  print(f"Вы накликали: {data['hash']}")
  data["hash"] +=1
  
  with open("save.json", "w") as f:
    json.dump(data, f)
    f.close()
    
  a = input()
  print("\033[H\033[J")
  
  if a == "exit":
    break
    
  if a == "ach":
    for i in data["ach"]:
      print(i, "\n")
  