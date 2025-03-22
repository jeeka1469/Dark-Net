import streamlit as st
from pages import home, submit_solution, view_bounties

st.set_page_config(page_title="Darkchain", layout="wide")

PAGES = {
    "🏠 Home": home,
    "📤 Submit Solution": submit_solution,
    "📜 View Bounties": view_bounties
}

st.sidebar.title("Darkchain Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

PAGES[selection].show()