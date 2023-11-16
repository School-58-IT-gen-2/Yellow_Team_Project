from extra import Card, Hand
import random

class Deck:
    ranks = ["Туз", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король"]
    suits = ["Черви", "Бубны", "Пики", "Крести"]

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card.Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
