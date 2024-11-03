import streamlit as st
import random
import pygame

# Initialize pygame for sound effects
pygame.mixer.init()

# Load sound effects (make sure the file paths are correct)
correct_sound = pygame.mixer.Sound("success.wav")
wrong_sound = pygame.mixer.Sound("wrong.wav")


# Portfolio Section
st.title(" Portfolio")
st.image("kutty.jpeg",width=200)
st.subheader("Personal Information")
st.write("Name:Boomika S N")
st.write("Age:18")
st.write("Department:Btech Computer Science with Business Systems")
st.write("College:KGiSL Institute of Technology")
st.write("Hobbies:Reading Books,Playing Badmiton,Painting,Yoga,Gardening")

st.subheader("Skills")
st.write("Python Programming")
st.write("Baking")
st.write("Digital Art")
st.write("Video Editing ")
st.write("Martial Art")
# LinkedIn and GitHub links
st.markdown(
    """
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/boomika-sn-06b58b336/)  
    [![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/BoomikaSN)
    """,
    unsafe_allow_html=True
)
import streamlit as st
import random
import pygame

# Initialize pygame for sound effects
pygame.mixer.init()

# Load sound effects (make sure the file paths are correct)
correct_sound = pygame.mixer.Sound("success.wav")
wrong_sound = pygame.mixer.Sound("wrong.wav")

# Title of the App
st.title("Guessing Game 🎉")

# Game Mode Selection
game_mode = st.selectbox("Choose a game mode:", ["User Guessing", "Machine Guessing"])

if game_mode == "User Guessing":
    # User Guessing Mode
    st.write("## 🎲 User Guessing Mode")
    st.write("I'm thinking of a number between 1 and 100. Can you guess what it is? 🎉")

    # Initialize game state for User Guessing Mode
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)  # Randomly choose a number between 1 and 100
    if "user_attempts" not in st.session_state:
        st.session_state.user_attempts = 0  # Initialize attempts counter

    # Take user input for their guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="user_guess")

    # Check if the user's guess is correct
    if st.button("Submit Guess"):
        st.session_state.user_attempts += 1  # Increment attempts counter

        # Give feedback based on the guess
        if guess < st.session_state.secret_number:
            wrong_sound.play()
            st.write("Oops! Too low. Try again! 🎯")
        elif guess > st.session_state.secret_number:
            wrong_sound.play()
            st.write("Oops! Too high. Try again! 🎯")
        else:
            correct_sound.play()
            st.write(f"🎉 Yay! You guessed it right in {st.session_state.user_attempts} tries! 🎈")
            st.image("congrats.jpeg")
            # Reset the game for a new round
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.user_attempts = 0

elif game_mode == "Machine Guessing":
    # Machine Guessing Mode
    st.write("## 🎲 Machine Guessing Mode")
    st.write("Think of a number between 1 and 100, and I'll try to guess it! Give me clues so I can get it right. 🎉")

    # Set initial values for Machine Guessing Mode
    if "low" not in st.session_state:
        st.session_state.low = 1
    if "high" not in st.session_state:
        st.session_state.high = 100
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    if "machine_guess" not in st.session_state:
        st.session_state.machine_guess = (st.session_state.low + st.session_state.high) // 2

    # Display the machine's current guess
    st.write(f"My guess is: {st.session_state.machine_guess}")

    # User feedback for machine's guess
    response = st.selectbox("Tell me:", ["Too Low", "Too High", "Correct"], key="response")

    if st.button("Submit Feedback"):
        st.session_state.attempts += 1  # Count the number of attempts

        # Adjust the guess based on user feedback
        if response == "Too Low":
            st.session_state.low = st.session_state.machine_guess + 1
        elif response == "Too High":
            st.session_state.high = st.session_state.machine_guess - 1
        else:
            correct_sound.play()
            st.write(f"🎉 Hooray! I guessed your number in {st.session_state.attempts} tries! 🎈")
            st.image("congrats.jpeg")
            st.balloons()
            
            # Reset for a new game
            st.session_state.low = 1
            st.session_state.high = 100
            st.session_state.attempts = 0
            st.session_state.machine_guess = (st.session_state.low + st.session_state.high) // 2
            st.stop()

        # Update the machine's guess for the next round
        st.session_state.machine_guess = (st.session_state.low + st.session_state.high) // 2

# Fun footer
st.write("---")
st.write("Thank you for playing!!! 🌈")