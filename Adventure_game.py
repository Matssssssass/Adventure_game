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

    #   def set_name(self, new_name):
    #       self.name = new_name

    #   def set_hp(self, new_hp):
    #       self.hp = new_hp

    #   def set_strength(self, new_strength):
    #       self.strength = new_strength

    def add_gold(self, gold):
        self.gold_inventory += gold

    def add_item(self):
        random_item = rand.randrange(100)
        if random_item <= 49:
            self.item_list.append("Sword")
            print("You found a SWORD!")
        elif random_item <= 98:
            self.item_list.append("Shield")
            print("You found a SHIELD!")
        elif random_item == 99:
            self.item_list.append("Sacrificial Child")
            print("You found the magical item called Sacrificial CHILD!")
        else:
            self.item_list.append("John Cena")
            print("You found the holy remains of JOHN CENA!")
    
    def show_items(self):
        for i in range(len(self.item_list)):
            self.item_inventory = (self.item_list[i])
        print(f"amount of gold:{self.gold_inventory}")
        print(f"Your special items are:{self.item_inventory}")

    def show_abilities(self):
        print(f"Your name is:{self.name}")
        print(f"Your hp is:{self.hp}")
        print(f"Your strength is:{self.strength}")

    def discovery(self):
        random_obstacle = rand.randrange(4)
        if random_obstacle == 0:
            self.trap()
        elif random_obstacle == 1:
            self.treasure()
        elif random_obstacle == 2:
            self.monster()
        else:
            print("You found nothing")

    def add_direction(self):
        self.movement_list = []
        random_direction = rand.randrange(0,4)
        if random_direction < 1:
            self.movement_list.append("Forward (w)")
            self.movement_list.append("left (a)")
        elif random_direction < 2:
            self.movement_list.append("left (a)")
            self.movement_list.append("right (d)")
        elif random_direction < 3:
            self.movement_list.append("right (d)")
            self.movement_list.append("forward (w)")
            
        else:
            self.movement_list.append("left (a)")
            self.movement_list.append("right (d)")
            self.movement_list.append("forward (w)")


        Direction = input(f"Where do you want to go?{self.movement_list}: ")
        Direction = Direction.lower()

        if Direction == "w":
            print("You went through the door in front of you silly bitch!")
            self.discovery()
        elif Direction == "a":
            print("You went through the left door, but why?")
            self.discovery()
        elif Direction == "d":
            print("You went through the right door, that's right")
            self.discovery()
        else: 
            print("you chose nothing and therefor god will hate you forever and kill you instantly!\n\nDie Bitch")
            self.hp = 0
            

    def flee(self):
        damage_taken = rand.randrange(2)
        self.hp -= damage_taken
        print(f"\nMonster hit you with {damage_taken}, Your new hp is {self.hp}")
        gold_lost = rand.randint(10,30)
        if gold_lost > self.gold_inventory:
            self.gold_inventory = 0
            print(f"While running away from the monster you had no gold left!")
        else:
            self.gold_inventory -= gold_lost
            print(f"While running away you lost {gold_lost} gold!")

    def monster(self):
        print("A MONSTER appeared out of the blue, how weird")
        monster_hp = rand.randrange(1,5) 
        player_attacking = True
        while player_attacking == True:
            attack = rand.randrange(self.strength)
            monster_hp -= attack
            print(f"\nYou hit the monster with {attack} damage!")
            if monster_hp < 1:
                gold_found = rand.randint(10,50)
                self.gold_inventory += gold_found
                print(f"The monster is dead! The corpse contained {gold_found} gold!")
                break
            print(f"The monsters hp is now {monster_hp}")
            damage_taken = rand.randrange(0,2)
            self.hp -= damage_taken
            print(f"\nThe monster then hit you with {damage_taken}! \nYour new hp is {self.hp}")
            player_wants_to_attack = input("\nDo you want to continue attacking? [y] or [n]\n:")
            player_wants_to_attack = player_wants_to_attack.lower()
            if player_wants_to_attack == "y":
                None
            elif player_wants_to_attack == "n":
                self.flee()
                break
            else:
                print("no acceptable input was called!\nthe fight will go on") 
                input("press enter to continue")
    
    def treasure(self):
        chance = rand.randrange(100)
        if chance <= 49:
            gold_found = rand.randint(10,50)
            self.gold_inventory += gold_found
            print(f"You found {gold_found} gold")
        elif chance <= 74:
            self.add_item()
        elif chance <= 79:
            self.diamond_inventory += 1
            print("You found a diamond")

    def trap(self):
        damage_taken = rand.randrange(0,2)
        self.hp -= damage_taken
        print(f"\nYou fell into a trap and took {damage_taken} damage. Your new hp is {self.hp} ")

        

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
player_hp = int(input("What is your hitpoints:"))
player_strength = int(input("What is your strength:"))

ready_player_one = Character(player_name, player_hp, player_strength, 0, 0, 0, 0)

i = 0
while i < 10:
    clear_screen()
    print(f"the time is {Time[i]} o'clock")
    main_menu()
    round_choice = input(":")
    round_choice = round_choice.lower()
    if round_choice == "w":
        ready_player_one.add_direction()
        i += 1
        input("If you are done press enter: ")
        
    elif round_choice == "s":
        random_obstacle = rand.randrange(4)
        if random_obstacle == 0:
            ready_player_one.trap()
        elif random_obstacle == 1:
            ready_player_one.treasure()
        elif random_obstacle == 2:
            ready_player_one.monster()
        else:
            print("You found nothing")
        input("If you are done press enter:")
        i += 1

    elif round_choice == "a":
        ready_player_one.show_abilities()
        input("\nIf you are done press enter!")
        
    elif round_choice == "i":
        ready_player_one.show_items()
        input("if you are done press enter!")
        
    else:
        print("None of the options were called:(")

    if ready_player_one.hp < 1:
        clear_screen()
        print("GAME OVER")
        print("\n\n\n\nsucker")
        break

if i >= 10:
    clear_screen()
    print("YOU WON sucker")
    print(f"Your score was: {ready_player_one.gold_inventory}")


print("hehehehe siuu")