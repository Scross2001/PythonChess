from chessPiece import chessPiece

class King(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "King" if "Black" in color else "king"
        self.color = color
        self.movableSpaces = []
        self.setInitalCords(x, y)
    def getMovableSpaces(self, chessboard):
        self.movableSpaces = []
        self.movableSpaces.append(self.name)
        king_moves = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        startingLocation = chessboard[self.cordX][self.cordY]

        for dx,dy in king_moves:
            new_x, new_y = self.cordX + dx, self.cordY + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                destination = chessboard[new_x][new_y]
                if destination.piece is False or destination.chess_piece.color != self.color:
                        self.movableSpaces.append(destination)
        return self.movableSpaces