from room import Room
from player import Player
from item import Item
import os
from time import sleep


items = {
  'coin': Item("coin", "A small shimmering golden [coin]"),
  'sword': Item("sword", "A worn [sword] used extensively in what was perhaps an exhausting battle")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'outside'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",'treasure'),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


room['treasure'].items.append(items['coin'])
room['outside'].items.append(items['sword'])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

user_input = 0

user_input = input("A deep voice comes over your senses, \nHELLO GOOD HUMAN!\nWhat is YOUR Name?: ")

player = Player(user_input, room['outside'] )
prev_dir = ""

os.system('clear')

sleep(1)

print(f"Welcome {player.name}! I will now send you to a land full of treasures, it is your duty to find them and to also return!")

sleep(7)

os.system('clear')
print("YOUR BODY IS DISINIGRATED LIKE ASH IN THE WIND, AFTER A FEW SECONDS YOUR BODY MATERIALIZES IN FRONT OF AN OMINOUS CAVE.")

sleep(7)

os.system('clear')

def update_game( prev_direction, item = "nothing" ): #function to call whenever a valid action takes place
  player.prev_room = prev_direction


  if item != "nothing":
    player.inventory_cap += 1
    player.inventory_list.append(item)



def validate_direction(cur_room, direction):
  if " " in direction:
    word1 = direction[0:direction.find(" ")]
    word2 = direction[(direction.find(" ")+1):]

    if word1 == "get" or word1 == "take":
      item = cur_room.get_item(word2)
      if item:
        item.on_take()
        cur_room.remove_item(item)
        player.inventory_list.append(item)
      else:
        print(f"{word2} does not exist in this room")
    elif word1 =="drop":
      item = player.check_item(word2)
      if item:
        cur_room.items.append(item)
        player.remove_item(item)
        print(f"You dropped your {item.name}")
      else:
        print(f"{word2} does not exist in your bag.")



  if direction == "n":
    if hasattr(cur_room, "n_to"):
      player.cur_room = room[cur_room.n_to.key]
      return

  elif direction == "s":
    if hasattr(cur_room, "s_to"):
      player.cur_room = room[cur_room.s_to.key]
      return

  elif direction == "e":
    if hasattr(cur_room, "e_to"):
      player.cur_room = room[cur_room.e_to.key]
      return

  elif direction == "w":
    if hasattr(cur_room, "w_to"):
      player.cur_room = room[cur_room.w_to.key]
      return
  #this will only run if there was an incorrect direction
  return "You cannot do that at this time."




print("Name: "+ player.name)
i = 0
while user_input != "q":

  print("Current Room: " + player.cur_room.name)
  if len(player.cur_room.items) == 0:
    print("\nRoom description: " + player.cur_room.description)
  else:
    print("\nRoom description: " + player.cur_room.description +" You see:")
    while i < len(player.cur_room.items):
      print(player.cur_room.items[i].description)
      i+=1
    i=0
  print("\nYou came from the " + player.prev_room + " direction.")

  user_input = input("Choose an Action: [n]orth, [s]outh, [e]ast, [w]est, [get][item], [drop][item], or [q]uit: ")

  validate_move = validate_direction(player.cur_room, user_input)



  if validate_move != "You cannot go that direction at this time.":
    if user_input == "n" :
      prev_dir = "South"
    elif user_input == "s" :
      prev_dir = "North"
    elif user_input == "w" :
      prev_dir = "East"
    else:
      prev_dir = "West"

    update_game(prev_dir )

  else:
    if user_input != "q":
      print("\n"+ validate_move)

  print("\n \n")
