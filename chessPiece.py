from abc import ABC, abstractmethod

class chessPiece():  # Abstract class
    def __init__(self):
        self.name = ""
        self.movableSpaces = []
        self.color = ""
        self.isAlive = True
        self.squareName = ""
    def setSquareName(self, squareName):
        self.squareName = squareName
    def getSquareName(self):
        return self.squareName
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
    @abstractmethod
    def movePiece(self, chessboard):
        pass