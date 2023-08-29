class chessSpaces:
    def __init__(self, files, rank, x, y, peace):
        self.square = files + str(rank)
        self.x = x
        self.y = y
        self.peace = peace

    def getCords(self):
        return "(" + self.x + "," + self.y + ")"
    def getSquareName(self):
        return self.square
    def printSquareName(self):
        print(self.square)
