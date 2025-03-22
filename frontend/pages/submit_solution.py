import streamlit as st
from web3_utils import submit_solution

def show():
    st.title("Submit a Solution ✍️")
    
    bounty_id = st.number_input("Bounty ID", min_value=0, step=1)
    solution_text = st.text_area("Enter your solution:")
    if st.button("Submit Solution"):
        if solution_text:
            tx_hash = submit_solution(bounty_id, solution_text)
            st.success(f"Solution submitted! Transaction Hash: {tx_hash}")
        else:
            st.error("Please enter a solution before submitting.")