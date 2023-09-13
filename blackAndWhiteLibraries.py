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

    def print_All_Possible_Moves_For_All_Alive_Pieces(self, chessboard):
        for pieces in self.allAlivePieces:
            pieces.getMovableSpaces(chessboard)

    def get_All_Possible_Moves_For_King(self, chessboard):
        for pieces in self.allAlivePieces:
            if "ing" in pieces.name:
                return pieces.getMovableSpaces(chessboard)

    def find_King(self, chessboard):
        for row in chessboard:
            for space in row:
                if "ing" in space.chess_piece.name and self.name in space.chess_piece.color:
                    return space

    def check_King_Is_Checked_Or_Checkmated(self, chessboard, opponets):
        allPossibleOpponetsMoves = []
        kingLocation = self.find_King(chessboard)
        kingsMoves = self.get_All_Possible_Moves_For_King(chessboard)
        kingsMovesAfterCheck = []
        #print(kingLocation.square)
        for pieces in opponets.allAlivePieces:
            if "ing" not in pieces.name:
                opponets.allPossibleMoves.append(pieces.getMovableSpaces(chessboard))
        for piece in opponets.allPossibleMoves:
            for i in range(1,len(piece)):
                if piece[i].square not in allPossibleOpponetsMoves:
                    allPossibleOpponetsMoves.append(piece[i].square)
        kingsMoves.pop(0)
        #print(allPossibleOpponetsMoves)
        #print(kingsMoves)
        if kingLocation.square not in allPossibleOpponetsMoves:
            print("Hurray Not Checkmate!!!!")
            return self.get_All_Possible_Moves_For_All_Alive_Pieces(chessboard)
        else:
            print("Checkmate")
            """ for move in kingsMoves:
                if move.square not in allPossibleOpponetsMoves:
                    kingsMovesAfterCheck.append(move.square)
            if not kingsMovesAfterCheck:
                print("Checkmate")
            else:
                print(kingsMovesAfterCheck)
                return kingsMovesAfterCheck """
        

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



