import pyglet
from . import piece, resources

# Draw the pawn figures and it will be able to do in either side of the board
def paws(team, start_x, start_y, square_sizes, batch):
    image_select = resources.white_pawns if team == "white" else resources.black_pawns
    paws = [None]*8
    offset = 0
    for index in range(len(paws)):
        element = pyglet.sprite.Sprite(image_select,start_x+offset, start_y, batch=batch)
        offset += square_sizes
        paws[index] = element
    return paws