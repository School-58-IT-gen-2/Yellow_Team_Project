class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += self.get_card_value(card)

    def get_card_value(self, card):
        if card.rank in ["Валет", "Дама", "Король"]:
            return 10
        elif card.rank == "Туз":
            return 11
        else:
            return int(card.rank)

    def adjust_for_ace(self):
        for card in self.cards:
            if card.rank == "Туз" and self.value > 21:
                self.value -= 10
