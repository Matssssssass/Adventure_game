from os import system
import random as rand

class Character():
    def __init__(self, name, hp, strength, gold_inventory, item_inventory, item_list):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.gold_inventory = gold_inventory
        self.item_list = item_list
        self.item_list = []
        self.item_inventory = item_inventory

    def set_name(self, new_name):
        self.name = new_name

    def set_hp(self, new_hp):
        self.hp = new_hp

    def set_strength(self, new_strength):
        self.strength = new_strength

    def get_abilities(self):
        print(f"your name is:{self.name}\nYour hp is:{self.hp}\nYour stregnth is:{self.strength}")

    def add_gold(self, gold):
        self.gold_inventory += gold

    def add_item(self):
        random_item = rand.randrange(100)
        if random_item <= 49:
            self.item_list.append("Sword")
        elif random_item <= 98:
            self.item_list.append("Shield")
        else:
            self.item_list.append("John Cena")
    
    def show_items(self):
        for i in range(len(self.item_list)):
            self.item_inventory = (self.item_list[i])
        print(f"amount of gold:{self.gold_inventory}")
        print(f"Your special items are:{self.item_inventory}")

    def show_abilities(self):
        print(f"Your name is:{self.name}")
        print(f"Your hp is:{self.hp}")
        print(f"Your strength is:{self.strength}")
        
    def flee(self):
    damage_taken = rand.randrange(2)
    self.hp -= damage_taken
    gold_lost = rand.randrange(10)
    self.gold_inventory -= gold_lost

Time = [20, 21, 22, 23, 00, 1, 2, 3, 4, 5,]

def clear_screen():
    system("cls || clear")

def main_menu():
    print("what do you want to do?")
    print("walk?[w]")
    print("search?[s]")
    print("look at your abilities?[a]")
    print("look in your inventory?[i]")

clear_screen()

print("welcome to the adventure!")

player_name = input("What is your name:")
player_hp = input("What is your hitpoints:")
player_strength = input("What is your strength:")

ready_player_one = Character(player_name, player_hp, player_strength, 0, 0, 0)

for i in range(len(Time)):
    clear_screen()
    print(f"the time is {Time[i]} o'clock")
    main_menu()
    round_choice = input(":")
    round_choice = round_choice.lower()
    if round_choice == "w":
        print("yeah")
    elif round_choice == "s":
        print("KFC")
    elif round_choice == "a":
        print("fuck")
    elif round_choice == "i":
        print("baby")
    else:
        print("None of the options were called:(")
