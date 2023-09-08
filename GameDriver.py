from chessBoard import chessBoard

def main():
    # Initialize the chessboard
    chessboard = chessBoard()
    current_team = "White"  # Start with White's turn

    while True:
        # Print the current state of the chessboard
        chessboardMap = chessboard.get_Chessboard()
        chessboard.Get_Chess_Piece_Locations()

        # Check if the current team's king is in check or checkmate
        if current_team == "White":
            check_result = chessboard.white_Team.check_King_Is_Checked_Or_Checkmated(chessboardMap, chessboard.black_Team)
        else:
            check_result = chessboard.black_Team.check_King_Is_Checked_Or_Checkmated(chessboardMap, chessboard.white_Team)

        if not check_result:
            print(f"{current_team} king is not in check or checkmate.")
        elif isinstance(check_result, list):
            print(f"{current_team} king is in check. Possible moves to get out of check:")
            for move in check_result:
                print(move.getSquareName(), end=" ")
            print()
        else:
            print(f"{current_team} king is in checkmate. Game over!")
            break

        # Get player move
        move = input(f"Enter your move for {current_team} (e.g., 'e2 e4'): ")
        # TODO: Implement move logic based on user inputd.

        # Toggle the current team
        current_team = "White" if current_team == "Black" else "Black"

if __name__ == "__main__":
    main()
