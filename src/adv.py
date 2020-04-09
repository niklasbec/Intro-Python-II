from room import Room
from player import NewPlayer
from item import Item
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["dagger"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["php-manual"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["coin", "coin", "coin"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["rubberduck"]),
}

items = {
    "dagger": Item("Dagger", "It's sharp and pointy"),
    "coin": Item("Coin", "It's proabably worth keeping"),
    "php-manual": Item("PHP-Manual", "It's probably just trash, no one wants to code PHP"),
    "rubberduck": Item("Rubberduck", "Great for debugging")
}


# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

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

gameOver = False

playerInput = input("Enter Player Name: ")
if playerInput == "q":
    exit()

player = NewPlayer(playerInput, "outside")
print(player)
print("Enter q at any point to quit!")
time.sleep(1)
print("Enter drop to drop an item.")
time.sleep(1)
print("Enter get to get an item.")
time.sleep(1)
print("Enter info to get more info about an item.")
time.sleep(1)
print("Enter inventory to see your inventory.")
time.sleep(1)
print("Game starts now!")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

inven = player.inventoryInfo()
while gameOver == False:
    print(room[player.room])
    time.sleep(1)
    nextMove = input("Where do you want to go? Answer with N , E , S or W: ")
    if nextMove == "q":
        exit()
    if nextMove == "inventory":
        print(f"Your inventory: {inven}")
    elif "drop" in nextMove:
        if len(inven) > 0:
            itemToDrop = nextMove.split(" ")[1]
            if itemToDrop in inven:
                player.drop(itemToDrop)
                room[player.room].addItem(itemToDrop)
                print(f"You have dropped up {itemToDrop}")
            else:
                print("No such item in inventory")
        else:
            print("You dont have any items")
    elif "get" in nextMove:
        if len(room[player.room].items) > 0:
            itemToGet = nextMove.split(" ")[1]
            if itemToGet in room[player.room].items:
                player.get(itemToGet)
                room[player.room].removeItem(itemToGet)
                print(f"You have picked up {itemToGet}")
            else:
                print("There is no such item in the room!")
        else:
            print("There are no items here!")
    elif "info" in nextMove:
        itemInfo = nextMove.split(" ")[1]
        if itemInfo in items:
            print(items[itemInfo])
        else:
            print("There is no such item")
    elif nextMove == "N":
        if hasattr(room[player.room], 'n_to'):
            player.move(room[player.room].n_to.lower())
        else:
            print("Move not possible")
    elif nextMove == "E":
        if hasattr(room[player.room], 'e_to'):
            player.move(room[player.room].e_to.lower())
        else:
            print("Move not possible")
    elif nextMove == "S":
        if hasattr(room[player.room], 's_to'):
            player.move(room[player.room].s_to.lower())
        else:
            print("Move not possible")
    elif nextMove == "W":
        if hasattr(room[player.room], 'w_to'):
            player.move(room[player.room].w_to.lower())
        else:
            print("Move not possible")
    else:
        print("Direction not recognized")
    
