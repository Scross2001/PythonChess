class chessSpaces:
    def __init__(self, files, rank, x, y, piece):
        self.square = files + str(rank)
        self.x = x
        self.y = y
        self.piece = piece

    def getCords(self):
        return "(" + self.x + "," + self.y + ")"
    def getSquareName(self):
        return self.square
    def printSquareName(self):
        print(self.square)
    def spotIsEmpty(self):
        if self.piece:
            return False
        return True
