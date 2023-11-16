from extra import Deck, Hand, Card
import random, json

class BlackjackGame:
    def __init__(self):
        self.get_data()
        self.deck = Deck.Deck()
        self.deck.shuffle()
        self.player_hand = Hand.Hand()
        self.dealer_hand = Hand.Hand()

    def play(self):
        print(f'Добро пожаловать в Blackjack! \nВыигрыши: {self.data["Wins"]} \nПроигрыши: {self.data["Loses"]}')
        for _ in range(1):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

        self.show_partial_hands()

        while True:
            if self.player_hand.value == 21:
                print("Blackjack! Ты выиграл!")
                self.data["Wins"] += 1
                self.set_data()
                break
            elif self.player_hand.value > 21:
                print("Разорен! Потрачено!")
                self.data["Loses"]+=1
                self.set_data()
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
                    print("Дилер банкрот! Вы выиграли!")
                    self.data["Wins"] += 1
                    self.set_data()
                elif self.dealer_hand.value == self.player_hand.value:
                    print("Ничья!")
                elif self.dealer_hand.value > self.player_hand.value:
                    print("Дилер выиграл!")
                    self.data["Loses"] += 1
                    self.set_data()
                else:
                    print("Вы выиграли!")
                    self.data["Wins"] += 1
                    self.set_data()
                break

    def show_partial_hands(self):
        print("В руках игрока:", ", ".join(str(card) for card in self.player_hand.cards))
        print("В руках дилера:", self.dealer_hand.cards[0])

    def show_final_hands(self):
        print("В руках игрока:", ", ".join(str(card) for card in self.player_hand.cards))
        print("В руказ дилера:", ", ".join(str(card) for card in self.dealer_hand.cards))
        print("Твоя сумма значений карт:", self.player_hand.value)
        print("Сумма значений карт диллера:", self.dealer_hand.value)

    def get_data(self):
        with open("extra/data.json") as f:
            self.data = json.load(f)
            f.close()

    def set_data(self):
        with open("extra/data.json", "w") as f:
            json.dumps(self.data, f)
            f.close()
