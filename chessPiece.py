from abc import ABC, abstractmethod

class chessPiece():  # Abstract class
    def __init__(self):
        self.name = ""
        self.movableSpaces = []
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
        self.hasMoved = False
        self.movableSpaces = []
        self.setInitalCords(x, y)
    def getMovableSpaces(self, chessboard):
        self.movableSpaces = []
        startingLocation = chessboard[self.cordX][self.cordY]
        
        if(self.hasMoved == False):
            if(chessboard[self.cordX+2][self.cordY].piece == False):
                self.movableSpaces.append(chessboard[self.cordX + 2][self.cordY])
            elif(chessboard[self.cordX-2][self.cordY].piece == False):
                self.movableSpaces.append(chessboard[self.cordX - 2][self.cordY])
            if(chessboard[self.cordX + 1][self.cordY].piece == False and "Black" in self.color ):
                self.movableSpaces.append(chessboard[self.cordX + 1][self.cordY])
            elif(chessboard[self.cordX - 1][self.cordY].piece == False and "White" in self.color):
                self.movableSpaces.append(chessboard[self.cordX][self.cordY])
        else:
            if(chessboard[self.cordX + 1][self.cordY].piece == False and "Black" in self.color ):
                self.movableSpaces.append(chessboard[self.cordX][self.cordY])
            elif(chessboard[self.cordX - 1][self.cordY].piece == False and "White" in self.color):
                self.movableSpaces.append(chessboard[self.cordX][self.cordY])
        print(startingLocation.chess_piece.name, end = "[ ")
        for x in self.movableSpaces:
            print(x.getSquareName(), end = " ")
        print("]")
        return self.movableSpaces


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
        while chessboard[startX+1][startY].piece == False:
            self.movableSpaces.append(chessboard[startX+1][startY])
            startX += 1
        for x in self.movableSpaces:
            print(x.getSquareName(), end = " ")

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
        


