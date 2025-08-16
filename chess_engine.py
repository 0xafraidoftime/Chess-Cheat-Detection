import chess.pgn

def parse_pgn(file_path):
    """Parses a PGN file and extracts moves."""
    with open(file_path) as pgn:
        game = chess.pgn.read_game(pgn)  # Load the game
        board = game.board()  # Initialize an empty board
        moves = []

        for move in game.mainline_moves():
            moves.append(move.uci())  # Convert move to UCI format
            board.push(move)  # Apply move to the board

        return moves

# ✅ List of PGN files to parse
pgn_files = ["game.pgn", "new_game.pgn"]  # Add more PGN files if needed

# ✅ Loop through each PGN file and parse moves
for file in pgn_files:
    print(f"\n📂 Parsing PGN File: {file}")
    parsed_moves = parse_pgn(file)
    print("Parsed Moves:", parsed_moves)
