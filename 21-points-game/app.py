import random
class start:
    
    def __init__(self):
        name = input("Привет как тебя зовут?\nПоиграем в 21?\n")
        self.ochki_player = 0
        self.ochki_diler = 0
        self.hod_player = 0
        self.hod_diler = 0
        self.choice = input(f"{name},вы будете брать карту да или нет?\n")
        self.koloda = [6,7,8,9,10,2,3,4,11,6,7,8,9,10,2,3,4,11,6,7,8,9,10,2,3,4,11,6,7,8,9,10,2,3,4,11] #у нас 4 масти


    """while ochki_diler <21 and ochki_player < 21:
        if choice == "Да" or choice == "да":
            ochki_player += int(random.choice(koloda))
            ochki_diler += int(random.choice(koloda))
            if ochki_player == 21:
                
                print(f"{name} у вас {ochki_player}, а у дилера {ochki_diler}\n вы победили")
                break
            elif ochki_diler == 21:
                print(f"{name} у вас {ochki_player}, а у дилера {ochki_diler}\n вы прогирали")
            hod_diler = ochki_diler - hod_diler
            hod_player = ochki_player - hod_player
            print(f"У вас {ochki_player} очков, у дилера {ochki_diler}\n")
            koloda.remove(hod_player)
            koloda.remove(hod_diler)
            choice_2 = input("Вы будете брать карту да или нет?\n")
            if choice_2 == "нет":
                print(f"{name} у вас {ochki_player}, а у дилера {ochki_diler}")   
                if ochki_diler>ochki_player:
                    print("Вы проиграли")
                elif ochki_player>ochki_diler:
                    print("Вы выйграли")
                else:
                    print("Ничья")
            if ochki_diler > 21:
                print("Вы выйграли, у дилера больше 21 очка")
            elif ochki_player>21:
                print("Вы проиграли, у вас больше 21 очка ")
    """    

    def hod(self):
        self.ochki_player = int(random.choice(self.koloda))
        self.ochki_diler = int(random.choice(self.koloda))
        if self.ochki_player == 21:
            print(f"{self.name} у вас {self.ochki_player}, а у дилера {self.ochki_diler}\n вы победили")
            
        elif self.ochki_diler == 21:
            print(f"{self.name} у вас {self.ochki_player}, а у дилера {self.ochki_diler}\n вы прогирали")
            

        self.hod_diler = self.ochki_diler - self.hod_diler
        self.hod_player = self.ochki_player - self.hod_player
        self.koloda.remove(self.hod_player)
        self.koloda.remove(self.hod_diler)
        choice_2 = input("Вы будете брать карту да или нет?\n")
        if self.ochki_diler > 21:
            print("Вы выйграли, у дилера больше 21 очка")
        elif self.ochki_player>21:
            print("Вы проиграли, у вас больше 21 очка ")


app = start()

while app.ochki_player<21 and app.ochki_diler<21:
    app.hod()
    if choice_2.lower() == "да":
        app.hod()
    else:
        print()
    choice_2 = input("Вы будете брать карту да или нет?\n")