import chess.pgn
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def extract_centipawn_loss(comment):
    """Extract centipawn loss from PGN comments."""
    match = re.search(r"\[%eval\s([+-]?\d+\.\d+)\]", comment)
    if match:
        return float(match.group(1)) * 100  # Convert to centipawns (1 pawn = 100 centipawns)
    return None

def parse_pgn(file_path):
    """Parses PGN and extracts move numbers and evaluations."""
    with open(file_path) as pgn:
        game = chess.pgn.read_game(pgn)
        board = game.board()
        moves = []
        centipawn_losses = []
        
        node = game
        move_number = 1
        
        while node.variations:
            node = node.variations[0]
            comment = node.comment
            centipawn_loss = extract_centipawn_loss(comment)
            
            moves.append(move_number)
            centipawn_losses.append(centipawn_loss if centipawn_loss is not None else 0)
            
            board.push(node.move)
            move_number += 1

    return pd.DataFrame({"Move Number": moves, "Centipawn Loss": centipawn_losses})

def plot_centipawn_loss(df, title):
    """Plot centipawn loss across moves."""
    plt.figure(figsize=(10,5))
    sns.lineplot(x="Move Number", y="Centipawn Loss", data=df, marker="o", linestyle="-")
    plt.axhline(y=0, color='r', linestyle='--', label="Perfect Move (0 cp loss)")
    plt.title(title)
    plt.xlabel("Move Number")
    plt.ylabel("Centipawn Loss")
    plt.legend()
    plt.show()

# ✅ Analyze and plot CPL for multiple PGN files
pgn_files = ["a.pgn", "annotated_game2.pgn"]
for file in pgn_files:
    print(f"\n📂 Analyzing PGN File: {file}")
    df = parse_pgn(file)
    
    # Save to CSV
    df.to_csv(f"{file}_cpl_analysis.csv", index=False)
    
    # Generate Centipawn Loss Graph
    plot_centipawn_loss(df, f"Centipawn Loss for {file}")
