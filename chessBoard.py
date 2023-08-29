from chessSpaces import chessSpaces
from blackAndWhiteLibraries import blackAndWhiteLibraries
from chessPiece import Pawn
maxY = 1000
maxX = 1000
class chessBoard:

    def __init__(self):
        self.chessboard = []
        self.black_Team = blackAndWhiteLibraries("Black")
        self.white_Team = blackAndWhiteLibraries("White")
        self.Initalizing_Chessboard()
        self.Initalizing_Chess_Pieces()

    def Initalizing_Chessboard(self):
        array = []
        global maxX
        global maxY
        for x in range(1, 9):
            row = []
            for y in range(1, 9):
                row.append(chessSpaces(chr(x+64), y, x, y, False))
            array.append(row)
        self.chessboard = array

    def Initalizing_Chess_Pieces(self):
        for row in self.chessboard:
            for space in row:
                if "B" in space.getSquareName():
                    pawn = Pawn()
                    pawn.setInitalCords(space.x,space.y)
                    space.piece = True
                elif "G" in space.getSquareName():
                    pawn = Pawn()
                    pawn.setInitalCords(space.x,space.y)
                    space.piece = True

    def printChessCords(self):
        for row in self.chessboard:
            for space in row:
                print(f"({space.piece})", end=" ")
                #print(f"({space.getSquareName()})", end=" ")
            print()