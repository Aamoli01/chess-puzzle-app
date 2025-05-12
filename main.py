import streamlit as st
import random
import chess
import chess.svg

# Hardcoded puzzles (FEN, best move, rating)
puzzles = [
    {
        "fen": "r1bqkbnr/pppppppp/n7/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2",
        "solution": "Nc3",
        "rating": 1200
    },
    {
        "fen": "rnbqkbnr/pppp1ppp/8/4p3/2B5/5N2/PPPPPPPP/RNBQK2R b KQkq - 2 2",
        "solution": "Nc6",
        "rating": 1100
    },
    {
        "fen": "r1bqkbnr/pppppppp/2n5/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 2 2",
        "solution": "d4",
        "rating": 1250
    }
]

# Select a random puzzle
puzzle = random.choice(puzzles)

st.title("♟️ Chess Puzzle Generator ♟️")
st.write(f"**Puzzle Rating:** {puzzle['rating']}")

# Display the chessboard
board = chess.Board(puzzle['fen'])
st.image(chess.svg.board(board=board), use_column_width=True)

# User input
user_move = st.text_input("Your move (e.g., Nc3):")

if user_move:
    if user_move.lower() == puzzle["solution"].lower():
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The best move is: {puzzle['solution']}")