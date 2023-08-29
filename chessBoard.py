from chessSpaces import chessSpaces
maxY = 1000
maxX = 1000
class chessBoard:
    def __init__(self):
        self.chessboard = []
        self.Initalizing_Chessboard()
    def Initalizing_Chessboard(self):
        array = []
        global maxX
        global maxY
        for x in range(1, 9):
            row = []
            for y in range(1, 9):
                row.append(chessSpaces(chr(x+64), y, (maxX/x), (maxY/y), False))
            array.append(row)
        self.chessboard = array
    def Initalizing_Chess_Pieces(self):
        for row in self.chessboard:
            for space in row:
                if "B" in space.getSquareName():
                    print("")
                elif "G" in space.getSquareName():
                    print("")
    def printChessCords(self):
        for row in self.chessboard:
            for space in row:
                print(f"({space.getSquareName()})", end=" ")
            print()



my_chess = chessBoard()
my_chess.printChessCords()