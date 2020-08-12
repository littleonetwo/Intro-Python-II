from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
player = Player("Guy",room['outside'] )
prev_dir = ""


def update_game(new_room, prev_direction, item = "nothing" ): #function to call whenever a valid action takes place
  player.prev_room = prev_direction
  player.cur_room = new_room

  if item != "nothing":
    player.inventory_cap += 1
    player.inventory_list.append(item)




while user_input != "q":
  print("Name: "+ player.name)
  print("Current Room: " + player.cur_room.name)
  print("\nRoom description: " + player.cur_room.description)
  print("\nYou came from the " + player.prev_room + " direction.")

  user_input = input("Choose a Direction: [n]orth, [s]outh, [e]ast, [w]est, or [q]uit: ")

  validate_move = player.validate_direction(player.cur_room.name, user_input)



  if validate_move != "You cannot go that direction at this time.":
    if user_input == "n" :
      prev_dir = "South"
    elif user_input == "s" :
      prev_dir = "North"
    elif user_input == "w" :
      prev_dir = "East"
    else:
      prev_dir = "West"

    update_game(room[validate_move], prev_dir )

  else:
    if user_input != "q":
      print("\n"+ validate_move)

  print("\n \n")
