from chessPiece import chessPiece, abstractmethod
class blackAndWhiteLibraries:
    def __init__(self, blackOrWhite):
        if "Black" in blackOrWhite:
            self.name = "Black"
        else:
            self.name = "White"
        self.dumpster = []
        self.allAlivePieces = []

    def addPieceToTeam(self, piece):
        self.allAlivePieces.append(piece)
    #def allPossibleMovement(self):


