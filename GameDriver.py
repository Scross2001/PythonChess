from chessBoard import chessBoard

chessboard = chessBoard()
chessboard.Get_Chess_Piece_Locations()
print()
chessboard.Get_Board_Spot_Numers_And_Cords()
print()
chessboard.Get_Board_FEN_Map()
print()
for row in chessboard.get_Chessboard():
    for column in row:
        print(column.square, end = "")
    print("")
#print(chessboard.get_Chessboard()[7][7].get_Chess_Piece().name)
#print(chessboard.get_Chessboard()[7][7].getCords())
chessboard.get_Chessboard()[0][0].get_Chess_Piece().getMovableSpaces(chessboard.get_Chessboard())