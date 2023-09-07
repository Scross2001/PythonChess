from chessPiece import chessPiece

class Queen(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "Queen" if "Black" in color else "queen"
        self.color = color
        self.setInitalCords(x, y)
   
    def getMovableSpaces(self, chessboard):
        self.movableSpaces = []
        self.movableSpaces.append(self.name)
        startingLocation = chessboard[self.cordX][self.cordY]

        diagonal_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        straight_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in diagonal_moves:
            x, y = self.cordX + dx, self.cordY + dy

            # Continue moving diagonally until the edge of the board is reached
            while 0 <= x < 8 and 0 <= y < 8:
                destination = chessboard[x][y]

                if destination.chess_piece.color in self.color:
                    break

                if destination.piece is False or destination.chess_piece.color != self.color:
                    self.movableSpaces.append(destination)

                    if destination.piece:
                        break
                x += dx
                y += dy

        for dx, dy in straight_moves:
            x, y = self.cordX + dx, self.cordY + dy

            # Continue moving straight until the edge of the board is reached
            while 0 <= x < 8 and 0 <= y < 8:
                destination = chessboard[x][y]

                if destination.chess_piece.color in self.color:
                    break

                if destination.piece is False or destination.chess_piece.color != self.color:
                    self.movableSpaces.append(destination)

                    if destination.piece:
                        break
                x += dx
                y += dy

        """ print(f"{self.color} Queen at {startingLocation.getSquareName()} can move to: ",end="")
        for move in self.movableSpaces:
            print(move.getSquareName(),end= " ")
        print() """

        return self.movableSpaces