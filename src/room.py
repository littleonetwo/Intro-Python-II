# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:

    def __init__(self, name, description, key):
      self.name = name
      self.description = description
      self.key = key
      self.items: List[Item] = []


    def get_item(self, item_name: str):
      for items in self.items:
        if items.name.lower() == item_name.lower():
          return items

        return None


    def remove_item(self, item_name):
      self.items.remove(item_name)


    def __str__(self):
      return f"Name of Room: {self.name}, Description of Room: {self.description}, Key: {self.key}"
