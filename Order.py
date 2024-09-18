#!/bin/python3
import MenuItem


class Order:
    def __init__(self, order_id: int, items: list = []):
        self.items = items
        self.order_id = order_id

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

    def to_dict(self):
        json_list = []
        for item in self.items:
            json_list.append(item.__dict__)
        return {"order_id": self.order_id, "items": json_list}
