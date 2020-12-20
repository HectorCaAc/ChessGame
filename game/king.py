from game import piece

class King(piece.Piece):

    def __init__(self, team, *args, **kwargs):
        super(King, self).__init__(*args, **kwargs)
        self.team = team
        self.name = 'king'
    
    def move(self, current_row, current_column):
        dirrections = [['up',0,1], ['down', 0,-1], ['left', -1,0], ['right', 1,0],['right_up', 1,1], ['left_up', 1,-1], ['right_down',-1,1],['left_down',-1,-1]]
        return super(King, self).one_movement(current_row, current_column, dirrections)