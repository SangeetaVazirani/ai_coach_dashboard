import streamlit as st

def fitness_tracker():
    IDEAL_STEPS = 8000
    CALORIES_PER_STEP = 0.04

    steps = st.number_input("Enter the number of steps you walked today:", min_value=0)
    if st.button("Track Steps"):
        calories_burnt = steps * CALORIES_PER_STEP
        st.success(f"You burned approximately {calories_burnt:.2f} calories today.")
        if steps < IDEAL_STEPS:
            shortfall = IDEAL_STEPS - steps
            st.warning(f"You walked {shortfall} steps less than the ideal goal of {IDEAL_STEPS}.")
        else:
            st.success("Great job! You met or exceeded your step goal for the day!")