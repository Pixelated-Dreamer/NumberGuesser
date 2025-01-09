import streamlit as st
import random as rd
from typing import Tuple

def check_guess(guess: int, number: int) -> Tuple[str, str]:
    """Check guess against number and return appropriate message and color."""
    if guess == number:
        return "🎉 Congratulations! You got the number!", "success"
    
    difference = abs(guess - number)
    message = ""
    
    if guess > number:
        if difference <= 5:
            message = "You are very close! But a little too high! Try again!"
        elif difference <= 15:
            message = "You are close to the answer! Just too high. Try again!"
        elif difference < 25:
            message = "You're pretty off! Too High! Try again!"
        else:
            message = "You are way off! Too high!"
    else:
        if difference <= 5:
            message = "You are very close! But a little too low! Try again!"
        elif difference <= 15:
            message = "You are close to the answer! Just too low. Try again!"
        elif difference < 25:
            message = "You're pretty off! Too Low! Try again!"
        else:
            message = "You are way off! Too low!"
            
    # Return message and color based on how close the guess is
    color = "warning" if difference <= 15 else "error"
    return message, color

def init_session_state():
    """Initialize session state variables if they don't exist."""
    if 'number' not in st.session_state:
        st.session_state.number = rd.randint(0, 100)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

def reset_game():
    """Reset the game state."""
    st.session_state.number = rd.randint(0, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Main app
st.set_page_config(page_title="Number Guessing Game", page_icon="🎲")

# Initialize session state
init_session_state()

# App title and description
st.title("🎲 Number Guessing Game")
st.markdown("""
Try to guess the number between 0 and 100! 
I'll give you hints about whether your guess is too high or too low.
""")

# Game interface
col1, col2 = st.columns([3, 1])

with col1:
    guess = st.number_input(
        "Enter your guess:",
        min_value=0,
        max_value=100,
        step=1,
        key="guess_input"
    )

with col2:
    if st.button("Make Guess"):
        st.session_state.attempts += 1
        message, color = check_guess(guess, st.session_state.number)
        
        if guess == st.session_state.number:
            st.session_state.game_over = True
            
        st.session_state.last_message = message
        st.session_state.last_color = color

# Display message if there is one
if 'last_message' in st.session_state:
    st.markdown(f"### {st.session_state.last_message}")

# Show attempts counter
st.markdown(f"**Attempts:** {st.session_state.attempts}")

# Show reset button if game is over
if st.session_state.game_over:
    if st.button("Play Again"):
        reset_game()

# Add some visual flair at the bottom
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
