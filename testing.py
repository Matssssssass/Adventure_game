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

def treasure(self):
        chance = rand.randrange(100)
        if chance <= 49:
            gold_found = rand.randint(10,50)
            self.gold_inventory += gold_found
            print(f"You found {gold_found} gold")
        elif chance >= 50 or chance <= 75:
            self.add_items()
        elif chance >= 76 or chance <= 81:
            self.siamond_inventory += 1
            print("You found a diamond")