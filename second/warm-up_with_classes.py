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
