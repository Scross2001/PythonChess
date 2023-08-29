from chessSpaces import chessSpaces
maxY = 1000
maxX = 1000
class chessBoard:
    def __init__(self):
        self.chessboard = []
        self.Initalizing_Chessboard()
    def Initalizing_Chessboard(self):
        matrix = []
        global maxX
        global maxY
        for x in range(1, 9):
            row = []
            for y in range(1, 9):
                row.append(chessSpaces(chr(x+64), y, (maxX/x), (maxY/y), False))
            matrix.append(row)
        self.chessboard = matrix
    def printChessCords(self):
        for row in self.chessboard:
            for space in row:
                print(f"({space.getSquareName()})", end=" ")
            print()



my_chess = chessBoard()
my_chess.printChessCords()