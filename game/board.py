import pyglet
from pyglet import shapes
from pyglet.window import mouse

from game import pawn, resources

class Board():
     ## View class of the board
     ## Able to change colors of the board

    """
        self.squares = 
        ------------------------
       |(56)|  |  |  |  |  |  |(63)|
       ------------------------
       | (48) |  |  |  |  |  |  |  |
       ------------------------
       | (40) |  |  |  |  |  |  |  |
       ------------------------
       | (32) |  |  |  |  |  |  |  |
       ------------------------
       | (24) |  |  |  |  |  |  |  |
       ------------------------
       | (16) |  |  |  |  |  |  |  |
       ------------------------
       | (8) |  |  |  |  |  |  | (15) |
       ------------------------
       |(0)|  |  |  |  |  |  |(7)|

    """

    def __init__(self, batch):
        # colors for the squares inside of the board
        white = (168, 112, 73)
        black = (206,157,109)
        self.move_square = (246,27,58)
        
        # Draw square
        square = 0
        start_y = 100
        start_x = 200
        start = [start_x, start_y]
        self.square_size = 50
        self.squares= [None]*64
        next_color = 'white'
        for row in range(8):
            for column in range(8):
                color = black if next_color=='black' else white
                next_color = 'white' if next_color == 'black' else 'black'
                self.squares[square]=shapes.Rectangle(start[0], start[1], self.square_size, self.square_size, color=color,  batch=batch)
                self.squares[square].opacity = 128
                square += 1
                # start[1]+=square_size
                start[0]+=self.square_size
            next_color = 'white' if next_color == 'black' else 'black'
            start[1] += self.square_size
            start[0] = start_x


    def moves(self, row, column, possible_moves):
        """
        range: list, squares that should be pinted in other color
        """
        start_square_x = (row*50)+200
        start_square_y = (column*50)+200
        index = row*8 +column
        previous = {}
        for next_column, next_row in possible_moves:
            new_index = index + next_column + (8*next_row)
            previous[new_index] = self.squares[new_index].color
            print('{}, {}'.format(next_row, next_column))
            self.squares[new_index].color = self.move_square
        return previous
    
    def default_colors(self, squares):
        for index_squares in squares:
            self.squares[index_squares].color = squares[index_squares]
        

        