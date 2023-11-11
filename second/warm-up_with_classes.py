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
        print(new_items)

yellow_list = YellowList((1, 2, 3))

# -- часть Вовы --

# Это заглушка класса dict
class YellowDict(dict):
   def __init__(self, dict):
        super().__init__(dict)
        dict["default"] = True
        return dict

# -- Часть Димы --

# Это заглушка класса set
def YellowSet(set):
    def __init__(self, list):
        for i in range(list):
            if type(list[i]) == bool:
                return false
            else:
                pass
        return True

# Это вызов конструктора списка с помощью кортежа.
# То есть на вход при создании экземпляра передается кортеж.
# Вывод в консоли должен получится [1, 2, 3], ведь мы ничего не меняли в заглушке класса... пока что=)
# Это вызов конструктора множества с помощью списка.
# То есть на вход при создании экземпляра передается список.
yellow_set = YellowSet(['1', "q", "wow", '1'])