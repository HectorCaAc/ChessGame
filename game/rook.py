from game import piece

class Rook(piece.Piece):

    def __init__(self, team, *args, **kwargs):
        super(Rook, self).__init__(*args, **kwargs)
        self.name = "rook"
        self.team = team

    def move(self, current_row, current_column):
        dirrections = [['up',1,0], ['down',-1,0], ['right',0,1],['left',0,-1]]
        positions_to_check = {}
        candidate_x = current_row
        candidate_y = current_column
        for dirrection, add_x, add_y in dirrections:
            candidate_x = current_row + add_x
            candidate_y = current_column + add_y
            positions_to_check[dirrection]= []
            while candidate_x > -1 and candidate_x < 8 and candidate_y> -1 and candidate_y < 8:
                positions_to_check[dirrection].append((candidate_x ,candidate_y))
                candidate_x += add_x
                candidate_y += add_y
        return positions_to_check