import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Birthday Party Challenge - Math Visualizer", 
    layout="centered",
    page_icon="🎂"
)

st.title("🎂 The Birthday Party Challenge")
st.markdown("### Interactive Math Visualizer")

# Problem Statement
st.markdown("""
### 🎉 The Problem:
**Sarah is having a birthday party! She ordered 2 large pizzas for 12 friends. 
If they cut each pizza into 8 equal slices, how much pizza does each friend get?**
""")

st.markdown("---")

# Step-by-step breakdown
st.markdown("### 🧮 Let's Solve This Step by Step!")

# Given information
st.markdown("""
#### 📋 What We Know:
- **🍕 Number of pizzas:** 2
- **👥 Number of friends:** 12  
- **✂️ Slices per pizza:** 8
- **❓ Question:** How much pizza does each friend get?
""")

# Visual calculation
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### 🔢 Step 1: Total Slices
    **2 pizzas × 8 slices = 16 total slices**
    """)

with col2:
    st.markdown("""
    #### ➗ Step 2: Division
    **16 slices ÷ 12 friends = ? slices per friend**
    """)

# Show the math
st.markdown(f"""
### 🎯 The Math:

<div style="background: linear-gradient(135deg, #3498db, #2980b9); color: white; padding: 25px; border-radius: 15px; text-align: center; margin: 20px 0; box-shadow: 0 8px 20px rgba(52, 152, 219, 0.3);">
<h2 style="margin: 0;">16 ÷ 12 = 16/12 = 4/3 ≈ 1.333 slices per friend</h2>
<p style="margin: 10px 0; font-size: 1.2em;">Each friend gets <strong>1⅓ slices</strong> (1 whole slice + ⅓ of another slice)</p>
</div>
""", unsafe_allow_html=True)

# Interactive Visualizer
st.markdown("### 🍕 Visual Pizza Distribution")

# The Birthday Party Visualizer
party_visualizer_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(135deg, #ff6b6b, #ffa500);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .party-container {{
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            max-width: 1000px;
            width: 100%;
            text-align: center;
        }}

        .party-title {{
            font-size: 2.5em;
            color: #e74c3c;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }}

        .pizza-row {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 30px 0;
            gap: 50px;
            flex-wrap: wrap;
        }}

        .pizza-container {{
            text-align: center;
        }}

        .pizza-label {{
            font-size: 1.3em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        }}

        .math-explanation {{
            background: linear-gradient(135deg, #00b894, #00a085);
            color: white;
            padding: 25px;
            border-radius: 15px;
            margin: 25px 0;
            font-size: 1.3em;
            box-shadow: 0 8px 20px rgba(0, 184, 148, 0.3);
        }}

        .friend-distribution {{
            background: linear-gradient(135deg, #fd79a8, #e84393);
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            font-size: 1.2em;
        }}

        .result-box {{
            background: linear-gradient(135deg, #fdcb6e, #e17055);
            color: white;
            padding: 25px;
            border-radius: 15px;
            margin: 25px 0;
            font-size: 1.4em;
            box-shadow: 0 8px 20px rgba(253, 203, 110, 0.3);
        }}

        .slice {{
            fill: #f1c40f;
            stroke: #f39c12;
            stroke-width: 2;
            opacity: 0.8;
        }}

        .slice-line {{
            stroke: #2c3e50;
            stroke-width: 3;
            stroke-linecap: round;
        }}

        .slice-number {{
            font-family: Arial, sans-serif;
            font-size: 14px;
            font-weight: bold;
            fill: #2c3e50;
        }}

        .friends-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
            gap: 15px;
            margin: 20px 0;
            max-width: 800px;
        }}

        .friend-card {{
            background: linear-gradient(135deg, #74b9ff, #0984e3);
            color: white;
            padding: 15px 10px;
            border-radius: 10px;
            font-size: 0.9em;
            font-weight: bold;
            box-shadow: 0 4px 12px rgba(116, 185, 255, 0.3);
        }}
    </style>
</head>
<body>
    <div class="party-container">
        <h1 class="party-title">🎂 Sarah's Birthday Party! 🎉</h1>
        
        <div class="math-explanation">
            <strong>📊 The Setup:</strong><br>
            • 2 pizzas × 8 slices each = <strong>16 total slices</strong><br>
            • 12 friends need to share equally<br>
            • 16 ÷ 12 = <strong>1.333... slices per friend</strong>
        </div>

        <div class="pizza-row">
            <div class="pizza-container">
                <div class="pizza-label">🍕 Pizza #1 (8 slices)</div>
                <svg width="250" height="250" id="pizza1">
                    <circle cx="125" cy="125" r="110" fill="#D2691E" stroke="#8B4513" stroke-width="4"/>
                    <circle cx="125" cy="125" r="105" fill="#FFD700" opacity="0.3"/>
                </svg>
            </div>
            
            <div style="font-size: 2em; color: #e74c3c; font-weight: bold;">+</div>
            
            <div class="pizza-container">
                <div class="pizza-label">🍕 Pizza #2 (8 slices)</div>
                <svg width="250" height="250" id="pizza2">
                    <circle cx="125" cy="125" r="110" fill="#D2691E" stroke="#8B4513" stroke-width="4"/>
                    <circle cx="125" cy="125" r="105" fill="#FFD700" opacity="0.3"/>
                </svg>
            </div>
        </div>

        <div class="result-box">
            <strong>🎯 Total Available:</strong> 16 slices from 2 pizzas<br>
            <strong>👥 To Share Among:</strong> 12 friends<br>
            <strong>🧮 Calculation:</strong> 16 ÷ 12 = 16/12 = 4/3 = 1⅓ slices each
        </div>

        <div class="friend-distribution">
            <strong>👥 How It Works Out:</strong><br>
            Each friend gets <strong>1 whole slice + ⅓ of another slice</strong><br>
            <em>(Some friends get 1 slice, others get 2 slices, but it averages to 1⅓ each)</em>
        </div>

        <div class="friends-grid" id="friendsGrid">
            <!-- Friends will be populated by JavaScript -->
        </div>

        <div style="background: linear-gradient(45deg, #6c5ce7, #a29bfe); color: white; padding: 20px; border-radius: 15px; margin-top: 25px;">
            <strong>✨ The Answer:</strong> Each friend gets <strong>4/3 slices</strong> or <strong>1⅓ slices</strong> or <strong>1.333... slices</strong><br>
            <em>In practice: 4 friends get 2 slices each, 8 friends get 1 slice each</em>
        </div>
    </div>

    <script>
        function drawPizza(svgId, slicesPerPizza) {{
            const svg = document.getElementById(svgId);
            const centerX = 125;
            const centerY = 125;
            const radius = 105;
            
            // Draw slices
            const angleStep = (2 * Math.PI) / slicesPerPizza;
            
            for (let i = 0; i < slicesPerPizza; i++) {{
                const startAngle = i * angleStep - Math.PI/2;
                const endAngle = (i + 1) * angleStep - Math.PI/2;
                
                // Calculate slice path
                const x1 = centerX + radius * Math.cos(startAngle);
                const y1 = centerY + radius * Math.sin(startAngle);
                const x2 = centerX + radius * Math.cos(endAngle);
                const y2 = centerY + radius * Math.sin(endAngle);
                
                // Create slice
                const slice = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                const pathData = [
                    `M ${{centerX}} ${{centerY}}`,
                    `L ${{x1}} ${{y1}}`,
                    `A ${{radius}} ${{radius}} 0 0 1 ${{x2}} ${{y2}}`,
                    'Z'
                ].join(' ');
                
                slice.setAttribute('d', pathData);
                slice.setAttribute('class', 'slice');
                svg.appendChild(slice);
                
                // Draw slice line
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', centerX);
                line.setAttribute('y1', centerY);
                line.setAttribute('x2', x1);
                line.setAttribute('y2', y1);
                line.setAttribute('class', 'slice-line');
                svg.appendChild(line);
                
                // Add slice number
                const textAngle = (startAngle + endAngle) / 2;
                const textRadius = radius * 0.7;
                const textX = centerX + textRadius * Math.cos(textAngle);
                const textY = centerY + textRadius * Math.sin(textAngle);
                
                const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                text.setAttribute('x', textX);
                text.setAttribute('y', textY);
                text.setAttribute('text-anchor', 'middle');
                text.setAttribute('dominant-baseline', 'middle');
                text.setAttribute('class', 'slice-number');
                text.textContent = i + 1;
                svg.appendChild(text);
            }}
        }}

        function createFriendsDisplay() {{
            const friendsGrid = document.getElementById('friendsGrid');
            const totalSlices = 16;
            const numFriends = 12;
            
            // Calculate distribution: some friends get 1 slice, some get 2
            const slicesPerFriend = totalSlices / numFriends; // 1.333...
            const friendsWithTwoSlices = totalSlices % numFriends; // 4 friends
            const friendsWithOneSlice = numFriends - friendsWithTwoSlices; // 8 friends
            
            for (let i = 1; i <= numFriends; i++) {{
                const friendCard = document.createElement('div');
                friendCard.className = 'friend-card';
                
                const slicesForThisFriend = i <= friendsWithTwoSlices ? 2 : 1;
                
                friendCard.innerHTML = `
                    <div>Friend ${{i}}</div>
                    <div>${{slicesForThisFriend}} slice${{slicesForThisFriend > 1 ? 's' : ''}}</div>
                `;
                
                friendsGrid.appendChild(friendCard);
            }}
        }}

        // Initialize the visualization
        drawPizza('pizza1', 8);
        drawPizza('pizza2', 8);
        createFriendsDisplay();
    </script>
</body>
</html>
"""

