from game import piece

class Pawn(piece.Piece):

    def __init__(self, move_up, team, *args, **kwargs):
        super(Pawn, self).__init__(*args, **kwargs)
        self.move_up = move_up
        self.name = "pawn"
        self.team = team

    def move(self):
        possible_moves = set()
        if self.move_up:
            possible_moves.add((0,1))
            if self.first_move:
                possible_moves.add((0,2))
        else:
            possible_moves.add((0,-1))
            if self.first_move:
                possible_moves.add((0,-2))
        return possible_moves

    
