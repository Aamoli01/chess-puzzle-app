import streamlit as st
import random

# Hardcoded puzzles
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

# Select puzzle
puzzle = random.choice(puzzles)

# Build Lichess board image URL
fen_encoded = puzzle["fen"].replace(" ", "_")
board_url = f"https://lichess.org/api/board.png?fen={fen_encoded}&theme=blue&piece=merida"

# Streamlit UI
st.set_page_config(page_title="♟️ Chess Puzzle", layout="centered")

st.markdown("<h1 style='text-align: center;'>♟️ Chess Puzzle Generator</h1>", unsafe_allow_html=True)
st.image(board_url, caption="Current Position", use_column_width=True)

st.markdown(f"### 🧠 Puzzle Rating: {puzzle['rating']}")
user_move = st.text_input("📝 Your move (like Nc3, d4, etc.):", "")

if user_move:
    if user_move.lower().strip() == puzzle["solution"].lower():
        st.success("✅ Correct! Well played!")
    else:
        st.error(f"❌ Nope! The correct move is: `{puzzle['solution']}`")

st.markdown("---")
st.markdown("Made with ❤️ by Aamoli Kumari", unsafe_allow_html=True)
