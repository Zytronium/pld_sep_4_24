#!/bin/python3
from random import randint
from AbcClasses import MySerializer
from Order import Order
from MenuItem import MenuItem
import json


def print_menu(menu: list):
    for item in menu:
        if isinstance(item, MenuItem):
            print(f"[{item.itemId:2}]: {item.name}: ", end='')
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

def set_color(color: str):
    color = color.lower()
    if color == "black":
        print("\033[30m", end='')
    elif color == "red":
        print("\033[31m", end='')
    elif color == "green":
        print("\033[32m", end='')
    elif color == "brown":
        print("\033[33m", end='')
    elif color == "blue":
        print("\033[34m", end='')
    elif color == "purple":
        print("\033[35m", end='')
    elif color == "cyan":
        print("\033[36m", end='')
    elif color == "light grey" or color == "light gray":
        print("\033[37m", end='')
    elif color == "dark grey" or color == "dark gray" or color == "grey" or color == "gray":
        print("\033[1;30m", end='')
    elif color == "light red":
        print("\033[1;31m", end='')
    elif color == "light green":
        print("\033[1;32m", end='')
    elif color == "yellow":
        print("\033[1;33m", end='')
    elif color == "light blue":
        print("\033[1;34m", end='')
    elif color == "light purple":
        print("\033[1;35m", end='')
    elif color == "light cyan":
        print("\033[1;36m", end='')
    elif color == "white":
        print("\033[1;37m", end='')
    elif color == "reset" or color == "default":
        print("\033[0m", end='')
    elif color == "bold":
        print("\033[1m", end='')
    elif color == "underline":
        print("\033[4m", end='')
    elif color == "blink" or color == "blinking":
        print("\033[5m", end='')
    elif color == "reverse":
        print("\033[7m", end='')
    elif color == "italic":
        print("\033[3m", end='')
    elif color == "concealed" or color == "conceal":
        print("\033[8m", end='')
    elif color == "revealed" or color == "reveal":
        print("\033[28m", end='')

def reset_color():
    print("\033[0m", end='')

def generate_order_id(orders):
    order_id = randint(0, 99999999)
    for item in orders:
        if item["order_id"] == order_id:
            return generate_order_id(orders)
    return order_id

chicken = MenuItem("Chicken Nuggets", 7.99, 0)
salmon = MenuItem("Salmon Nuggets", 4.49, 1)
sandwich = MenuItem("Sandwich", 5.99, 2)
rickroll = MenuItem("Roll", 0.99, 3)
halibut = MenuItem("Halibut", 14.99, 4)
tuna = MenuItem("Tuna", 13.99, 5)
pineapple = MenuItem("Pineapple", 14.99, 6)
banana = MenuItem("Banana", 0.99, 7)
apple = MenuItem("Apple", 4.99, 8)
chips = MenuItem("Potato Chips", 2.99, 9)
water = MenuItem("Water", 2.49, 10)
soda = MenuItem("Soda", 3.99, 11)
nugget = MenuItem("Nugget Nuggets", 16.99, 12)
pie = MenuItem("Pie", 3141.59, 13)

menu_items = [chicken, salmon, sandwich, rickroll, halibut, tuna, pineapple, banana, apple, chips, water, soda, nugget, pie]

if __name__ == "__main__":
    try:
        all_orders = MySerializer.deserialize("orders.json")
    except FileNotFoundError:
        all_orders = []
    order_id = generate_order_id(all_orders)
    order = Order(order_id)

    print("Welcome to the restaurant. Here is the menu:")
    print_menu(menu_items)

    while True:
        print("Please type an item name you'd like to order. If that is everything, "
              "type 'done'. To see the menu again, type 'menu'.")
        set_color("bold")
        set_color("italic")
        set_color("light cyan")
        user_input = input().lower()
        reset_color()
        if user_input == "menu":
            print_menu(menu_items)
        elif user_input != "done":
            item_found = False
            for item in menu_items:
                if item.name.lower() == user_input or str(item.itemId) == user_input:
                    order.add_item(item)
                    item_found = True
                    if item.name == "Roll":
                        print(f"Never Gonna Give You Up!")
                    print(f"{item.name if item.name != 'Roll' else 'Rick Roll'}: {item.price:.2f}")
                    break
            if not item_found:
                set_color("Red")
                print("Not a valid menu item.")
                reset_color()
        else:
            break
    if len(order.items) == 0:
        print("Really? You came to our restaurant and didn't order?")
    else:
        print("You ordered:")
        print_order(order)
        set_color("green")
        set_color("bold")
        print(f"Your total is: ",end='')
        set_color("light green")
        set_color("reverse")
        print(f"${order.calculate_total():.2f}")
        reset_color()
        all_orders.append(order.to_dict())
        MySerializer.serialize(all_orders, "orders.json")
        print(all_orders[0][str("items")][0]["itemId"])
