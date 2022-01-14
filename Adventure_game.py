from os import system
import random as rand
import sys
from time import sleep

from testing import fin_utprint

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

    # Ändrar hastigheten som texten skrivs.

    def fin_utprint(string):
        edited_string = string
        edited_string = str(edited_string)
        for char in edited_string:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(.09)
        sleep(1)   

    # Lägger till guld i inventory.

    def add_gold(self, gold):
        self.gold_inventory += gold

    # Funktionen slumpar fram ett item som hjälper dig i spelet.

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

    # Funktionen visar items som finns i spelarens inventory
    
    def show_items(self):
        for i in range(len(self.item_list)):
            self.item_inventory = (self.item_list[i])
        print(f"amount of gold:{self.gold_inventory}")
        print(f"amount of diamonds:{self.diamond_inventory}")
        print(f"Your special items are:{self.item_inventory}")

    #Funktion för att visa spelarens egenskaper

    def show_abilities(self):
        print(f"Your name is:{self.name}")
        
        # Funktionen undersöker om Shield finns i item_list och ändrar därefter spelarens egenskaper

        if "Shield" in self.item_list:
            print(f"Your hp is:{self.hp} + (2)")
        else:
            print(f"your hp is {self.hp}")

        # Funktionen undersöker om Sword finns i item_list och ändrar därefter spelarens egenskaper
        
        if "Sword" in self.item_list:
            print(f"Your strength is:{self.strength} + (2)")
        else:
            print(f"your strength is {self.strength}")

    # Funktionen slumpar fram om spelaren ska hitta en fälla, skatt, monster eller ingenting

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

        for number in self.movement_list:
            number = self.movement_list.index(number)
            name = self.movement_list[number]
            name = str(name)
            print(f"{name}")
            
        # Input bestämmer vilken dörr spelaren går igenom.

        while True:
            Direction = input(":")
            if Direction == "w":
                print("You went through the door in front of you silly bitch!")
                self.discovery()
                break
            elif Direction == "a":
                print("You went through the left door, but why?")
                self.discovery()
                break
            elif Direction == "d":
                print("You went through the right door, that's right")
                self.discovery()
                break
            else: 
                print("Wrong input")            

    # Funktion för att fly från monster

    def flee(self):
        damage_taken = rand.randrange(2)
        self.hp -= damage_taken
        print(f"\nMonster hit you with {damage_taken}, Your new hp is {self.hp}")

        # Slumpar fram skada som spelaren tar när han flyr.

        gold_lost = rand.randint(10,30)
        if gold_lost > self.gold_inventory:
            self.gold_inventory = 0
            print(f"While running away from the monster you had no gold left!")
        else:
            self.gold_inventory -= gold_lost
            print(f"While running away you lost {gold_lost} gold!")

    def monster(self):
        
        print("A MONSTER appeared out of the blue, how weird")
        
        #skapar variabel för anfalls loopen att köra
        player_attacking = True
        
        #input loop för spelarens val antingen att slåss eller fly
        while True:
            fight_decision = input("What do you want to do? flee[f] attack[a] \n:")
            fight_decision = fight_decision.lower()
            if fight_decision == "a":
                break
            elif fight_decision == "f":
                self.flee()
                player_attacking = False
                break
            else:
                print("Wrong input")
                
        #Skapar monstrets liv    
        monster_hp = rand.randrange(1,5) 
        
        #Anfalls loopen som kör medans både monster och spelare lever
        while player_attacking == True:
            
            #spelare anfaller med slumpvis styrka mellan 0 - self.strength

            #Om spelaren har ett svärd så ska styrkan på den adderas 
            if "sword" in self.item_list:
                random_attack = rand.randrange(self.strength)
                attack = random_attack + 2
                monster_hp -= attack
                print(f"\nYou hit the monster with {random_attack} + (2) damage!")
            
            #annars så slåss den utan denna extra skada
            else:    
                attack = rand.randrange(self.strength)
                monster_hp -= attack
                print(f"\nYou hit the monster with {attack} damage!")

            # om monstret är död så hoppar vi över resten av funktionen
            if monster_hp < 1:
                gold_found = rand.randint(10,50)
                self.gold_inventory += gold_found
                print(f"The monster is dead! The corpse contained {gold_found} gold!")
                break
            #visar monstrets nya liv
            print(f"The monsters hp is now {monster_hp}")
            
            #Monstrets slumpvisa anfall mellan 0-2 ifall spelare har en sköld
            if "shield" in self.item_list:
                damage_taken = rand.randrange(0,2)
                self.hp -= damage_taken
                if self.hp < 1:
                    break
                else:
                    print(f"\nThe monster then hit you with {damage_taken}! \nYour new hp is {self.hp}")

            #Annars så slumpas anfallet mellan 0-4
            else:
                damage_taken = rand.randrange(0,4)
                self.hp -= damage_taken
                if self.hp < 1:
                    break
                else:
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


    def Boss_fight(self):
        
        Boss_appearence = "THE BOSS appeared..."
        fin_utprint(Boss_appearence)

        #skapar variabel för anfalls loopen att köra
        player_attacking = True
        
        #Skapar BOSSENs liv    
        BOSS_hp = rand.randrange(5,15) 
        
        #Anfalls loopen som kör medans både BOSSEN och spelare lever
        while player_attacking == True:
            
        #spelare anfaller med slumpvis styrka mellan 0 - self.strength

            #Om spelaren har ett svärd så ska styrkan på den adderas 
            if "sword" in self.item_list:
                random_attack = rand.randrange(self.strength)
                attack = random_attack + 2
                BOSS_hp -= attack
                print(f"\nYou hit the BOSS with {random_attack} + (2) damage!")
            
            #annars så slåss den utan denna extra skada
            else:    
                random_attack = rand.randrange(self.strength)
                BOSS_hp -= random_attack
                print(f"\nYou hit the BOSS with {random_attack} damage!")

            # om Bossen är död så hoppar vi över resten av funktionen
            if BOSS_hp < 1:
                gold_found = rand.randint(50,150)
                self.gold_inventory += gold_found
                Boss_win_string = (f'''
{self.name} slayed THE BOSS! By his dying breath makes one last wish...

"Let my tale be told to generations after me"

With his last words he then lays completaly still with wide open eyes
and gold pouring out of his pockets. 
{self.name} counted to see how much and he found a total of {gold_found} gold coins!''')
                fin_utprint(Boss_win_string)
                break

            #visar BOSSENS nya liv
            print(f"The monsters hp is now {BOSS_hp}")
            
            #BOSSENS slumpvisa anfall mellan 2-4 ifall spelare har en sköld
            if "shield" in self.item_list:
                damage_taken = rand.randrange(2,4)
                self.hp -= damage_taken
                if self.hp < 1:
                    Death_string = f'''
With the sharpness of his sword The BOSS slays {self.name} and smiles at this warrior as he drops
on his knees and drops his bag of gold on the ground with the total of {self.gold_inventory} coins 
of gold pouring around him!

{self.name} says during his dying breath

"WAKANDA FOREVAAAAAH!"
                    '''
                    fin_utprint(Death_string)
                    break
                else:
                    print(f"\nTHE BOSS then hit you with {damage_taken}! \nYour new hp is {self.hp}")

            #Annars så slumpas anfallet mellan 2-6
            else:
                damage_taken = rand.randrange(2,6)
                self.hp -= damage_taken
                if self.hp < 1:
                    Death_string = f'''
With the sharpness of his sword The BOSS slays {self.name} and smiles at this warrior as he drops
on his knees and drops his bag of gold on the ground with the total of {self.gold_inventory} coins 
of gold pouring around him!

{self.name} says during his dying breath

"WAKANDA FOREVAAAAAH!"
                    '''
                    fin_utprint(Death_string)
                    break
                else:
                    print(f"\nTHE BOSS then hit you with {damage_taken}! \nYour new hp is {self.hp}")
            
            player_wants_to_attack = input("\nDo you want to continue attacking? [y] or [n]\n:")
            player_wants_to_attack = player_wants_to_attack.lower()
            if player_wants_to_attack == "y":
                None
            elif player_wants_to_attack == "n":
                Boss_surrender_string = f'''
The nobel warrior after hours of struggling tripped at the finnish line. {self.name} kneels
Before the great BOSS feet as he accepts his terrible defeat. THE BOSS gives the nobel warrior
mercy and let's him go with one condition

THE BOSS takes half of all the gold {self.name} had earned during his quest'''
                fin_utprint(Boss_surrender_string)
                self.gold_inventory /= 2
                break
            else:
                print("no acceptable input was called!\nthe fight will go on") 
                input("press enter to continue")

        # Slumpar fram om spelaren ska hitta guld, diamanter eller special item.

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

        # Skada tagen från fälla

    def trap(self):
        damage_taken = rand.randrange(0,2)
        self.hp -= damage_taken
        print(f"\nYou fell into a trap and took {damage_taken} damage. Your new hp is {self.hp} ")

        
    # Rensar skärmen.

