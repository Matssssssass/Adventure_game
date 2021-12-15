from os import system
import random as rand


def add_direction(self):
    self.movement_list = []
    random_direction = rand.randrange(0,4)
    if random_direction == 1:
        self.movement_list.append("forward (w)", "left (a)")
    if random_direction == 2:
        self.movement_list.append("left (a)", "right (d)")
    if random_direction == 3:
        self.movement_list.append("right (d)", "forward (w)")
    else:
        self.movement_lost.append("forward (w)", "right (d)", "left (a)")

direction = input("Where do you want to go?{self.movement_list}")

    


def trap(self):
    damage_taken = rand.randrange(0,2)
    self.hp -= damage_taken
    print(f"\nYou fell into a trap and took {damage_taken}. Your new hp is {self.hp} ")

