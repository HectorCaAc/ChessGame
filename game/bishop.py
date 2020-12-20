from game import piece

class Bishop(piece.Piece):

    def __init__(self, team, *args, **kwargs):
        super(Bishop, self).__init__(*args, **kwargs)
        self.name = 'bishop'
        self.team = team

    def move(self, current_row, current_column):
        dirrections = [['right_up', 1,1], ['left_up', 1,-1], ['right_down',-1,1],['left_down',-1,-1]]
        return super(Bishop, self).line_movement(current_row, current_column, dirrections)
