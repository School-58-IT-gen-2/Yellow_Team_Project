import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    ranks = ["Туз", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король"]
    suits = ["Черви", "Бубны", "Пики", "Крести"]

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

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

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def play(self):
        print("Добро пожаловать в Blackjack!")
        for _ in range(1):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

        self.show_partial_hands()

        while True:
            if self.player_hand.value == 21:
                print("Blackjack! Ты выиграл!")
                break
            elif self.player_hand.value > 21:
                print("Разорен! Потрачено!")
                break

            action = input("Хотите ходить или воздержаться? ")
            if action.lower() == "ходить":
                self.player_hand.add_card(self.deck.deal_card())
                self.show_partial_hands()
            elif action.lower() == "пропуск":
                while self.dealer_hand.value < 17:
                    self.dealer_hand.add_card(self.deck.deal_card())
                self.show_final_hands()
                if self.dealer_hand.value > 21:
                    print("Дилер! Вы выиграли!")
                elif self.dealer_hand.value == self.player_hand.value:
                    print("Ничья!")
                elif self.dealer_hand.value > self.player_hand.value:
                    print("Дилер выиграл!")
                else:
                    print("Вы выиграли!")
                break

    def show_partial_hands(self):
        print("В руках игрока:", ", ".join(str(card) for card in self.player_hand.cards))
        print("В руках дилера:", self.dealer_hand.cards[0])

    def show_final_hands(self):
        print("В руках игрока:", ", ".join(str(card) for card in self.player_hand.cards))
        print("В руказ дилера:", ", ".join(str(card) for card in self.dealer_hand.cards))
        print("Твоя сумма значений карт:", self.player_hand.value)
        print("Сумма значений карт диллера:", self.dealer_hand.value)

game = BlackjackGame()
game.play()