# Write a class to hold player information, e.g. what room they are in
# currently.

class NewPlayer:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def move(self, roomMove):
        self.room = roomMove
    
    def __str__(self):
        return (f'{self.name} is starting at {self.room}. Good luck!')