# Display the visualizer
st.components.v1.html(party_visualizer_html, height=1000)

# Step-by-step explanation
st.markdown("---")
st.markdown("### 🎓 Mathematical Explanation")

tab1, tab2, tab3 = st.tabs(["📊 The Math", "🍕 Practical Solution", "🧠 Key Concepts"])

with tab1:
    st.markdown("""
    #### 🔢 Step-by-Step Calculation:
    
    1. **Total slices available:**
       - Pizza 1: 8 slices
       - Pizza 2: 8 slices  
       - **Total: 8 + 8 = 16 slices**
    
    2. **Division calculation:**
       - 16 slices ÷ 12 friends = 16/12
       - Simplify: 16/12 = 4/3 (divide both by 4)
       - As decimal: 4 ÷ 3 = 1.333...
       - As mixed number: 1⅓ slices
    
    3. **What this means:**
       - Each friend gets 1 whole slice + ⅓ of another slice
       - In decimal form: 1.333... slices per person
    """)

with tab2:
    st.markdown("""
    #### 🍕 How Sarah Actually Shares the Pizza:
    
    **The Reality Check:**
    - You can't give someone exactly ⅓ of a slice in practice!
    - **Smart solution:** Some friends get more, some get less, but it averages out
    
    **Practical Distribution:**
    - **4 friends** get **2 slices each** = 8 slices
    - **8 friends** get **1 slice each** = 8 slices
    - **Total used:** 8 + 8 = 16 slices ✓
    
    **The Math Still Works:**
    - (4 × 2) + (8 × 1) = 8 + 8 = 16 slices total
    - 16 slices ÷ 12 friends = 1.333... average per friend ✓
    """)