def clear_screen():
    system("cls || clear")

    # Meny

def main_menu():
    print("what do you want to do?")
    print("walk?[w]")
    print("search?[s]")
    print("look at your abilities?[a]")
    print("look in your inventory?[i]")

#Spelets start och huvudprogrammets början

clear_screen()
print("welcome to the adventure!")

# Spelarens namn, hp och strength bestämms med input

player_name = input("What is your name:")
player_hp = int(input("What is your hitpoints:"))
player_strength = int(input("What is your strength:"))

#Klassen för spelaren skapas

ready_player_one = Character(player_name, player_hp, player_strength, 0, 0, 0, 0)

# Spelets klocka (i) skapas

i = 0
Time = [20, 21, 22, 23, 00, 1, 2, 3, 4, 5,]

while i < 10:
    clear_screen()

    #Rundan startar 

    print(f"the time is {Time[i]} o'clock")

    #Sista rundan är en bossfight!

    if i == 9:
        ready_player_one.Boss_fight()
        if ready_player_one.hp < 1:
            break
        else:
            i += 1
            break 

    #Spelaren blir frågad vad den vill göra

    main_menu()
    round_choice = input(":")
    round_choice = round_choice.lower()
    
    #En if sats för vad spelaren ger för input
    #Ifall spelaren ger felaktig input eller välja att kolla på sina abilities så skall variabeln i ej ökas
    
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

    #Om spelarens hp är 0 så ska spelaren vara död och därmed förlorar

    if ready_player_one.hp < 1:
        clear_screen()
        print("GAME OVER")
        break

#Om spelaren överlever alla rundor så ska vinnande avslutet printas

if i >= 10:
    clear_screen()

    Winning_text = (f'''
    You won!!
    Your score was {ready_player_one.gold_inventory}
    ''')
    fin_utprint(Winning_text)

    input("\nPress enter to continue")

    end_credits = '''
    Designed / Developed by: Åstrand productions

    Coworked with: Bergling Motors

    published by: Jarpner Airlines 
    
    '''
    fin_utprint(end_credits)