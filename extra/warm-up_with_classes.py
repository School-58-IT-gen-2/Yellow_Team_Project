# -- часть Никиты --
class YellowList(list):
    def __init__(self, items):
        super().__init__(items)
        items = list(items)
        new_items = []
        for i in self:
            for j in range(len(items)):
                if items[j] == i:
                    items[j] = "1" * j
                    new_items.append(items[j])
        print(f"List: {new_items}")

yellow_list = YellowList((1, 2, 3))

# -- часть Вовы --

# Это заглушка класса dict
class YellowDict(dict):
   def __init__(self, dict):
        super().__init__(dict)
        dict["default"] = True
        print(f"Dict: {dict}")

# -- Часть Димы --

yellow_dict = YellowDict(dict={})

# Это заглушка класса set
class YellowSet(set):
    def __init__(self, list):
        super().__init__(list)
        for i in range(len(list)):
            if type(list[i]) == bool:
                print("Set: False")
            else:
                pass
        print(f"Set: True")

# Это вызов конструктора списка с помощью кортежа.
# То есть на вход при создании экземпляра передается кортеж.
# Вывод в консоли должен получится [1, 2, 3], ведь мы ничего не меняли в заглушке класса... пока что=)
# Это вызов конструктора множества с помощью списка.
# То есть на вход при создании экземпляра передается список.
yellow_set = YellowSet(['1', "q", "wow", '1'])