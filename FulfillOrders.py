#!/usr/bin/python3
from Order import Order
from MenuItem import MenuItem
from AbcClasses import MySerializer
from RestaurantOrderSystem import set_color, reset_color, print_menu, menu_items


def calculate_total(order: list) -> float:
    total = 0
    for item in order:
        total += item["price"]
    return total

def print_order(order: list):
    for item in order:
        print(f'{item["name"]}: {item["price"]:.2f}')
    print()

def remove_item(order, item: MenuItem):
    order.remove(item)

try:
    orders = MySerializer.deserialize("orders.json")
except FileNotFoundError:
    orders = []
print("Here's a list of pending order IDs:\n")
i = 0
for item in orders:
    print(f'[Order {i}]: {item["order_id"]} | order size: {len(item["items"])}')
    i += 1
print()

print("Enter the index of the order to fulfill.")
order_index = int(input("Order "))
print(f'Confirm order id {orders[order_index]["order_id"]}? [Y/N]')
confirmation = input()
if confirmation.lower() == "y":
    order = orders[order_index]["items"]
    total = f"${calculate_total(order):.2f}"
    print("Here is the order:")
    print_order(order)
    print("Type an item or its item id to add it to the order. Type \"menu\" to "
          "see the menu.")
    while len(order) != 0:
        set_color("bold")
        set_color("italic")
        set_color("light cyan")
        user_input = input().lower()
        reset_color()
        if user_input == "menu":
            print_menu(menu_items)
        elif len(order) != 0:
            item_found = False
            for item in order:
                if item["name"].lower() == user_input or str(item["itemId"]) == user_input:
                    remove_item(order, item)
                    item_found = True
                    print(f'{item["name"] if item["name"] != "Roll" else "Rick Roll"}: ${item["price"]:.2f}')
                    break
            if not item_found:
                set_color("Red")
                print("Item wasn't ordered.")
                reset_color()

    print(f"Order fulfilled! Total money earned from this order: {total}")
    orders.remove(orders[order_index])
    MySerializer.serialize(orders, "orders.json")

