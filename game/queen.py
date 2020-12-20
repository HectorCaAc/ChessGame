from game import piece

class Queen(piece.Piece):

    def __init__(self, team, *args, **kwargs):
        super(Queen, self).__init__(*args, **kwargs)
        self.team = team
        self.name = 'queen'
    
    def move(self, current_row, current_column):
        dirrections = [['up',0,1], ['down', 0,-1], ['left', -1,0], ['right', 1,0],['right_up', 1,1], ['left_up', 1,-1], ['right_down',-1,1],['left_down',-1,-1]]
        return super(Queen, self).line_movement(current_row, current_column, dirrections)