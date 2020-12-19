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
        self.square_selected = {
                'square_selected': None,
                'possible_squares': {}
            }
        # self.draw_pawns()

    def draw_pawns(self):
        # draw the black ones first
        start_x = 195
        start_y = 395
        offset = 0
        for index in range(8):
            self.pieces_location[6][index] = pawn.Pawn(False, 'black', resources.black_pawns, start_x+offset,start_y, batch =self.batch)
            offset += 50
        start_x = 195
        start_y = 145
        offset =0 
        # draw whites figure
        for index in range(8):
            self.pieces_location[1][index] = pawn.Pawn(True, 'white',resources.white_pawns, start_x+offset,start_y, batch =self.batch)
            offset += 50

    def convert_row_column_to_square(self, row, column):
        return row*8 + column

    def convert_square_to_row_column(self, square):
        column = square % 8
        row = int(square / 8)
        return {
                'column': column,
                'row': row    
            }

    """
        PAWN
        rook- bishop- queen - king ( similar move differnt movement)
        knight
    """
    def moveWithOutJump(self, row, column, moves, attack_piece):
        """
            Take an array for moves and be sure sorte it and check if there is an enemy there
            if there is there stop
        """
        capable_move = set()
        piece = self.pieces_location[row][column]
        for off_set_row, off_set_column in moves:
            candidate_x = off_set_row+row
            candidate_y = off_set_column + column
            space = self.pieces_location[candidate_x][candidate_y]
            if space is None:
                capable_move.add((candidate_x, candidate_y))
            elif space.team != piece.team and attack_piece:
                capable_move.add((candidate_x, candidate_y))
                break
            else:
                break
        return capable_move

    def possibleMovesPawn(self, row, column):
        piece = self.pieces_location[row][column]
        moves = piece.move(row, column)
        attack = piece.attack(row,column)
        possible_moves = self.moveWithOutJump(row, column, moves, False)
        for diagonal in attack:
            candidate_x = row + diagonal[0]
            candidate_y = column + diagonal[1]
            if candidate_x > -1 and candidate_x < 8 and candidate_y > -1 and candidate_y < 8:
                space = self.pieces_location[candidate_x][candidate_y]
                if space is not None and space.team != piece.team:
                    possible_moves.add((candidate_x, candidate_y))
        print('moves')
        print(moves)
        print(attack)
        return possible_moves
            


    def piece_selected(self, row, column):
        piece = self.pieces_location[row][column]
        moves = set()
        check_enemies = piece.attack(row, column)
        possible_moves = piece.move(row, column)
        if piece.name == 'pawn':
            moves=  self.possibleMovesPawn(row, column)
        self.clean_board()
        # keep that if there are some squares
        square_select = self.convert_row_column_to_square(row, column)
        self.square_selected['square_selected'] = square_select
        # self.squares_selected[square_select] = {}
        print('*'*10+'Arguments that are being passe to the board')
        print('{},{},{}'.format(row, column, str(moves)))
        self.square_selected['possible_squares'] = self.board.moves(row, column, moves)

    def clean_board(self):
        if len(self.square_selected) != 0:
            self.board.default_colors(self.square_selected['possible_squares'])
            self.square_selected = {
                'square_selected': None,
                'possible_squares': {}
            }

    def calculate_update_square(self,new_square_cordinates, default_square_size = 50):
        """Calculate where the new piece should appear"""
        y = 100 + (new_square_cordinates['row'] * default_square_size) - 5
        x = 200 + (new_square_cordinates['column'] * default_square_size) - 5
        return {
            'x_update': x,
            'y_update': y
        }

    def move_piece(self, old_square, new_square):
        old_square_cordinates = self.convert_square_to_row_column(old_square)
        new_square_cordinates = self.convert_square_to_row_column(new_square)
        print('old {}'.format(str(old_square_cordinates)))
        print('new {}'.format(str(new_square_cordinates)))
        piece_selected = self.pieces_location[old_square_cordinates['row']][old_square_cordinates['column']]
        possible_place = self.pieces_location[new_square_cordinates['row']][new_square_cordinates['column']]
        new_graphics_location = self.calculate_update_square(new_square_cordinates)
        piece_selected.update(y= new_graphics_location['y_update'], x=new_graphics_location['x_update'])
        if possible_place is not None:
            if piece_selected.team != possible_place.team:
                piece_selected.dead = True
        self.pieces_location[new_square_cordinates['row']][new_square_cordinates['column']] = piece_selected
        self.pieces_location[old_square_cordinates['row']][old_square_cordinates['column']] = None
        piece_selected.first_move = False
        self.clean_board()
        
    def on_mouse_press(self, x, y, button, modifiers):
        # check if board need to be clean
        print(self.square_selected)

        # Determine the square that was selected , how ??
        # make sure that the clikc is inside of the square
        
        if x < 200 or x >= 600 or y < 100 or y >= 500:
            self.clean_board()
        # get index of the square
        x -= 200
        y -= 100
        row = int(y/50)
        column = int(x/50)
        square_selected = row*8 + column
        print('Square selected {}'.format(square_selected))
        if square_selected in self.square_selected['possible_squares']:
            # current piece is going to move to next square
            self.move_piece(self.square_selected['square_selected'],square_selected)
        elif self.pieces_location[row][column] is not None:
            print('possible moves ')
            self.piece_selected(row, column )
        else:
            print('Empty square')
        square_select = 8*row + column