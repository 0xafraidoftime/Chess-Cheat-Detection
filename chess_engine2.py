
import chess.pgn
import re

def extract_centipawn_loss(comment):
    """Extract centipawn loss from the move comment, if present."""
    match = re.search(r"\[%eval\s([+-]?\d+\.\d+)\]", comment)
    if match:
        return float(match.group(1)) * 100  # Convert to centipawns (1 pawn = 100 centipawns)
    return None

def check_cheating(game):
    cheating_detected = False
    node = game  # Start with the root node of the game
    while node.variations:
        for variation in node.variations:
            move = variation.move
            comment = variation.comment
            # Extract centipawn loss (if available)
            centipawn_loss = extract_centipawn_loss(comment)
            
            if centipawn_loss is not None:
                # If the centipawn loss is significant (you can adjust this threshold)
                if abs(centipawn_loss) > 50:  # 50 centipawns (half a pawn) as a threshold
                    cheating_detected = True
                    player = "White" if game.board().turn == chess.WHITE else "Black"
                    print(f"Potential cheating detected at move {game.board().san(move)} by {player}: Centipawn loss: {centipawn_loss} (Comment: {comment})")
            elif "Inaccuracy" in comment or "Mistake" in comment or "Blunder" in comment:
                cheating_detected = True
                player = "White" if game.board().turn == chess.WHITE else "Black"
                print(f"Potential cheating detected at move {game.board().san(move)} by {player}: {comment}")
            
            node = variation
    return cheating_detected

def analyze_game(pgn_file):
    with open(pgn_file) as f:
        game = chess.pgn.read_game(f)
    
    cheating_detected = check_cheating(game)
    if cheating_detected:
        print("Potential cheating detected in the game.")
    else:
        print("No cheating detected in the game.")

# Path to your saved annotated game file
pgn_file = 'a.pgn'
analyze_game(pgn_file)