# MathCraft Streamlit App (No matplotlib dependency)
import streamlit as st
import pandas as pd
import numpy as np
import random

# Page configuration
st.set_page_config(
    page_title="MathCraft | Pizza Fraction & Division Adventures", 
    layout="centered",
    page_icon="🍕"
)

# Header branding
st.markdown("""
<div style="text-align: center; padding: 1.5rem; background: linear-gradient(90deg, #ff6b6b 0%, #ffa500 50%, #ff6b6b 100%); border-radius: 15px; margin-bottom: 2rem; box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);">
    <h1 style="color: white; margin: 0; font-weight: bold; font-size: 2.5em;">🍕 MathCraft</h1>
    <p style="color: #fff8dc; margin: 0; font-style: italic; font-size: 1.3em;">Pizza Fraction & Division Adventures</p>
    <p style="color: #ffe4b5; margin: 0; font-size: 0.9rem; margin-top: 0.5rem;">© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 🍕 Pizza Math Adventures!
Learn fractions and division the delicious way!
""")

# Audio support for instructions
st.audio("https://upload.wikimedia.org/wikipedia/commons/8/84/Example.ogg", format='audio/ogg', start_time=0)
st.caption("Audio Guide: Welcome to your Pizza Adventure!")

# Name/date input
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name:", key="student_name", placeholder="Enter your first and last name")
with col2:
    date = st.text_input("Today's Date:", key="student_date", placeholder="MM/DD/YYYY")

# Pizza Slices Control
st.markdown("---")
party_size = st.slider("🎉 How many people at the party?", 2, 16, 8)
slice_fraction = 1 / party_size
st.markdown(f"Each person gets **1/{party_size}** of the pizza, or **{slice_fraction:.3f}**.")

# Pizza Toppings Selector
st.markdown("### 🍕 Build Your Pizza!")
toppings = st.multiselect("Choose your toppings:", ["Pepperoni", "Mushrooms", "Olives", "Green Peppers", "Onions"])

# Pizza summary (visual simulation replaced with emoji feedback)
pizza_display = f"<h3 style='color: tomato;'>Your Pizza with {party_size} Slices</h3>"
if toppings:
    topping_emojis = {
        "Pepperoni": "🍕", "Mushrooms": "🍄", "Olives": "🥜",
        "Green Peppers": "🌶️", "Onions": "🧂"
    }
    emoji_string = " ".join(topping_emojis[t] for t in toppings if t in topping_emojis)
    pizza_display += f"<p style='font-size: 2em;'>{emoji_string}</p>"
else:
    pizza_display += "<p><i>No toppings selected</i></p>"
st.markdown(pizza_display, unsafe_allow_html=True)

# Practice Questions
st.markdown("---")
st.markdown("### 🔹 Practice Questions")
q1 = st.radio("If a pizza has 8 slices and 4 friends, how many slices per person?", ["2", "4", "1/2", "8"])
q2 = st.radio("What is 3/8 as a decimal?", ["0.375", "0.25", "0.5", "3.8"])
q3 = st.radio("Which is more: 1/4 or 1/6?", ["1/4", "1/6", "They are equal", "Can't say"])

# Scoring
answers = {"q1": "2", "q2": "0.375", "q3": "1/4"}
score = sum([
    q1 == answers["q1"],
    q2 == answers["q2"],
    q3 == answers["q3"]
])

if st.button("Check Answers"):
    st.markdown(f"You scored **{score}/3** correct!")
    if score == 3:
        st.balloons()

# Class Summary Table (for teacher)
st.markdown("---")
teacher_pw = st.text_input("Teacher Code:", type="password")
if teacher_pw == "pizzamath2025":
    if "class_data" not in st.session_state:
        st.session_state.class_data = []
    st.session_state.class_data.append({"Name": name, "Score": score, "Date": date})
    df = pd.DataFrame(st.session_state.class_data)
    st.dataframe(df)
    st.download_button("Download Class Scores", df.to_csv(index=False), "pizza_scores.csv", "text/csv")
