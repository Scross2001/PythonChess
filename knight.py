from chessPiece import chessPiece

class Knight(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "Night" if "Black" in color else "night"
        self.color = color
        self.setInitalCords(x, y)

    def getMovableSpaces(self, chessboard):
        self.movableSpaces = []
        startingLocation = chessboard[self.cordX][self.cordY]
        knight_moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

        for dx, dy in knight_moves:
            new_x, new_y = self.cordX + dx, self.cordY + dy

            if 0 <= new_x < 8 and 0 <= new_y < 8:
                destination = chessboard[new_x][new_y]

                if destination.piece is False or destination.chess_piece.color != self.color:
                    self.movableSpaces.append(destination)

        print(f"{self.color} Knight at {startingLocation.getSquareName()} can move to: ",end="")
        for move in self.movableSpaces:
            print(move.getSquareName(),end= " ")
        print()
        return self.movableSpaces