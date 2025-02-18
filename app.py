import streamlit as st
import random
import pandas as pd
from datetime import datetime

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #ffffff, #f0f0f0);
        padding: 20px;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #2575fc, #6a11cb);
    }
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
    }
    .stMarkdown {
        font-size: 16px;
        color: #2c3e50;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .profile-card {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .badge-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .badge {
        display: inline-block;
        background: #6a11cb;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        margin: 5px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Session State for User Data
if "users" not in st.session_state:
    st.session_state.users = {}

# App Logo and Title
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://via.placeholder.com/100", width=100)  # Replace with your logo URL
with col2:
    st.markdown("<h1 style='color: #2c3e50;'>🌟 Mindset Mastery</h1>", unsafe_allow_html=True)

# User Input Section in Sidebar
st.sidebar.markdown("<h2 style='color: #2c3e50;'>👤 Your Profile</h2>", unsafe_allow_html=True)
name = st.sidebar.text_input("What's your name?")
goal = st.sidebar.text_input("What's your biggest learning goal?")
learning_style = st.sidebar.selectbox(
    "How do you learn best?", ["Visual", "Reading/Writing", "Hands-on", "Listening"]
)
profile_pic = st.sidebar.file_uploader("Upload a profile picture", type=["jpg", "jpeg", "png"])
bio = st.sidebar.text_area("Write a short bio about yourself")
interests = st.sidebar.text_input("What are your interests? (e.g., coding, art, science)")
email = st.sidebar.text_input("Your email (optional)")

if name:
    if name not in st.session_state.users:
        st.session_state.users[name] = {
            "effort": 5,
            "learning": 5,
            "feedback": "",
            "milestones": [],
            "badges": [],
            "mood": "😊",
            "weekly_reflection": "",
            "profile_pic": None,
            "bio": "",
            "interests": "",
            "email": "",
        }

    # Update user profile data
    st.session_state.users[name]["profile_pic"] = profile_pic
    st.session_state.users[name]["bio"] = bio
    st.session_state.users[name]["interests"] = interests
    st.session_state.users[name]["email"] = email

    # User Profile Card
    st.markdown("<div class='profile-card'><h2 style='color: white;'>👤 Your Profile</h2>", unsafe_allow_html=True)
    if st.session_state.users[name]["profile_pic"]:
        st.image(st.session_state.users[name]["profile_pic"], width=100)
    st.markdown(f"<h3 style='color: white;'>🌟 Welcome, {name}!</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Your Goal: <i>{goal}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Learning Style: <i>{learning_style}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Bio: <i>{bio}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Interests: <i>{interests}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Email: <i>{email}</i></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Daily Motivation
    st.markdown("<div class='card'><h2 style='color: #2c3e50;'>💡 Daily Motivation</h2>", unsafe_allow_html=True)
    quotes = [
        "Every small step you take brings you closer to your goal.",
        "Challenges are opportunities in disguise.",
        "Your potential is limitless—keep pushing forward.",
        "Success is a journey, not a destination.",
    ]
    st.markdown(f"<h3 style='color: #6a11cb;'>{random.choice(quotes)}</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Progress Tracker
    st.markdown("<div class='card'><h2 style='color: #2c3e50;'>📈 Track Your Progress</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.users[name]["effort"] = st.slider("How much effort are you putting in? (1-10)", 1, 10, st.session_state.users[name]["effort"])
    with col2:
        st.session_state.users[name]["learning"] = st.slider("How much are you learning? (1-10)", 1, 10, st.session_state.users[name]["learning"])
    st.markdown("</div>", unsafe_allow_html=True)

    # Mood Tracker
    st.markdown("<div class='card'><h2 style='color: #2c3e50;'>😊 How Are You Feeling Today?</h2>", unsafe_allow_html=True)
    mood = st.radio("Select your mood:", ["😊 Happy", "😄 Excited", "😐 Neutral", "😔 Sad", "😡 Angry"], horizontal=True)
    st.session_state.users[name]["mood"] = mood
    st.markdown(f"<h3 style='color: #6a11cb;'>Your mood today: {mood}</h3></div>", unsafe_allow_html=True)

    # Weekly Reflection
    st.markdown("<div class='card'><h2 style='color: #2c3e50;'>📅 Weekly Reflection</h2>", unsafe_allow_html=True)
    st.session_state.users[name]["weekly_reflection"] = st.text_area("What did you learn this week? What can you improve?", value=st.session_state.users[name]["weekly_reflection"])
    if st.button("Submit Reflection"):
        st.success("Your reflection has been saved. Great job! 🌟")
    st.markdown("</div>", unsafe_allow_html=True)

    # Learning Tips
    st.markdown("<div class='card'><h2 style='color: #2c3e50;'>🧠 Tips for Your Learning Style</h2>", unsafe_allow_html=True)
    learning_tips = {
        "Visual": ["Use diagrams and mind maps.", "Watch videos and tutorials.", "Create colorful notes."],
        "Reading/Writing": ["Read books and articles.", "Write summaries and essays.", "Use flashcards for key concepts."],
        "Hands-on": ["Engage in practical projects.", "Experiment and build things.", "Participate in workshops."],
        "Listening": ["Listen to podcasts and audiobooks.", "Record and replay lectures.", "Discuss topics with others."],
    }
    st.markdown(f"<h3 style='color: #6a11cb;'>Here are some tips for {learning_style} learners:</h3>", unsafe_allow_html=True)
    for tip in learning_tips[learning_style]:
        st.markdown(f"- {tip}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Leaderboard (Top Learners)
    st.markdown("<div class='card'><h2 style='color: #2c3e50;'>🏆 Top Learners Leaderboard</h2>", unsafe_allow_html=True)
    df = pd.DataFrame.from_dict(st.session_state.users, orient="index")
    df = df.sort_values(by=["effort", "learning"], ascending=False)
    st.table(df)
    st.markdown("</div>", unsafe_allow_html=True)

    # Progress Graph
    st.markdown("<div class='card'><h2 style='color: #2c3e50;'>📊 Learning Progress Chart</h2>", unsafe_allow_html=True)
    st.line_chart(df[["effort", "learning"]])
    st.markdown("</div>", unsafe_allow_html=True)