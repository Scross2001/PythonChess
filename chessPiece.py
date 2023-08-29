
from abc import ABC, abstractmethod

class chessPiece(ABC):  # Abstract class
    def __init__(self):
        self.name = ""
        self.movableSpaces = []
        self.specialMoves = True
        self.initalCordX
        self.initalCordY
    def getChessPieceName(self):
        return self.name
    def setInitalCords(self, x ,y):
        self.initalCordX = x
        self.initalCordX = y
    def printChessPieceName(self):
        print(self.name)
    def setChessPieceName(self, name):
        self.name = name
    @abstractmethod
    def getMovableSpaces(self):
        pass  # This method must be implemented by concrete subclasses

class Pawn(chessPiece):  # Concrete subclass
    def __init__(self):
        chessPiece.setChessPieceName("Pawn")
    def getMovableSpaces(self):
        return self.movableSpaces


