from chessPiece import chessPiece, abstractmethod
class blackAndWhiteLibraries:
    #This class should have cords on where the dead things are outside of the chess map
    def __init__(self, blackOrWhite):
        self.name = blackOrWhite
        self.allDeadPieces = []
        self.allAlivePieces = []
        self.allPossibleMoves = []
    
    def get_All_Possible_Moves_For_All_Alive_Pieces(self, chessboard):
        for pieces in self.allAlivePieces:
            pieces.getMovableSpaces(chessboard)

    def add_Piece_To_Alive_List(self, piece):
        self.allAlivePieces.append(piece)
    def find_Piece_From_Dead_Or_Alive(self, isItAlive, piece):
        if(isItAlive):
            for aliveOrDeadPiece in self.allAlivePieces:
                if aliveOrDeadPiece.getCords() in piece.getCords():
                    return aliveOrDeadPiece
    def add_Piece_To_Dead_Group(self, piece):
        alivePiece = self.find_Piece_From_Dead_Or_Alive(piece)
        self.allAlivePieces.remove(alivePiece)
        self.allDeadPieces.append(alivePiece)
    
    def Print_Alive_And_Dead_Groups(self):
        print(f"\t\t{self.name} Alive Group\t\t")
        for alive in self.allAlivePieces:
            print(f"{alive.name} ({alive.getCordX()},{alive.getCordY()})")
        print(f"\t\t{self.name} Dead Group")
        for dead in self.allDeadPieces:
            print(f"{dead.name}")



