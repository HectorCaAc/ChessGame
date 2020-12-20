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

    def line_movement(self, current_row, current_column, moves):
        positions_to_check ={}
        for dirrection, add_x, add_y, in moves:
            candidate_x = current_row + add_x
            candidate_y = current_column + add_y
            positions_to_check[dirrection]=[]
            while candidate_x > -1 and candidate_x < 8 and candidate_y > -1 and candidate_y < 8:
                positions_to_check[dirrection].append((candidate_x, candidate_y))
                candidate_x += add_x
                candidate_y += add_y
        return positions_to_check
