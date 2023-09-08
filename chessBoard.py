from chessSpaces import chessSpaces
from blackAndWhiteLibraries import blackAndWhiteLibraries
from pawn import Pawn
from queen import Queen
from king import King
from knight import Knight
from bishop import Bishop
from rook import Rook
MAXX = 1000
MAXY = 1000
STARTING_COLOR = "BLACK"
class chessBoard:

    def __init__(self):
        self.chessboard = []
        self.black_Team = blackAndWhiteLibraries("Black")
        self.white_Team = blackAndWhiteLibraries("White")
        self.Initalizing_Chessboard()
        self.Initalizing_Chess_Pieces()
    
    def get_Chessboard(self):
        return self.chessboard

    def Initalizing_Chessboard(self):
        array = []
        for x in range(0, 8):
            row = []
            for y in range(0, 8):
                row.append(chessSpaces(x + 1, chr(y + 65), x, y, False))
            array.append(row)
        self.chessboard = array
    
    def Initalizing_Pawns(self, color, row):
        for column in row:
            pawn = Pawn(color, column.x, column.y)
            column.piece = True
            column.chess_piece = pawn
            self.Add_Piece_To_Alive_Group(color, pawn)
    #def movePiece(self, current, newSpot, color):
        

    def Add_Piece_To_Alive_Group(self, color, piece):
        if "Black" in color:
            self.black_Team.add_Piece_To_Alive_List(piece)
        else:
            self.white_Team.add_Piece_To_Alive_List(piece)
    def Initalize_Special_Pieces(self, spot, color, piece):
        spot.piece = True
        spot.chess_piece = piece
        self.Add_Piece_To_Alive_Group(color, piece)
    def Initalizing_KQ_Rows(self, color, row):
        x = 1
        for column in row:
            if(x == 1 or x == 8):
                self.Initalize_Special_Pieces(column, color, Rook(color, column.x, column.y))
            elif(x == 2 or x == 7):
                self.Initalize_Special_Pieces(column, color, Knight(color, column.x, column.y))
            elif(x == 3 or x == 6):
                self.Initalize_Special_Pieces(column, color, Bishop(color, column.x, column.y))
            elif(x == 4):
                self.Initalize_Special_Pieces(column, color, King(color, column.x, column.y))
            elif(x == 5):
                self.Initalize_Special_Pieces(column, color, Queen(color, column.x, column.y))
            x += 1

    def Initalizing_Chess_Pieces(self): #Initalizing the whole board and Initalizing the object pieces
        for row in self.chessboard:
            if "1" in row[0].getSquareName():
                self.Initalizing_KQ_Rows("Black", row)
            elif "8" in row[0].getSquareName():
                self.Initalizing_KQ_Rows("White", row)
            elif "7" in row[0].getSquareName():
                self.Initalizing_Pawns("White", row)
                #self.Initalizing_Pawns("Black", row)
            elif "2" in row[0].getSquareName():
                #self.Initalizing_KQ_Rows("Black", row)
                self.Initalizing_Pawns("Black", row)
            else:
                for column in row:
                    column.piece = False
        

    def Get_Board_FEN_Map(self):
        for row in self.chessboard:
            amount_of_blank_spaces = 0
            for column in row:
                if not column.spotIsEmpty():
                    print(column.chess_piece.getChessPieceName()[0], end="")
                    if amount_of_blank_spaces > 0:
                        print(amount_of_blank_spaces, end="")
                        amount_of_blank_spaces = 0
                else:
                    amount_of_blank_spaces += 1
            
            if amount_of_blank_spaces > 0:
                print(amount_of_blank_spaces, end="")
            print("/", end="")
        print
    print()

    def Get_Chess_Piece_Locations(self): #Prints the chess board with files and numbers
        x = 1
        for row in self.chessboard:
            print(f"{str(x)}", end=" ")
            for space in row:
                if space.spotIsEmpty() == False:
                    print(f"[  {space.chess_piece.getChessPieceName()[0]}  ]", end=" ")
                else:
                    print(f"[     ]", end=" ")
            print()
            x += 1

        print("     A       B       C       D       E       F       G       H   ")
    def Get_Chess_Piece_Truth_Locations(self): #Prints the chess board with files and numbers
        x = 1
        for row in self.chessboard:
            print(f"{str(x)}", end=" ")
            for space in row:
                if space.spotIsEmpty() == False:
                    print(f"[{space.piece} ]", end=" ")
                else:
                    print(f"[{space.piece}]", end=" ")
            print()
            x += 1

        print("     A       B       C       D       E       F       G       H   ")
    def Print_Each_Teams_Alive_Pieces(self):
        self.black_Team.Print_Alive_And_Dead_Groups()
        self.white_Team.Print_Alive_And_Dead_Groups()

    def Get_Board_Spot_Numers_And_Cords(self): #prints the spot cords and name of the spot
        for row in self.chessboard:
            for column in row:
                print(f"[{column.getCords()},{column.getSquareName()}]", end=" ")
            print()