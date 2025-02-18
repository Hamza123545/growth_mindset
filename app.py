## Growth Mindset Challenge Web App
# Tech Stack: Streamlit, UV, Pandas
# Features: User Profile, Daily Motivation, Progress Tracker, Mood Tracker, Weekly Reflection, Learning Tips, Leaderboard, Learning Progress Chart

import streamlit as st
import random
import pandas as pd
from datetime import datetime

# Global Styles
st.set_page_config(page_title='Growth Mindset Challenge', layout='wide')
st.markdown("<style>body {background-color: #f0f2f6;}</style>", unsafe_allow_html=True)

# Initializing Session State
if 'users' not in st.session_state:
    st.session_state.users = {}

# Sidebar - User Profile
st.sidebar.title("👤 Your Profile")
name = st.sidebar.text_input("What's your name?")
goal = st.sidebar.text_input("What's your biggest learning goal?")
learning_style = st.sidebar.selectbox(
    "How do you learn best?", ["Visual", "Reading/Writing", "Hands-on", "Listening"]
)

# Registering New User
if name:
    if name not in st.session_state.users:
        st.session_state.users[name] = {
            "effort": 5,
            "learning": 5,
            "mood": "😊",
            "weekly_reflection": "",
            "badges": [],
            "milestones": [],
        }

# Main Layout
st.title("🌟 Growth Mindset Challenge")
st.markdown("Welcome to the Growth Mindset Challenge! Track your progress, stay motivated, and grow every day.")

if name:
    # User Profile
    st.subheader(f"Welcome, {name}!")
    st.write(f"Your Goal: {goal}")
    st.write(f"Learning Style: {learning_style}")

    # Daily Motivation
    st.subheader("💡 Daily Motivation")
    quotes = [
        "Every small step brings you closer to your goal.",
        "Challenges are opportunities in disguise.",
        "Your potential is limitless—keep pushing forward.",
        "Success is a journey, not a destination."
    ]
    st.success(random.choice(quotes))

    # Progress Tracker
    st.subheader("📈 Track Your Progress")
    st.session_state.users[name]["effort"] = st.slider("Effort Level (1-10)", 1, 10, st.session_state.users[name]["effort"])
    st.session_state.users[name]["learning"] = st.slider("Learning Level (1-10)", 1, 10, st.session_state.users[name]["learning"])

    # Mood Tracker
    st.subheader("😊 How Are You Feeling Today?")
    st.session_state.users[name]["mood"] = st.radio(
        "Your Mood:", ["😊 Happy", "😄 Excited", "😐 Neutral", "😔 Sad", "😡 Angry"],
        horizontal=True
    )

    # Weekly Reflection
    st.subheader("📅 Weekly Reflection")
    st.session_state.users[name]["weekly_reflection"] = st.text_area(
        "What did you learn this week? What can you improve?",
        value=st.session_state.users[name]["weekly_reflection"]
    )
    if st.button("Submit Reflection"):
        st.success("Your reflection has been saved. Great job! 🌟")

    # Leaderboard
    st.subheader("🏆 Top Learners Leaderboard")
    df = pd.DataFrame.from_dict(st.session_state.users, orient="index")
    df = df.sort_values(by=["effort", "learning"], ascending=False)
    st.table(df)

    # Progress Graph
    st.subheader("📊 Learning Progress Chart")
    st.line_chart(df[["effort", "learning"]])
