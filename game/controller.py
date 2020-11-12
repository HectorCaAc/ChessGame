import pyglet
from pyglet.window import mouse

from game import pawn, resources


class Controller():

    def __init__(self, board, batch,  *args, **kwargs):
        self.board = board
        self.pieces_location = [[None for i in range(8)] for i in range(8)]

        # Handlers
        self.mouse_handler = mouse.MouseStateHandler()

        #batch 
        self.batch = batch
        
        #Squares that change of color when user clicks in a piece
        self.squares_selected = {}
        # self.draw_pawns()

    def draw_pawns(self):
        # draw the black ones first
        start_x = 195
        start_y = 395
        offset = 0
        for index in range(8):
            self.pieces_location[6][index] = pawn.Pawn(False, resources.black_pawns, start_x+offset,start_y, batch =self.batch)
            offset += 50
        start_x = 195
        start_y = 145
        offset =0 
        for index in range(8):
            self.pieces_location[1][index] = pawn.Pawn(True, resources.white_pawns, start_x+offset,start_y, batch =self.batch)
            offset += 50

    def piece_selected(self, row, column):
        piece = self.pieces_location[row][column]
        moves = set()
        if piece.name == 'pawn':
            # Check if there are enemies in the sides
                # check if there is oponents in the adjacent
            moves = moves.union(piece.move())
            if piece.move_up:
                check_enemies = [[-1,1], [1,1]]
            else:
                check_enemies = [[-1,-1], [1,-1]]
            for add_x, add_y in check_enemies:
                candidate_x = row + add_x
                candidate_y = column + add_y
                if candidate_x >= 0 and candidate_x <= 7 and candidate_y >= 0 and candidate_y <= 7:
                    if self.pieces_location[candidate_x][candidate_y] != piece.team:
                        moves.add((candidate_x, candidate_y))
        self.clean_board()
        # keep that if there are some squares
        squares_selected = self.board.moves(row, column, moves)
        self.squares_selected= squares_selected

    def clean_board(self):
        if len(self.squares_selected) != 0:
            self.board.default_colors(self.squares_selected)
            self.squares_selected = {}


    def on_mouse_press(self, x, y, button, modifiers):
        # check if board need to be clean


        self.clean_board()
        # Determine the square that was selected , how ??
        # make sure that the clikc is inside of the square
        
        if x < 200 or x >= 600 or y < 100 or y >= 500:
            return
        # get index of the square
        print('x {}, y {}'.format(x,y))
        x -= 200
        y -= 100
        row = int(y/50)
        column = int(x/50)
        if self.pieces_location[row][column] is not None:
            print('possible moves ')
            self.piece_selected(row, column )
        else:
            print('Empty square')
        square_select = 8*row + column