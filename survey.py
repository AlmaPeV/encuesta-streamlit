# -*- coding: utf-8 -*-
"""survey.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xRnGzHwo0RSkREru2GUSS3WOkh1WSxna
"""

pip install streamlit

import streamlit as st
import random

# Define a list of samples (replace with your actual samples)
samples = ["Sample 1", "Sample 2", "Sample 3", "Sample 4", "Sample 5",
           "Sample 6", "Sample 7", "Sample 8", "Sample 9", "Sample 10"]

def conduct_survey(participant_name, samples):
    remaining_samples = samples.copy()
    round_number = 1
    rounds_info = []

    while len(remaining_samples) > 1 and round_number <= 10:
        # Randomly choose two samples to compare
        sample_pair = random.sample(remaining_samples, 2)

        # Display the samples to the participant
        st.write(f"\nRound {round_number}:")
        st.write(f"1: {sample_pair[0]}")
        st.write(f"2: {sample_pair[1]}")

        # Get participant's choice
        choice = st.radio("Select the sample you like more:", options=['1', '2'], index=0, key=f"round_{round_number}")

        # Process the choice and move to next round
        if choice == '1':
            remaining_samples.remove(sample_pair[1])
            selected_sample = sample_pair[0]
        elif choice == '2':
            remaining_samples.remove(sample_pair[0])
            selected_sample = sample_pair[1]

        rounds_info.append({
            'participant': participant_name,
            'round': round_number,
            'appeared_samples': sample_pair,
            'selected_sample': selected_sample
        })

        round_number += 1
        st.button("Next Round", key=f"next_{round_number}")

    return rounds_info

# Streamlit app
st.title("Sample Preference Survey")

# Authentication section
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

password = st.text_input("Enter password to access the admin panel:", type='password')

if password == '0103':
    st.session_state.authenticated = True
    st.success("Access granted")
elif password != '':
    st.error("Invalid password")

# Survey section
participant_name = st.text_input("Enter your name or code to start the survey:", "")

if participant_name and st.button("Start Survey"):
    if 'rounds_info' not in st.session_state:
        st.session_state.rounds_info = []

    rounds_info = conduct_survey(participant_name, samples)
    st.session_state.rounds_info.extend(rounds_info)

# Admin panel
if st.session_state.authenticated:
    st.subheader("Admin Panel")
    st.write("Real-time survey results:")

    if 'rounds_info' in st.session_state:
        for info in st.session_state.rounds_info:
            st.write(f"Participant: {info['participant']}, Round {info['round']}: Appeared Samples: {info['appeared_samples']}, Selected Sample: {info['selected_sample']}")