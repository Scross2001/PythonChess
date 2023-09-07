from chessPiece import chessPiece

class Rook(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "Rook" if "Black" in color else "rook"
        self.color = color
        self.movableSpaces = []
        self.setInitalCords(x, y)

    def getMovableSpaces(self, chessboard):
        self.movableSpaces = []
        self.movableSpaces.append(self.name)
        startingLocation = chessboard[self.cordX][self.cordY]

        # Horizontal movement (right)
        for i in range(self.cordX + 1, 8):
            if chessboard[i][self.cordY].piece:
                if chessboard[i][self.cordY].chess_piece.color != self.color:
                    self.movableSpaces.append(chessboard[i][self.cordY])  # Capture opponent's piece
                break
            else:
                self.movableSpaces.append(chessboard[i][self.cordY])

        # Horizontal movement (left)
        for i in range(self.cordX - 1, -1, -1):
            if chessboard[i][self.cordY].piece:
                if chessboard[i][self.cordY].chess_piece.color != self.color:
                    self.movableSpaces.append(chessboard[i][self.cordY])  # Capture opponent's piece
                break
            else:
                self.movableSpaces.append(chessboard[i][self.cordY])

        # Vertical movement (up)
        for i in range(self.cordY + 1, 8):
            if chessboard[self.cordX][i].piece:
                if chessboard[self.cordX][i].chess_piece.color != self.color:
                    self.movableSpaces.append(chessboard[self.cordX][i])  # Capture opponent's piece
                break
            else:
                self.movableSpaces.append(chessboard[self.cordX][i])

        # Vertical movement (down)
        for i in range(self.cordY - 1, -1, -1):
            if chessboard[self.cordX][i].piece:
                if chessboard[self.cordX][i].chess_piece.color != self.color:
                    self.movableSpaces.append(chessboard[self.cordX][i])  # Capture opponent's piece
                break
            else:
                self.movableSpaces.append(chessboard[self.cordX][i])
        
        """ print(f"{self.color} Rook at {startingLocation.getSquareName()} can move to: ",end="")
        for move in self.movableSpaces:
            print(move.getSquareName(),end= " ")
        print() """
        return self.movableSpaces