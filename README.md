# Chess Cheat Detection: Analyzing PGN Files

An automated framework for detecting potential cheating in chess games through statistical analysis of Portable Game Notation (PGN) files, developed as part of an MTech dissertation in AI & ML at BITS Pilani.

## Project Overview

This project addresses the growing concern of chess cheating in online platforms by analyzing gameplay patterns using centipawn loss (CPL) metrics and machine learning techniques. The system identifies statistical anomalies that may indicate computer assistance during gameplay.

## Key Features

- **PGN File Analysis**: Parse and analyze chess games in standard PGN format
- **Centipawn Loss Calculation**: Evaluate move quality against optimal engine recommendations
- **Statistical Pattern Detection**: Identify suspicious gameplay patterns and anomalies
- **Data Visualization**: Generate comprehensive graphs and charts for pattern analysis
- **Machine Learning Classification**: 95% accuracy achieved using Neural Network models
- **Multi-factor Analysis**: Consider game length, move timing, and contextual factors

## Technologies Used

- **Python 3.x**
- **Chess Libraries**: `python-chess`, `chess.pgn`
- **Engine Analysis**: Stockfish 16 (depth 20)
- **Data Processing**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`
- **Machine Learning**: `scikit-learn`, `tensorflow`

## Detection Methodology

### Primary Indicators
- Consistently low CPL across complex positions
- Unnatural CPL stability throughout games
- High alignment with top engine choices in critical positions
- Performance incongruent with player rating

### Secondary Indicators
- Unusual game length patterns
- Inconsistent time usage patterns
- Performance spikes in specific periods
- Drastic improvement without corresponding rating increase

### Classification Confidence Levels
- **Low Confidence**: Only secondary indicators present
- **Medium Confidence**: One primary + multiple secondary indicators
- **High Confidence**: Multiple primary indicators present

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/0xafraidoftime/Chess-Cheat-Detection.git
cd Chess-Cheat-Detection
```

2. **Install required dependencies**
```bash
pip install python-chess pandas matplotlib seaborn scikit-learn tensorflow stockfish
```

3. **Download Stockfish Engine**
- Download Stockfish 16 from [official website](https://stockfishchess.org/)
- Ensure it's accessible in your system PATH

## Project Structure

```
chess-cheat-detection/
├── chess_engine.py          # Basic PGN parsing functionality
├── chess_engine2.py         # Enhanced analysis with CPL extraction
├── CPL plot.py             # Visualization and plotting utilities
├── engine3.py              # Additional analysis features
├── game length distribution.py  # Game length analysis
├── data/
│   ├── a.pgn               # Sample PGN files
│   ├── game.pgn
│   ├── new_game.pgn
│   └── annotated_game2.pgn
├── analysis/
│   ├── *.csv               # Generated analysis results
│   └── pgn_analysis.csv    # Summary statistics
└── README.md
```

## Usage

### Basic PGN Analysis
```python
from chess_engine import parse_pgn

# Parse a PGN file
moves = parse_pgn("your_game.pgn")
print("Extracted moves:", moves)
```

### Centipawn Loss Analysis
```python
# Run CPL analysis and generate visualizations
python "CPL plot.py"
```

### Game Length Distribution
```python
# Analyze game length patterns
python "game length distribution.py"
```

### Cheat Detection
```python
from chess_engine2 import analyze_game

# Analyze a game for potential cheating
analyze_game("suspicious_game.pgn")
```

## Performance Metrics

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|-----------|----------|-----------|---------|----------|
| Decision Tree | 85% | 88% | 83% | 85% |
| Random Forest | 92% | 90% | 93% | 91% |
| **Neural Network** | **95%** | **94%** | **96%** | **95%** |

## Key Findings

- **CPL Analysis**: Effectively differentiates fair from engine-assisted play
- **Game Context**: Complexity, phase, and time control are crucial for accurate detection
- **Multi-factorial Approach**: Reduces false positives significantly
- **Pattern Recognition**: Identifies bimodal distribution in game lengths for suspicious accounts

## Limitations

- Requires annotated PGN files or Stockfish integration for evaluation
- May not detect sophisticated cheating (intentional suboptimal moves)
- Dataset size impacts ML model accuracy
- Computational intensity for real-time analysis
- Potential false positives with very strong human players

## Future Enhancements

### Technical Improvements
- Real-time analysis capability for tournament monitoring
- Cloud-based implementation for scalability
- Mobile application for arbiters and tournament directors
- Integration with chess platform APIs

### Research Extensions
- Advanced neural network architectures (LSTM, Transformer)
- Incorporation of psychological factors and playing style analysis
- Application to other strategic games (Go, Shogi)
- Self-improving detection through continuous learning

## Research Background

This project was developed as part of an MTech dissertation in AI & ML at BITS Pilani under the supervision of Milin Shah (VP & Technology Manager, Bank of America). The research addresses the increasing prevalence of chess cheating in online environments, particularly since 2020.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests to improve the detection algorithms and expand the project's capabilities.

## Citation

If you use this work in your research, please cite:
```
Pal, A. (2025). Cheat Detection in Chess: Analyzing PGN Files. 
MTech Dissertation, BITS Pilani. Supervisor: Milin Shah.
```

## License

This project is open-source and available under the MIT License. See LICENSE file for details.

## Acknowledgments

- **Supervisor**: Milin Shah, Bank of America
- **Institution**: BITS Pilani Department of AI & ML
- **Chess Community Contributors**: Manan Pahwa (Purdue University), Moin Memon (Bank of America)
- **Technical Support**: Stockfish Development Team, Python-chess Library Contributors
- **Data Sources**: Chess.com Research Dataset, Lichess Open Database

## Contact

**Ankita Pal**  
BITS ID: 2022AC05327  
Email: 2022AC05327@wilp.bits-pilani.ac.in  

---

*This project aims to maintain competitive integrity in chess while providing transparent, objective methods for cheat detection that can assist tournament arbiters and online platforms.*

