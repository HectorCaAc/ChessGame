from game import piece

class Pawn(piece.Piece):

    def __init__(self, team, *args, **kwargs):
        print('Inside of the Pawn class')
        print(args)
        print(kwargs)
        value_move_up = kwargs['piece_move_up']
        del kwargs['piece_move_up']
        print(kwargs)
        super(Pawn, self).__init__(*args, **kwargs)
        self.move_up = value_move_up
        self.name = "pawn"
        self.team = team
        print('pawn created ')

    def move(self, current_row, current_column):
        # Pawn arrived to the other side of the board
        if current_row == 7 or current_row == 0:
            return {}
        possible_moves = set()
        if self.move_up:
            possible_moves.add((1,0))
            if self.first_move:
                possible_moves.add((2,0))
        else:
            possible_moves.add((-1,0))
            if self.first_move:
                possible_moves.add((-2,0))
        return possible_moves

    def attack(self, current_row, current_column):
        check_enemies = set()
        if self.move_up:
            check_enemies.add((1, -1))
            check_enemies.add((1,1))
        else:
            check_enemies.add((-1,-1))
            check_enemies.add((-1,1))
        return check_enemies