with tab3:
    st.markdown("""
    #### 🧠 Important Mathematical Concepts:
    
    **🎯 Division with Remainders:**
    - When 16 ÷ 12, we get 1 remainder 4
    - This means 1 slice per person, with 4 slices left over
    - Those 4 extra slices can be shared among 4 friends
    
    **📐 Fractions as Division:**
    - 16/12 is the same as saying "16 divided by 12"
    - Fractions represent division problems!
    
    **⚖️ Fair Sharing:**
    - Even though not everyone gets exactly the same number of slices
    - The **average** is fair: 1⅓ slices per person
    - This is what "equal sharing" means in mathematics
    
    **🔄 Equivalent Representations:**
    - 16/12 = 4/3 = 1⅓ = 1.333... = 133.33%
    - All of these represent the same mathematical value!
    """)

# Interactive Quiz
st.markdown("---")
st.markdown("### 🎮 Test Your Understanding!")

quiz_question = st.radio(
    "**Based on the Birthday Party Challenge, each friend gets:**",
    [
        "Exactly 1 slice each",
        "Exactly 1⅓ slices each", 
        "4/3 slices each (which equals 1⅓)",
        "Some get 1 slice, some get 2 slices, averaging 1⅓ each"
    ],
    key="birthday_quiz"
)

if st.button("🎯 Check My Answer!", key="check_birthday"):
    if "4/3 slices each" in quiz_question or "Some get 1 slice, some get 2 slices" in quiz_question:
        st.success("🌟 Excellent! You understand both the mathematical answer (4/3 slices) AND the practical reality!")
        st.balloons()
        st.info("💡 Key insight: Math gives us the exact answer (4/3), but real life requires practical solutions (some get 1, some get 2).")
    elif "1⅓ slices each" in quiz_question:
        st.success("✅ Correct mathematically! 1⅓ = 4/3. In practice, some friends would get 1 slice, others 2 slices.")
    else:
        st.error("❌ Not quite! Remember: 16 slices ÷ 12 friends = 16/12 = 4/3 = 1⅓ slices each on average.")

st.markdown("---")
st.markdown("""
### 🎯 Summary:
**The Birthday Party Challenge** teaches us that:
- **Mathematical answer:** Each friend gets 4/3 (or 1⅓) slices
- **Practical solution:** 4 friends get 2 slices, 8 friends get 1 slice  
- **Both are correct!** Math gives us the exact answer, real life gives us the practical solution
- **Key concept:** Division, fractions, and fair sharing all work together! 🍕🎉
""")
