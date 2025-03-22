import streamlit as st
from web3_utils import get_all_bounties

def show():
    st.title("View Bounties 📜")
    
    bounties = get_all_bounties()
    for idx, bounty in enumerate(bounties):
        st.write(f"**Bounty {idx+1}:** {bounty['title']}")
        st.write(f"Description: {bounty['description']}")
        st.write(f"Reward: {bounty['reward']} ETH")
        st.markdown("---")