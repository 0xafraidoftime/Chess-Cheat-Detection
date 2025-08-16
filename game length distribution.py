import chess.pgn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def parse_pgn(file_path):
    """Parses a PGN file and extracts moves & metadata."""
    with open(file_path) as pgn:
        game = chess.pgn.read_game(pgn)
        board = game.board()
        moves = []
        move_san_list = []
        
        for move in game.mainline_moves():
            moves.append(move.uci())  # Convert move to UCI format
            move_san_list.append(board.san(move))  # Get move notation
            board.push(move)  # Apply move to board
            
        return moves, move_san_list, len(moves)  # Return moves, notation, and game length

def analyze_games(pgn_files):
    """Extracts move statistics from multiple PGN files."""
    data = []
    
    for file in pgn_files:
        print(f"\n📂 Analyzing PGN File: {file}")
        moves, move_san_list, game_length = parse_pgn(file)
        
        data.append({
            "PGN File": file,
            "Total Moves": game_length,
            "First Move": move_san_list[0] if move_san_list else "N/A",
            "Most Frequent Move": Counter(move_san_list).most_common(1)[0][0] if move_san_list else "N/A"
        })

    return pd.DataFrame(data)

def plot_game_lengths(df):
    """Plot game length distribution."""
    plt.figure(figsize=(8,5))
    sns.barplot(x="PGN File", y="Total Moves", data=df)
    plt.title("Game Length Distribution")
    plt.xlabel("PGN File")
    plt.ylabel("Number of Moves")
    plt.show()

# ✅ Analyze multiple PGN files
pgn_files = ["game.pgn", "new_game.pgn"]
df = analyze_games(pgn_files)

# Save to CSV
df.to_csv("pgn_analysis.csv", index=False)

# Generate Game Length Graph
plot_game_lengths(df)

# Print Data for Reference
print(df)
