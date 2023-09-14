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
        for piece in self.allAlivePieces:
            possiblePieceMoves = piece.getMovableSpaces(chessboard)
            print(f"{piece.getSquareName()} {possiblePieceMoves[0]} is able to move to: ", end="")
            for i in range(1,len(possiblePieceMoves)):
                print(possiblePieceMoves[i].square,end=" ")
            print()
    
    def check_If_Move_Is_Possible(self, currentSpot, possibleSpot, chessboard):
        allMovableSpaces = currentSpot.chess_piece.getMovableSpaces(chessboard)
        if possibleSpot in allMovableSpaces:
                return True
        return False
    
    def move_peiece(self, currentSpot, possibleSpot, opposing, chessboard):
        allMovableSpaces = currentSpot.chess_piece.getMovableSpaces(chessboard)
        if possibleSpot in allMovableSpaces:
            if possibleSpot.piece:
                opposing.add_Piece_To_Dead_Group(possibleSpot.chess_piece)
            possibleSpot.chess_piece = currentSpot.chess_piece
            possibleSpot.piece = True
            currentSpot.piece = False
            currentSpot.chess_piece = chessPiece()
            possibleSpot.chess_piece.setInitalCords(possibleSpot.x, possibleSpot.y)
            possibleSpot.chess_piece.squareName = possibleSpot.square
    
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
    def find_Alive_Piece(self, piece):
        for alivePiece in self.allAlivePieces:
            if alivePiece.squareName in piece.squareName:
                return alivePiece
    def add_Piece_To_Dead_Group(self, piece):
        alivePiece = self.find_Alive_Piece(piece)
        self.allAlivePieces.remove(alivePiece)
        self.allDeadPieces.append(alivePiece)
    
    def Print_Alive_And_Dead_Groups(self):
        print(f"\t\t{self.name} Alive Group\t\t")
        for alive in self.allAlivePieces:
            print(f"{alive.name} is at location = {alive.getSquareName()}")
        print(f"\t\t{self.name} Dead Group")
        for dead in self.allDeadPieces:
            print(f"{dead.name}")



