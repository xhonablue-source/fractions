import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="MathCraft | Pizza Fraction Adventures", 
    layout="centered",
    page_icon="🍕"
)

# Header with branding
st.markdown("""
<div style="text-align: center; padding: 1.5rem; background: linear-gradient(90deg, #ff6b6b 0%, #ffa500 50%, #ff6b6b 100%); border-radius: 15px; margin-bottom: 2rem; box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);">
    <h1 style="color: white; margin: 0; font-weight: bold; font-size: 2.5em;">🍕 MathCraft</h1>
    <p style="color: #fff8dc; margin: 0; font-style: italic; font-size: 1.3em;">Pizza Fraction & Division Adventures</p>
    <p style="color: #ffe4b5; margin: 0; font-size: 0.9rem; margin-top: 0.5rem;">© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 style='text-align: center; color: #ff6b6b; font-size: 2.2em;'>🍕 Pizza Math Adventures!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666; font-style: italic;'>Learn fractions and division the delicious way!</h3>", unsafe_allow_html=True)

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# Student Information
st.markdown("---")
st.markdown("### 👨‍🎓 Student Information")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name:", key="student_name", placeholder="Enter your first and last name")
with col2:
    date = st.text_input("Today's Date:", key="student_date", placeholder="MM/DD/YYYY")

st.session_state.responses.update({"Name": name, "Date": date})

# Learning Standards
st.markdown("---")
st.markdown("### 📚 Learning Standards - Grade 5")
with st.expander("🎯 Click to see what we're learning today!"):
    st.markdown("""
    **5.NF.1** - Add and subtract fractions with unlike denominators
    *🍕 Applied through: Understanding pizza slices as fractions (1/8, 1/4, etc.)*

    **5.NF.2** - Solve word problems involving addition and subtraction of fractions
    *🍕 Applied through: Real pizza sharing scenarios and fraction combinations*

    **5.NF.3** - Interpret a fraction as division of the numerator by the denominator
    *🍕 Applied through: Understanding that 3/8 means 3 ÷ 8*
    """)

# Learning Objective
st.markdown("---")
st.markdown("""
### 🎯 Today's Pizza Mission!

**Your Mission:** Become a Pizza Math Expert! You'll learn to:
- 🍕 Cut pizzas into equal parts (fractions!)
- 🧮 Understand what fractions really mean
- ➖ See how division and fractions are best friends
- 🎮 Use our amazing Pizza Wheel to explore math

**Big Secret:** Math is everywhere - especially in pizza! 😫
""")

# Section: Practice Questions
st.markdown("---")
st.markdown("### 🎮 Section: Practice Questions")

questions = {
    "Q1": ("If a pizza is cut into 6 equal slices, each slice is:", "1/6 of the pizza"),
    "Q2": ("What does 1/8 mean as division?", "1 ÷ 8"),
    "Q3": ("If 10 people share 1 pizza equally, each gets:", "1/10 of the pizza"),
    "Q4": ("Which is bigger: 1/4 or 1/8?", "1/4 (bigger slices)"),
    "Q5": ("3/8 as a division problem is:", "3 ÷ 8"),
    "Q6": ("If you eat 2 slices of a pizza cut into 12 pieces, you ate:", "2/12 of the pizza")
}

for key, (qtext, correct_answer) in questions.items():
    answer = st.selectbox(qtext, ["", correct_answer, "Wrong option 1", "Wrong option 2"], key=key)
    st.session_state.responses[key] = answer
    if answer and answer == correct_answer:
        st.success("🌟 Correct!")
    elif answer:
        st.error("❌ Try again!")

# Final Check Button
st.markdown("---")
st.markdown("### ✅ Check Your Pizza Powers!")
correct_answers = {k: v[1] for k, v in questions.items()}

if st.button("🎯 Check My Pizza Powers!", type="primary"):
    score = 0
    for q, correct in correct_answers.items():
        if st.session_state.responses.get(q) == correct:
            score += 1

    total = len(correct_answers)
    st.markdown(f"### 📊 Your Score: {score}/{total} ({(score/total)*100:.0f}%)")

    if score == total:
        st.success("🌟 PIZZA MASTER! You've mastered every slice of math!")
        st.balloons()
    elif score >= 4:
        st.info("👍 Great job! Just a few more to become a master!")
    else:
        st.warning("📈 Keep practicing and use pizza as your guide!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 10px; color: #666; font-size: 0.9em;">
<p>Created with ❤️ by Xavier Honablue M.Ed | Pizza Math Adventures</p>
<p>Use math to make every pizza party fair and fun!</p>
</div>
""", unsafe_allow_html=True)
