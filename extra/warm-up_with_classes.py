# -- часть Никиты --
class YellowList(list):
    def __init__(self, items):
        super().__init__(items)
        self.items = list(items)
        new_items = []
        for i in self:
<<<<<<< HEAD:second/warm-up_with_classes.py
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
    
          
=======
            for j in range(len(items)):
                if items[j] == i:
                    items[j] = "1" * j
                    new_items.append(items[j])
        print(f"List: {new_items}")
>>>>>>> e8cc6c5b03ca156166202c3d8e80624b6dce0042:extra/warm-up_with_classes.py

yellow_list = YellowList([1,2,3])
print(yellow_list, sep = " ")

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
<<<<<<< HEAD:second/warm-up_with_classes.py
                return False
=======
                print("Set: False")
>>>>>>> e8cc6c5b03ca156166202c3d8e80624b6dce0042:extra/warm-up_with_classes.py
            else:
                pass
        print(f"Set: True")

# Это вызов конструктора списка с помощью кортежа.
# То есть на вход при создании экземпляра передается кортеж.
# Вывод в консоли должен получится [1, 2, 3], ведь мы ничего не меняли в заглушке класса... пока что=)
# Это вызов конструктора множества с помощью списка.
# То есть на вход при создании экземпляра передается список.
yellow_set = YellowSet(['1', "q", "wow", '1'])