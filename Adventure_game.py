from os import system
import random as rand

class Character():
    def __init__(self, name, hp, strength, gold_inventory, item_inventory, item_list, diamond_inventory):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.gold_inventory = gold_inventory
        self.item_list = item_list
        self.item_list = []
        self.item_inventory = item_inventory
        self.diamond_inventory = diamond_inventory

    def set_name(self, new_name):
        self.name = new_name

    def set_hp(self, new_hp):
        self.hp = new_hp

    def set_strength(self, new_strength):
        self.strength = new_strength

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
        
    def monster(self):
        monster_hp = rand.randrange(1,5) 
        player_attacking = True
        while player_attacking == True:
            attack = rand.randrange(self.strength)
            monster_hp -= attack
            print(f"\nYou hit the monster with {attack} damage!")
            damage_taken = rand.randrange(0,2)
            self.hp -= damage_taken
            print(f"\nThe monster then hit you with {damage_taken}! \nYour new hp is {self.hp}")
            player_wants_to_attack = input("\nDo you want to continue attacking? [y] or [n]\n:")
            player_wants_to_attack = player_wants_to_attack.lower()
            if player_wants_to_attack == "y":
                None
            elif player_wants_to_attack == "n":
                player_attacking = False
            else:
                print("no acceptable input was called!\nthe fight will go on") 

    def flee(self):
        damage_taken = rand.randrange(2)
        self.hp -= damage_taken
        gold_lost = rand.randrange(10)
        self.gold_inventory -= gold_lost
    
    def treasure(self):
        chance = rand.randrange(100)
        if chance <= 49:
            gold_found = rand.randint(10,50)
            self.gold_inventory += gold_found
            print(f"You found {gold_found} gold")
        elif chance <= 74:
            self.add_items()
        elif chance <= 79:
            self.siamond_inventory += 1
            print("You found a diamond")

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
