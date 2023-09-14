from chessPiece import chessPiece

class Bishop(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y, squareName):
        self.name = "Bishop" if "Black" in color else "bishop"
        self.color = color
        self.setInitalCords(x, y)
        self.squareName = squareName
    
    def getMovableSpaces(self, chessboard):
        self.movableSpaces = []
        self.movableSpaces.append(self.name)
        startingLocation = chessboard[self.cordX][self.cordY]

        diagonal_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in diagonal_moves:
            x, y = self.cordX + dx, self.cordY + dy
            # Continue moving diagonally until the edge of the board is reached
            while 0 <= x < 8 and 0 <= y < 8:
                destination = chessboard[x][y]

                if destination.piece is False:
                    self.movableSpaces.append(destination)
                elif destination.piece and destination.chess_piece.color != self.color:
                    # Capture the opponent's piece and stop searching in this direction
                    self.movableSpaces.append(destination)
                    break
                else:
                    # Can't move through your own piece, stop searching in this direction
                    break

                x += dx
                y += dy

        """ print(f"{self.color} Bishop at {startingLocation.getSquareName()} can move to: ",end="")
        for move in self.movableSpaces:
            print(move.getSquareName(),end= " ")
        print() """

        return self.movableSpaces