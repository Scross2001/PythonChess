from chessPiece import chessPiece
class chessSpaces:
    def __init__(self, files, rank, x, y, piece):
        self.square = files + str(rank)
        self.x = x
        self.y = y
        self.piece = piece
        self.chess_piece = chessPiece()
    def get_Chess_Piece(self):
        if(self.spotIsEmpty):
            return self.chess_piece
    def getCords(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    def getSquareName(self):
        return self.square
    def printSquareName(self):
        print(self.square)
    def spotIsEmpty(self):
        if self.piece:
            return False
        return True
