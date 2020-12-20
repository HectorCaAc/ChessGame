import pyglet
from pyglet.window import mouse

from game import pawn, resources, rook, bishop, queen, king, knight


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

        self.previous_move = 'black'
        # self.draw_pawns()

    def draw_pawns(self):
        black_pawns = [195,395,6,0]
        self.draw_figures(black_pawns, 8, 'black', pawn.Pawn, resources.black_pawns, 50, piece_move_up=False)
        white_pawns = [195, 145, 1, 0]
        self.draw_figures(white_pawns, 8, 'white', pawn.Pawn, resources.white_pawns, 50, piece_move_up=True)
    
    def draw_rooks(self):
        rook_white = [195, 95, 0,0]
        rook_black = [195, 445, 7,0]
        self.draw_figures(rook_white, 2, 'white', rook.Rook, resources.white_rook, 350, gaps=7)
        self.draw_figures(rook_black, 2, 'black', rook.Rook, resources.black_rook, 350, gaps=7)
    
    def draw_bishops(self):
        white_bishop = [295, 95,0, 2]
        black_bishop = [295, 445,7,2]
        self.draw_figures(white_bishop, 2, 'white', bishop.Bishop, resources.white_bishop, 150, gaps=3)
        self.draw_figures(black_bishop, 2, 'black', bishop.Bishop, resources.black_bishop, 150, gaps=3)

    def draw_queens(self):
        white_queen = [395, 95, 0,4 ]
        self.draw_figures(white_queen, 1, 'white', queen.Queen, resources.white_queen, 0)
        black_queen = [395,445, 7,4]
        self.draw_figures(black_queen, 1, 'black', queen.Queen, resources.black_queen, 0)

    def draw_kings(self):
        white_king = [345, 95, 0,3]
        black_king = [345, 445,7,3]
        self.draw_figures(white_king, 1, 'white', king.King, resources.white_king, 0)
        self.draw_figures(black_king, 1, 'black', king.King, resources.black_king, 0)
    
    def draw_knigths(self):
        white_knights = [245, 95,0,1]
        black_knights = [245, 445, 7,1]
        self.draw_figures(white_knights, 2, 'white', knight.Knight, resources.white_knights, 250, gaps=5)
        self.draw_figures(black_knights, 2, 'black', knight.Knight, resources.black_knights, 250, gaps=5)


    def draw_figures(self,figure, number_copies, team, class_object, resource, increment_offset, gaps=None, *args, **kwargs):
        """
            TODO: improve the description of this function
                - also improve the data structure use for this. It kinda looks younki
            figure:  Array size 4.
                index = 0 => locaiton of x 2d map
                index = 1 => location of y 2d map
                index = 2 => index row in logic map
                index = 3 => index colum in logic map
            black_start same logic
            number_copies: int number of figures to draw
            gaps: there is space betwen pieces. Default is 1
            team: string. 
        """
        if gaps is None:
            gaps = 1
        start_x = figure[0]
        start_y = figure[1]
        index_row = figure[2]
        index_column = figure[3]
        offset = 0
        for index in range(number_copies):
            print('row {}'.format(index_row))
            print('column {}'.format(index_column+(index*gaps)))
            self.pieces_location[index_row][index_column+(index*gaps)] = class_object(team, resource, start_x+offset, start_y, batch =self.batch, *args, **kwargs)
            offset+= increment_offset


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
        PAWN - knight
        rook- bishop- queen - king ( similar move differnt movement)
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

    def possible_moves_line(self, row, column):
        piece = self.pieces_location[row][column]
        check_positions = piece.move(row, column)
        print('moves that can happend for piece {}'.format(piece.name))
        print(check_positions)
        future_moves = set()
        for dirrection in check_positions:
            stop = False
            index = 0
            while index < len(check_positions[dirrection]) and not stop:
                movement = check_positions[dirrection][index]
                row = movement[0]
                column = movement[1]
                if self.pieces_location[row][column] is None:
                    future_moves.add(movement)
                else:
                    if self.pieces_location[row][column].team != piece.team:
                        future_moves.add(movement)
                    stop = True
                index +=1
        return future_moves
        # return moves

    def possible_moves_pawn(self, row, column):
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
            moves =  self.possible_moves_pawn(row, column)
        elif piece.name == 'rook':
            moves = self.possible_moves_line(row, column)
            print('moves from the rook [{}]'.format(str(moves)))
        elif piece.name == 'bishop':
            moves = self.possible_moves_line(row, column)
        elif piece.name == 'queen':
            moves = self.possible_moves_line(row, column)
        elif piece.name == 'king':
            moves = self.possible_moves_line(row, column)
        elif piece.name == 'knight':
            moves = self.possible_moves_line(row, column)

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
            self.previous_move = 'white' if self.previous_move == 'black' else 'black'
        elif self.pieces_location[row][column] is not None and self.pieces_location[row][column].team != self.previous_move:
            print('possible moves ')
            self.piece_selected(row, column )
        else:
            print('Empty square')
        square_select = 8*row + column