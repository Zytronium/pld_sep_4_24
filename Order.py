#!/bin/python3
import MenuItem

class Order:
    def __init__(self, items: list = []):
        self.items = items

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def remove_item(self, item: MenuItem):
        self.items.remove(item)

    def add_items(self, items: list):
        for item in items:
            self.items.append(item)

    def remove_items(self, items: list):
        for item in items:
            self.items.remove(item)

    def calculate_total(self) -> float:
        total = 0
        for item in self.items:
            total += item.price
        return total

    def get_json(self):
        json_dict = {}
        for item in self.items:
            json_dict[item.name] = item.__dict__
        return json_dict
