from game import piece

class Rook(piece.Piece):

    def __init__(self, team, *args, **kwargs):
        super(Rook, self).__init__(*args, **kwargs)
        self.name = "rook"
        self.team = team

    def move(self, current_row, current_column):
        dirrections = [['up',1,0], ['down',-1,0], ['right',0,1],['left',0,-1]]
        return super(Rook, self).line_movement(current_row, current_column, dirrections)