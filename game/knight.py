from game import piece

class Knight(piece.Piece):

    def __init__(self, team, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.team = team
        self.name = 'knight'
    
    def move(self, current_row, current_column):
        dirrections = [['up',2,1], ['up_right', 1,2], ['right', -1,2], ['down_right', -2,1],['left', -2,-1], ['down_left', -1,-2], ['left_up',1,-2],['up_left',2,-1]]
        return super(Knight, self).one_movement(current_row, current_column, dirrections)