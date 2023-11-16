# -- часть Никиты --
class YellowList(list):
    def __init__(self, items):
        super().__init__(items)
        self.items = list(items)
        new_items = []
        for i in self:
            for j in range(len(self.items)):
                if self.items[j] == i:
                    self.items[j] = "1" * j
                    new_items.append(self.items[j])
        print(new_items)
    
    def __str__(self):
        items_new = []     # список для новых элементов
        for i in range(len(self.items)):
            items_new.append(self.items[i])   # добавляем текущий элемент
            items_new.append("--||--")   # добавляем разделитель
            print(items_new)
        items_new.remove(items_new[-1])   # удаляем последний разделитель
        return f"{items_new}"
    
          

yellow_list = YellowList([1,2,3])
print(yellow_list, sep = " ")

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
                return False
            else:
                pass
        return True

# Это вызов конструктора списка с помощью кортежа.
# То есть на вход при создании экземпляра передается кортеж.
# Вывод в консоли должен получится [1, 2, 3], ведь мы ничего не меняли в заглушке класса... пока что=)
# Это вызов конструктора множества с помощью списка.
# То есть на вход при создании экземпляра передается список.
yellow_set = YellowSet(['1', "q", "wow", '1'])