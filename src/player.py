# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:

    def __init__(self, name, cur_room, prev_room = "No Where", inventory_cap = 0, inventory_list = []):
        self.name = name
        self.cur_room: Room = cur_room
        self.prev_room = prev_room
        self.inventory_cap = inventory_cap
        self.inventory_list= inventory_list


    def check_item(self, item_name: str):
      for items in self.inventory_list:
        if items.name.lower() == item_name.lower():
          return items

        return None

    def remove_item(self, item_name):
      self.inventory_list.remove(item_name)


    def __str__(self):
        return f"Name = {self.name}, Current Room = {self.cur_room},Previous Room = {self.prev_room}, Inventory Count = {self.inventory_cap}, Inventory Items = {self.inventory_list}"
