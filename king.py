from chessPiece import chessPiece

class King(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "King" if "Black" in color else "king"
        self.color = color
        self.setInitalCords(x, y)
    def getMovableSpaces(self, chessboard):
        startingLocation = chessboard[self.cordX][self.cordY]