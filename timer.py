import streamlit as st
import time

def countdown_timer(seconds):
    """Display a countdown timer for the given number of seconds."""
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        st.write(f"⏳ Time remaining: {time_format}")
        time.sleep(1)
        seconds -= 1

    st.write("🚀 Time's up!")

# Set up Streamlit app
st.title("Countdown Timer")

# Input for timer duration in seconds
seconds_input = st.number_input("Enter countdown time in seconds", min_value=1, value=10, step=1)

if st.button("Start Countdown"):
    countdown_timer(seconds_input)
