# Write a class to hold player information, e.g. what room they are in
# currently.

class NewPlayer:
    def __init__(self, name, room, inventory=[]):
        self.name = name
        self.room = room
        self.inventory = inventory

    def move(self, roomMove):
        self.room = roomMove

    def get(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def inventoryInfo(self):
        return self.inventory

    def __str__(self):
        return (f'{self.name} is starting at {self.room}. Good luck! Inventory: {self.inventory}')
