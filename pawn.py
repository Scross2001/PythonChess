from chessPiece import chessPiece

class Pawn(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y, squareName):
        self.name = "Pawn" if "Black" in color else "pawn"
        self.color = color
        self.hasMoved = False
        self.movableSpaces = []
        self.setInitalCords(x, y)
        self.squareName = squareName
    def getMovableSpaces(self, chessboard):
        self.movableSpaces = []
        self.movableSpaces.append(self.name)
        startingLocation = chessboard[self.cordX][self.cordY]

        if "Black" in self.color:
            if chessboard[self.cordX + 1][self.cordY].piece is False:
                self.movableSpaces.append(chessboard[self.cordX + 1][self.cordY])
                if not self.hasMoved and chessboard[self.cordX + 2][self.cordY].piece is False:
                    self.movableSpaces.append(chessboard[self.cordX + 2][self.cordY])

            # Capture to the right
            if self.cordY < 7 and chessboard[self.cordX + 1][self.cordY + 1].piece:
                if chessboard[self.cordX + 1][self.cordY + 1].chess_piece.color != self.color:
                    self.movableSpaces.append(chessboard[self.cordX + 1][self.cordY + 1])

            # Capture to the left
            if self.cordY > 0 and chessboard[self.cordX + 1][self.cordY - 1].piece:
                if chessboard[self.cordX + 1][self.cordY - 1].chess_piece.color != self.color:
                    self.movableSpaces.append(chessboard[self.cordX + 1][self.cordY - 1])
        else:  # White Pawn
            if chessboard[self.cordX - 1][self.cordY].piece is False:
                self.movableSpaces.append(chessboard[self.cordX - 1][self.cordY])
                if not self.hasMoved and chessboard[self.cordX - 2][self.cordY].piece is False:
                    self.movableSpaces.append(chessboard[self.cordX - 2][self.cordY])

            # Capture to the right
            if self.cordY < 7 and chessboard[self.cordX - 1][self.cordY + 1].piece:
                if chessboard[self.cordX - 1][self.cordY + 1].chess_piece.color != self.color:
                    self.movableSpaces.append(chessboard[self.cordX - 1][self.cordY + 1])

            # Capture to the left
            if self.cordY > 0 and chessboard[self.cordX - 1][self.cordY - 1].piece:
                if chessboard[self.cordX - 1][self.cordY - 1].chess_piece.color != self.color:
                    self.movableSpaces.append(chessboard[self.cordX - 1][self.cordY - 1])

        return self.movableSpaces