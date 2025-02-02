import streamlit as st
import random

# Dictionary mappings
Dict = {"r": 0, "p": 1, "s": 2}
reverse_dict = {0: "rock", 1: "paper", 2: "scissors"}

# Streamlit UI
st.title("Rock-Paper-Scissors Game")

st.write("Choose your move:")

# Vertical button layout for user choice
user_choice = None
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Rock"):
        user_choice = "r"
with col2:
    if st.button("📄 Paper"):
        user_choice = "p"
with col3:
    if st.button("✂️ Scissors"):
        user_choice = "s"

# Game logic execution after user clicks a button
if user_choice:
    computer = random.choice([0, 1, 2])
    you = Dict[user_choice]

    # Display choices
    st.write(f"**You chose:** {reverse_dict[you]}")
    st.write(f"**Computer chose:** {reverse_dict[computer]}")

    # Determine the winner
    if computer == you:
        result = "It's a Draw! 🤝"
    elif (computer == 0 and you == 1) or \
         (computer == 1 and you == 2) or \
         (computer == 2 and you == 0):
        result = "You Win! 🎉"
    else:
        result = "You Lose! 😢"

    # Display the result
    st.subheader(result)
