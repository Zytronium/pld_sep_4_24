#!/bin/python3
from Order import Order
from MenuItem import MenuItem

def print_menu(menu: list):
    for item in menu:
        if isinstance(item, MenuItem):
            print(f"{item.name}: ",end='')
            space = 32 - len(item.name)
            for i in range(space):
                if (i + len(item.name)) % 2 == 0:
                    print(".", end='')
                else:
                    print(" ",end='')
            print(f"${item.price:.2f}")
    print()

def print_order(order: Order):
    for item in order.items:
        if isinstance(item, MenuItem):
            print(f"{item.name}: {item.price:.2f}")
    print()

chicken = MenuItem("Chicken Nuggets", 6.99)
salmon = MenuItem("Salmon Nuggets", 6.49)
sandwich = MenuItem("Sandwich", 5.99)
halibut = MenuItem("Halibut", 14.99)
tuna = MenuItem("Tuna", 13.99)
pineapple = MenuItem("Pineapple", 12.99)
banana = MenuItem("Banana", 0.99)
apple = MenuItem("Apple", 2.99)
chips = MenuItem("Potato Chips", 2.99)
water = MenuItem("Water", 1.49)
soda = MenuItem("Soda", 3.99)
nugget = MenuItem("Nugget Nuggets", 16.99)

menu_items = [chicken, salmon, sandwich, halibut, tuna, pineapple, banana, apple, chips, water, soda, nugget]
order = Order()

print("Welcome to the restaurant. Here is the menu:")
print_menu(menu_items)

while True:
    print("Please type an item name you'd like to order. If that is everything,"
          "type 'done'. To see the menu again, type 'menu'.")
    user_input = input().lower()
    if user_input == "menu":
        print_menu(menu_items)
    elif user_input != "done":
        item_found = False
        for item in menu_items:
            if item.name.lower() == user_input:
                order.add_item(item)
                item_found = True
                print(f"{item.name}: {item.price:.2f}")
                break
        if not item_found:
            print("Not a valid menu item.")
    else:
        break
if len(order.items) == 0:
    print("Really? You came to our restaurant and didn't order?")
else:
    print("You ordered:")
    print_order(order)
    print(f"Your total is ${order.calculate_total()}")
