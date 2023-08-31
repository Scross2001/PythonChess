from abc import ABC, abstractmethod

class chessPiece():  # Abstract class
    def __init__(self):
        self.name = ""
        self.movableSpaces = []
        self.specialMoves = True
        self.color = ""
        self.isAlive = True
    def getChessPieceName(self):
        return self.name
    def kill_Piece(self):
        self.isAlive = False
    def setInitalCords(self, x ,y):
        self.cordX = x
        self.cordY = y
    def printChessPieceName(self):
        print(self.name)
    def getCordX(self):
        return self.cordX
    def getCordY(self):
        return self.cordY
    def printCords(self):
        print(f"({self.cordX},{self.cordY})")
    @abstractmethod
    def getMovableSpaces(self, chessboard):
        pass

class Pawn(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "Pawn" if "Black" in color else "pawn"
        self.color = color
        self.setInitalCords(x, y)
    def getMovableSpaces(self, chessboard):
        startingLocation = chessboard[self.cordX][self.cordY]
        print(f"{self.cordX},{self.cordY}")
        print(startingLocation.square)
        print(f"[ {startingLocation.chess_piece.color} {startingLocation.chess_piece.getChessPieceName()} ]")

class Rook(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "Rook" if "Black" in color else "rook"
        self.color = color
        self.movableSpaces = []
        self.setInitalCords(x, y)
    def getMovableSpaces(self, chessboard):
        startingLocation = chessboard[self.cordX][self.cordY]
        startX = self.cordX
        startY = self.cordY
        sX = startX
        sY = startY
        for down in range(8):
            print(f"({sX},{sY})")
            spot = chessboard[sX][sY]
            if not spot.spotIsEmpty() or sY > 8:
                break
            self.movableSpaces.append(spot)
            sY += 1
        """for right in range(8):
            print(f"({sX},{sY})")
            spot = chessboard[sX][sY]
            if not spot.spotIsEmpty() or sX > 9:
                break
            self.movableSpaces.append(spot)
            sX += 1
        sX = startX
        sY = startY
        for left in range(8):
            spot = chessboard[sX][sY]
            if not spot.spotIsEmpty() or sX < -1:
                break
            self.movableSpaces.append(spot)
            sX -= 1 """
        for x in self.movableSpaces:
            print(x.getSquareName(), end = " ")
        #print(f"{self.cordX},{self.cordY}")
        #print(startingLocation.square)
        #print(f"[ {startingLocation.chess_piece.color} {startingLocation.chess_piece.getChessPieceName()} ]")

class Knight(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "Night" if "Black" in color else "night"
        self.color = color
        self.setInitalCords(x, y)
    def getMovableSpaces(self, chessboard):
        startingLocation = chessboard[self.cordX][self.cordY]
        print(f"{self.cordX},{self.cordY}")
        print(startingLocation.square)
        print(f"[ {startingLocation.chess_piece.color} {startingLocation.chess_piece.getChessPieceName()} ]")

class Bishop(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "Bishop" if "Black" in color else "bishop"
        self.color = color
        self.setInitalCords(x, y)
    def getMovableSpaces(self, chessboard):
        startingLocation = chessboard[self.cordX][self.cordY]
        print(f"{self.cordX},{self.cordY}")
        print(startingLocation.square)
        print(f"[ {startingLocation.chess_piece.color} {startingLocation.chess_piece.getChessPieceName()} ]")

class King(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "King" if "Black" in color else "king"
        self.color = color
        self.setInitalCords(x, y)
    def getMovableSpaces(self, chessboard):
        startingLocation = chessboard[self.cordX][self.cordY]
        print(f"{self.cordX},{self.cordY}")
        print(startingLocation.square)
        print(f"[ {startingLocation.chess_piece.color} {startingLocation.chess_piece.getChessPieceName()} ]")

class Queen(chessPiece):  # Concrete subclass
    def __init__(self, color, x, y):
        self.name = "Queen" if "Black" in color else "queen"
        self.color = color
        self.setInitalCords(x, y)
    def getMovableSpaces(self, chessboard):
        startingLocation = chessboard[self.cordX][self.cordY]
        print(f"{self.cordX},{self.cordY}")
        print(startingLocation.square)
        print(f"[ {startingLocation.chess_piece.color} {startingLocation.chess_piece.getChessPieceName()} ]")
        


