#!/bin/python3
import MenuItem

class Order:
    def __init__(self, items: list, total: float):
        self.items = items
        self.total = total

    def add_item(item: MenuItem):
        self.items.append(item)

    def calculate_total() -> float:
        new_total = 0
        for item in self.items:
            new_total += item.price
        return new_total


        self.i1 = MenuItem("Salmon", 16.99),
        self.i2 = MenuItem("Halibut", 14.99),
        self.i3 = MenuItem("Tuna", 13.99),
        self.i4 = MenuItem("Pineapple", 12.99),
        self.i5 = MenuItem("Banana", 2.99),
        self.i6 = MenuItem("Apple", 3.99),
        self.i7 = MenuItem("Another Banana", 2.99),
        self.i8 = MenuItem("Sandwich", 9.99)

        self.item_list = [self.i1, self.i2, self.i3, self.i4, self.i5, self.i6, self.i7, self.i8]

        def print_menu(self):
            for item in self.item_list:
                print(f"{item.name}: \t${item.price:.2f}")