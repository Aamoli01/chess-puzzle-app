import streamlit as st
import random

# --- Chess puzzle database ---
puzzles = [
    {"fen": "r1bqkbnr/pppppppp/n7/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2", "solution": "Nc3", "rating": 1200},
    {"fen": "rnbqkbnr/pppp1ppp/8/4p3/2B5/5N2/PPPPPPPP/RNBQK2R b KQkq - 2 2", "solution": "Nc6", "rating": 1100},
    {"fen": "r1bqkbnr/pppppppp/2n5/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 2 2", "solution": "d4", "rating": 1250},
    {"fen": "r1bq1rk1/pp2nppp/2p2n2/3p4/3P4/2N1PN2/PP3PPP/R1BQ1RK1 w - - 0 9", "solution": "b3", "rating": 1350},
    {"fen": "2kr3r/p1pp1ppp/1p6/n1b1P3/8/P1N1B3/1PP2PPP/R3K2R w KQ - 0 13", "solution": "Bxc5", "rating": 1450}
]

# --- Themes and pieces for random style ---
themes = ["blue", "green", "wood", "brown", "purple", "marble"]
pieces = ["merida", "cburnett", "alpha", "pirouetti", "leipzig"]

# --- Streamlit page setup ---
st.set_page_config(page_title="♟️ Chess Puzzle", layout="centered")

st.markdown("<h1 style='text-align: center;'>♟️ Chess Puzzle Generator</h1>", unsafe_allow_html=True)

# --- "Next Puzzle" Button ---
if "puzzle_index" not in st.session_state or st.button("🔁 New Puzzle"):
    st.session_state.puzzle = random.choice(puzzles)
    st.session_state.theme = random.choice(themes)
    st.session_state.piece = random.choice(pieces)

puzzle = st.session_state.puzzle
theme = st.session_state.theme
piece = st.session_state.piece

# --- Display the board ---
fen_encoded = puzzle["fen"].replace(" ", "_")
board_url = f"https://lichess.org/api/board.png?fen={fen_encoded}&theme={theme}&piece={piece}"

st.image(board_url, caption="Current Position", use_container_width=True)

# --- Puzzle info and input ---
st.markdown(f"### 🧠 Puzzle Rating: {puzzle['rating']}")
user_move = st.text_input("📝 Your move (e.g., Nc3, d4):")

if user_move:
    if user_move.lower().strip() == puzzle["solution"].lower():
        st.success("✅ Correct! Well played!")
    else:
        st.error(f"❌ Incorrect. Best move was: `{puzzle['solution']}`")

st.markdown("---")
st.markdown("<center>Made with ❤️ by Aamoli Kumari</center>", unsafe_allow_html=True)
