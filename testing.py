import random as rand
def show_items():
    item_list = ["apple", "banana", "pear"]
    gold_inventory = 10
    item_inventory = None
    for i in range(len(item_list)):
        item_inventory = (item_list[i])
    print(f"amount of gold: {gold_inventory}")
    print(f"Your special items are: {item_inventory}")

show_items()