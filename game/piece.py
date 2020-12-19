import pyglet
from pyglet.window import mouse

class Piece(pyglet.sprite.Sprite):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dead = False
        self.team = None
        self.first_move = True
    
    def move(self, current_row, current_column):
        pass

    def attack(self, current_row, current_column):
        pass