# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, cur_room, prev_room = "No Where", inventory_cap = 0, inventory_list = []):
        self.name = name
        self.cur_room = cur_room
        self.prev_room = prev_room
        self.inventory_cap = inventory_cap
        self.inventory_list= inventory_list

    def __str__(self):
        return f"Name = {self.name}, Current Room = {self.cur_room},Previous Room = {self.prev_room}, Inventory Count = {self.inventory_cap}, Inventory Items = {self.inventory_list}"

    def validate_direction(self, cur_room, direction):
      if cur_room == "Outside Cave Entrance":
        if direction == "n":
          return "foyer"

      elif cur_room == "Foyer":
        if direction == "s":
          return "outside"
        elif direction == "n":
          return "overlook"
        elif direction == "e":
          return "narrow"

      elif cur_room =="Grand Overlook":
        if direction == "s":
          return "foyer"

      elif cur_room == "Narrow Passage":
        if direction == "n":
          return "treasure"
        elif direction == "w":
          return "foyer"

      elif cur_room =="Treasure Chamber":
        if direction == "s":
          return "narrow"


      return "You cannot go that direction at this time."
