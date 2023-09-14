from chessPiece import chessPiece
from blackAndWhiteLibraries import blackAndWhiteLibraries
class chessSpaces:
    def __init__(self, rank, files, x, y, piece):
        self.square = files + str(rank)
        self.x = x
        self.y = y
        self.piece = piece
        self.chess_piece = chessPiece()
    def get_Chess_Piece(self):
        if(self.spotIsEmpty):
            return self.chess_piece
    def getCordX(self):
        return self.x
    def getCordX(self):
        return self.y
    def getCords(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    def getSquareName(self):
        return self.square
    def killChessPiece(self, piece, team):
        team.add_Piece_To_Dead_Group(piece)
        self.piece = None
        self.chess_piece = chessPiece()
    def removeChessPiece(self, piece):
        self.chess_piece = chessPiece()
    def printSquareName(self):
        print(self.square)
    def spotIsEmpty(self):
        if self.piece:
            return False
        return True
