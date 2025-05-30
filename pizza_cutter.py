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

# Error Handling Info Box
st.markdown("""
### ⚠️ Component Load Errors
If you see `TypeError: Failed to fetch dynamically imported module`, it means that your browser or the Streamlit environment couldn't fetch a JavaScript module required by a custom component. 

This often happens when:
- A custom Streamlit component uses external JS with `import()` statements.
- The app is referencing a module not bundled properly.

### Fix Options:
- Inline all JS and CSS used in your `st.components.v1.html()` content.
- Avoid referencing paths like `/_+/static/js/...`
- Consider deploying external modules as fully bundled apps and using an iframe instead.

**Recommendation:** Refactor broken JS dependencies to inline HTML/JS or a bundled component.
""")

# Simple Calculator for Backup
st.markdown("---")
st.markdown("### 🧩 Quick Pizza Share Calculator")

col1, col2, col3 = st.columns(3)
with col1:
    pizzas = st.number_input("Number of Pizzas", min_value=1, max_value=10, value=2)
with col2:
    slices_per_pizza = st.number_input("Slices per Pizza", min_value=1, max_value=16, value=8)
with col3:
    people = st.number_input("People Sharing", min_value=1, max_value=50, value=12)

if people:
    total_slices = pizzas * slices_per_pizza
    slices_each = total_slices / people
    fraction_each = slices_each / slices_per_pizza
    percent_each = fraction_each * 100

    st.markdown(f"""
    **Results:**
    - 🔢 Total slices: **{total_slices}**
    - 📊 Per person: **{slices_each:.2f} slices**
    - 📊 Fraction of pizza: **{fraction_each:.3f}**
    - 📊 Percentage: **{percent_each:.1f}%**
    """)

# Final score evaluation logic (without auto-triggered balloons)
correct_answers = {
    "Q1": "1/6 of the pizza",
    "Q2": "1 ÷ 8", 
    "Q3": "1/10 of the pizza",
    "Q4": "1/4 (bigger slices)",
    "Q5": "3 ÷ 8",
    "Q6": "2/12 of the pizza"
}

submitted = st.button("🎯 Check My Pizza Powers!", type="primary")

if submitted:
    responses = st.session_state.get("responses", {})
    score = sum(1 for key, correct in correct_answers.items() if responses.get(key) == correct)
    if responses.get("Problem_Answer") == responses.get("Problem_Choice"):
        score += 1

    total_questions = 7
    st.markdown(f"### 📊 Your Pizza Score: {score}/{total_questions} ({(score/total_questions)*100:.0f}%)")

    if score == total_questions:
        st.success("🌟 PIZZA MASTER! You've conquered fractions and division! 🍕👑")
        st.balloons()
    elif score >= 6:
        st.success("🎯 AWESOME! You're a Pizza Math Expert! Just review the ones you missed!")
    elif score >= 4:
        st.info("👍 GOOD JOB! You're getting the hang of pizza math! Keep practicing!")
    else:
        st.warning("📚 Keep exploring! Use the pizza wheel to help you understand fractions better!")

st.markdown("""
<div style="margin-top: 50px; padding: 20px; border-radius: 10px; background: #fff0f0; color: #990000;">
<b>Note:</b> This page had JavaScript loading issues. The calculator above is provided as a fallback.
</div>
""", unsafe_allow_html=True)

# Final Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 10px; color: #666; font-size: 0.9em;">
<p>Created with ❤️ by Xavier Honablue M.Ed | Pizza Math Adventures</p>
<p>Use math to make every pizza party fair and fun!</p>
</div>
""", unsafe_allow_html=True)
