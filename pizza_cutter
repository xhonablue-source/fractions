import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="MathCraft | Pizza Fraction & Division Adventures", 
    layout="centered",
    page_icon="🍕"
)

# Header with logo-style branding
st.markdown("""
<div style="text-align: center; padding: 1.5rem; background: linear-gradient(90deg, #ff6b6b 0%, #ffa500 50%, #ff6b6b 100%); border-radius: 15px; margin-bottom: 2rem; box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);">
    <h1 style="color: white; margin: 0; font-weight: bold; font-size: 2.5em;">🍕 MathCraft</h1>
    <p style="color: #fff8dc; margin: 0; font-style: italic; font-size: 1.3em;">Pizza Fraction & Division Adventures</p>
    <p style="color: #ffe4b5; margin: 0; font-size: 0.9rem; margin-top: 0.5rem;">© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ff6b6b; font-size: 2.2em;'>🍕 Pizza Math Adventures!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666; font-style: italic;'>Learn fractions and division the delicious way!</h3>", unsafe_allow_html=True)

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# Michigan Learning Standards for 5th Grade
st.markdown("---")
st.markdown("### 📚 Michigan Learning Standards - Grade 5")
with st.expander("🎯 Click to see what we're learning today!"):
    st.markdown("""
    **5.NF.1** - Add and subtract fractions with unlike denominators
    *🍕 Applied through: Understanding pizza slices as fractions (1/8, 1/4, etc.)*
    
    **5.NF.2** - Solve word problems involving addition and subtraction of fractions
    *🍕 Applied through: Real pizza sharing scenarios and fraction combinations*
    
    **5.NF.3** - Interpret a fraction as division of the numerator by the denominator
    *🍕 Applied through: Understanding that 3/8 means 3 ÷ 8*
    
    **5.MD.1** - Convert among different-sized standard measurement units
    *🍕 Applied through: Understanding degrees in a circle (360°)*
    
    **5.G.2** - Represent real world problems by graphing points and shapes
    *🍕 Applied through: Pizza slice geometry and circular divisions*
    
    **Mathematical Practices:**
    - **MP.1** - Make sense of problems *(real pizza sharing scenarios)*
    - **MP.2** - Reason abstractly *(connecting fractions to division)*
    - **MP.4** - Model with mathematics *(using pizza to understand fractions)*
    - **MP.6** - Attend to precision *(exact equal shares)*
    - **MP.7** - Look for structure *(patterns in fraction equivalents)*
    """)

st.markdown("---")
st.markdown("### 👨‍🎓 Student Information")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name:", key="student_name", placeholder="Enter your first and last name")
with col2:
    date = st.text_input("Today's Date:", key="student_date", placeholder="MM/DD/YYYY")

st.session_state.responses.update({"Name": name, "Date": date})

# Learning Objective - Fun Version
st.markdown("---")
st.markdown("""
### 🎯 Today's Pizza Mission!

**Your Mission:** Become a Pizza Math Expert! You'll learn to:
- 🍕 Cut pizzas into equal parts (fractions!)
- 🧮 Understand what fractions really mean
- ➗ See how division and fractions are best friends
- 🎮 Use our amazing Pizza Wheel to explore math

**Big Secret:** Math is everywhere - especially in pizza! 🤫
""")

# Section 1: Meet the Pizza Wheel!
st.markdown("---")
st.markdown("### 🎡 Section 1: Meet Our Amazing Pizza Wheel!")
st.markdown("**Get ready for some pizza magic!** This isn't just any pizza - it's a mathematical masterpiece!")

# Interactive Pizza Wheel Introduction
people_count = st.slider("🎉 How many people are coming to your pizza party?", 2, 16, 8, key="people_slider")

st.markdown(f"""
### 🧮 The Math Magic:

<div style="background: linear-gradient(135deg, #ff9a56 0%, #ffb347 100%); padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0; box-shadow: 0 5px 15px rgba(255, 154, 86, 0.3);">
<h2 style="color: white; margin: 0;">🍕 Pizza ÷ {people_count} people = {people_count} slices!</h2>
<h3 style="color: #fff8dc; margin: 10px 0;">Each person gets 1/{people_count} of the whole pizza</h3>
</div>
""", unsafe_allow_html=True)

# The Amazing Pizza Wheel - Using our perfect working code!
pizza_wheel_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(135deg, #ff9a56 0%, #ffb347 50%, #ff9a56 100%);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .pizza-magic {{
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            max-width: 700px;
            width: 100%;
            text-align: center;
        }}

        .wheel-title {{
            font-size: 2.2em;
            color: #e67e22;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }}

        .controls {{
            margin-bottom: 25px;
        }}

        .slider-label {{
            font-size: 1.4em;
            font-weight: bold;
            color: #d35400;
            margin-bottom: 15px;
            display: block;
        }}

        .pizza-slider {{
            width: 100%;
            height: 15px;
            border-radius: 8px;
            background: linear-gradient(90deg, #e74c3c, #f39c12, #e67e22);
            outline: none;
            -webkit-appearance: none;
            margin: 20px 0;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
            border: 3px solid #d35400;
        }}

        .pizza-slider::-webkit-slider-thumb {{
            -webkit-appearance: none;
            appearance: none;
            width: 60px;
            height: 60px;
            background: radial-gradient(circle, #ff6b6b, #e74c3c);
            border: 4px solid #fff;
            border-radius: 50%;
            cursor: grab;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            transition: all 0.2s ease;
        }}

        .pizza-slider::-webkit-slider-thumb:hover {{
            transform: scale(1.1);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4);
        }}

        .pizza-slider::-webkit-slider-thumb:active {{
            cursor: grabbing;
            transform: scale(1.05);
        }}

        .fraction-display {{
            background: linear-gradient(135deg, #3498db, #9b59b6);
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            font-size: 1.5em;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }}

        .pizza-info {{
            background: linear-gradient(135deg, #2ecc71, #27ae60);
            color: white;
            padding: 15px;
            border-radius: 12px;
            margin: 15px 0;
            font-size: 1.2em;
        }}

        .instruction-text {{
            font-size: 1.1em;
            color: #7f8c8d;
            margin: 15px 0;
            font-weight: bold;
        }}

        .pizza-wheel-container {{
            background: linear-gradient(45deg, #fff, #f8f9fa);
            border-radius: 50%;
            padding: 15px;
            margin: 20px 0;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        }}
    </style>
</head>
<body>
    <div class="pizza-magic">
        <h1 class="wheel-title">🍕 The Amazing Pizza Wheel! 🎡</h1>
        
        <div class="controls">
            <label class="slider-label">👥 Party Size: <span id="sliceValue">{people_count}</span> people</label>
            <div class="instruction-text">← Smaller Party &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Bigger Party →</div>
            <input type="range" min="2" max="16" value="{people_count}" class="pizza-slider" id="partySlider">
            
            <div class="fraction-display">
                <p style="margin: 0; font-size: 1.8em;"><strong><span id="sliceCount">{people_count}</span> Equal Slices!</strong></p>
                <p style="margin: 10px 0; font-size: 1.3em;">Each person gets <span style="background: rgba(255,255,255,0.3); padding: 5px 10px; border-radius: 8px;" id="fractionDisplay">1/{people_count}</span> of the pizza</p>
            </div>
        </div>

        <div class="pizza-wheel-container">
            <svg width="350" height="350" id="pizzaWheel" style="filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.2));">
                <circle cx="175" cy="175" r="160" fill="#D2691E" stroke="#8B4513" stroke-width="5"/>
                <circle cx="175" cy="175" r="155" fill="#FFD700" opacity="0.9"/>
                <circle cx="175" cy="175" r="150" fill="none" stroke="#F4D03F" stroke-width="2" opacity="0.6"/>
            </svg>
        </div>

        <div class="pizza-info">
            <div id="pizzaInfo">
                <p><strong>🎯 Math Fact:</strong> Each slice is exactly <strong>1/{people_count}</strong> of the whole pizza!</p>
                <p><strong>🔢 As a decimal:</strong> 1 ÷ {people_count} = <strong>{1/people_count:.3f}</strong></p>
                <p><strong>📊 As a percentage:</strong> <strong>{(1/people_count)*100:.1f}%</strong> of the pizza per person!</p>
            </div>
        </div>
        
        <div style="background: linear-gradient(45deg, #f39c12, #e67e22); color: white; padding: 15px; border-radius: 10px; margin-top: 15px;">
            <strong>✨ Pizza Magic:</strong> No matter how many people come to the party, everyone gets an <em>exactly equal share</em> because math is fair and delicious!
        </div>
    </div>

    <script>
        const slider = document.getElementById('partySlider');
        const sliceValue = document.getElementById('sliceValue');
        const sliceCount = document.getElementById('sliceCount');
        const fractionDisplay = document.getElementById('fractionDisplay');
        const pizzaInfo = document.getElementById('pizzaInfo');
        const pizzaWheel = document.getElementById('pizzaWheel');

        const centerX = 175;
        const centerY = 175;
        const radius = 150;

        // Realistic pepperoni distribution like real pizza makers!
        function generatePepperoni(numSlices) {{
            const pepperoniData = [];
            
            let seed = 42069;
            function seededRandom() {{
                seed = (seed * 9301 + 49297) % 233280;
                return seed / 233280;
            }}
            
            // Create rings of pepperoni from center outward
            const rings = [
                {{ radius: 0.25, count: 4 }},     // Center ring
                {{ radius: 0.5, count: 7 }},      // Middle ring  
                {{ radius: 0.75, count: 10 }},    // Outer ring
                {{ radius: 0.9, count: 5 }}       // Edge ring
            ];
            
            rings.forEach(ring => {{
                const angleStep = (2 * Math.PI) / ring.count;
                
                for (let i = 0; i < ring.count; i++) {{
                    const baseAngle = i * angleStep;
                    const angleJitter = (seededRandom() - 0.5) * 0.7;
                    const angle = baseAngle + angleJitter;
                    
                    const radiusJitter = (seededRandom() - 0.5) * 0.1;
                    const distance = (ring.radius + radiusJitter) * radius;
                    const finalDistance = Math.min(distance, radius * 0.92);
                    
                    const x = centerX + finalDistance * Math.cos(angle);
                    const y = centerY + finalDistance * Math.sin(angle);
                    
                    pepperoniData.push({{ 
                        x: x, 
                        y: y, 
                        size: 6 + seededRandom() * 3
                    }});
                }}
            }});
            
            // Add a few random scattered pieces
            for (let i = 0; i < 3; i++) {{
                const angle = seededRandom() * 2 * Math.PI;
                const distance = seededRandom() * radius * 0.85;
                const x = centerX + distance * Math.cos(angle);
                const y = centerY + distance * Math.sin(angle);
                
                pepperoniData.push({{ 
                    x: x, 
                    y: y, 
                    size: 5 + seededRandom() * 3
                }});
            }}
            
            return pepperoniData;
        }}

        // Perfect pizza slicing with instant updates!
        function updatePizzaWheel() {{
            const numSlices = parseInt(slider.value);
            
            sliceValue.textContent = numSlices;
            sliceCount.textContent = numSlices;
            fractionDisplay.textContent = `1/${{numSlices}}`;
            
            const decimalValue = (1/numSlices).toFixed(3);
            const percentage = ((1/numSlices) * 100).toFixed(1);
            
            pizzaInfo.innerHTML = `
                <p><strong>🎯 Math Fact:</strong> Each slice is exactly <strong>1/${{numSlices}}</strong> of the whole pizza!</p>
                <p><strong>🔢 As a decimal:</strong> 1 ÷ ${{numSlices}} = <strong>${{decimalValue}}</strong></p>
                <p><strong>📊 As a percentage:</strong> <strong>${{percentage}}%</strong> of the pizza per person!</p>
            `;

            // Clear existing elements
            const existingPepperoni = pizzaWheel.querySelectorAll('.pepperoni');
            const existingLines = pizzaWheel.querySelectorAll('.slice-line');
            existingPepperoni.forEach(p => p.remove());
            existingLines.forEach(l => l.remove());

            // Perfect angle calculation
            const exactAngleStep = (2 * Math.PI) / numSlices;
            
            // Add pepperoni instantly
            const pepperoniData = generatePepperoni(numSlices);
            pepperoniData.forEach((pep) => {{
                const pepperoni = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                pepperoni.setAttribute('cx', pep.x);
                pepperoni.setAttribute('cy', pep.y);
                pepperoni.setAttribute('r', pep.size);
                pepperoni.setAttribute('fill', '#DC143C');
                pepperoni.setAttribute('stroke', '#8B0000');
                pepperoni.setAttribute('stroke-width', '1');
                pepperoni.setAttribute('class', 'pepperoni');
                pizzaWheel.appendChild(pepperoni);
            }});

            // Draw perfect slice lines instantly
            for (let i = 0; i < numSlices; i++) {{
                const exactAngle = i * exactAngleStep;
                const x2 = centerX + radius * Math.cos(exactAngle);
                const y2 = centerY + radius * Math.sin(exactAngle);
                
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', centerX);
                line.setAttribute('y1', centerY);
                line.setAttribute('x2', x2.toFixed(2));
                line.setAttribute('y2', y2.toFixed(2));
                line.setAttribute('stroke', '#2c3e50');
                line.setAttribute('stroke-width', '4');
                line.setAttribute('stroke-linecap', 'round');
                line.setAttribute('class', 'slice-line');
                pizzaWheel.appendChild(line);
            }}
        }}

        slider.addEventListener('input', function() {{
            updatePizzaWheel();
        }});

        updatePizzaWheel();
    </script>
</body>
</html>
"""

# Display the amazing pizza wheel
st.components.v1.html(pizza_wheel_html, height=800)

# Section 2: Fraction Detective Work
st.markdown("---")
st.markdown("### 🕵️ Section 2: Fraction Detective Work!")
st.markdown("**Time to become a Fraction Detective!** Use your pizza wheel to solve these mysteries!")

# Interactive fraction exploration
st.markdown("#### 🔍 Mystery #1: The Equal Shares Investigation")

detective_slices = st.slider("🔍 Set your pizza wheel to this many slices:", 2, 12, 6, key="detective_slider")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    **🕵️ Detective Report:**
    - **Total Pizza:** 1 whole pizza 🍕
    - **Number of Slices:** {detective_slices}
    - **Each Slice:** 1/{detective_slices} of the pizza
    - **As Decimal:** {1/detective_slices:.3f}
    - **As Percentage:** {(1/detective_slices)*100:.1f}%
    """)

with col2:
    st.markdown(f"""
    **🧮 Detective Math:**
    - 1 pizza ÷ {detective_slices} people = {detective_slices} slices
    - Each person gets: 1/{detective_slices}
    - If 2 people shared: 2/{detective_slices} = {2/detective_slices:.3f}
    - If 3 people shared: 3/{detective_slices} = {3/detective_slices:.3f}
    """)

# Section 3: Fraction vs Division - The Great Discovery!
st.markdown("---")
st.markdown("### 🎉 Section 3: The Great Math Discovery!")
st.markdown("**Are you ready for the BIGGEST math secret ever?** Fractions and division are the same thing!")

# Create visual comparison
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left side: Fraction representation
slices_demo = 8
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_aspect('equal')

# Draw pizza circle
circle = plt.Circle((0, 0), 1, fill=False, color='saddlebrown', linewidth=3)
ax1.add_patch(circle)
pizza_fill = plt.Circle((0, 0), 0.95, fill=True, color='gold', alpha=0.8)
ax1.add_patch(pizza_fill)

# Draw slice lines
for i in range(slices_demo):
    angle = i * (2 * np.pi) / slices_demo
    x = np.cos(angle)
    y = np.sin(angle)
    ax1.plot([0, x], [0, y], 'black', linewidth=2)

# Highlight one slice
angle1 = 0
angle2 = (2 * np.pi) / slices_demo
angles = np.linspace(angle1, angle2, 20)
slice_x = [0] + [np.cos(a) for a in angles] + [0]
slice_y = [0] + [np.sin(a) for a in angles] + [0]
ax1.fill(slice_x, slice_y, alpha=0.6, color='red', edgecolor='darkred', linewidth=2)

ax1.text(0, -1.5, f'1/{slices_demo} of the pizza', fontsize=16, ha='center', fontweight='bold', color='red')
ax1.text(0, 1.3, 'FRACTION', fontsize=18, ha='center', fontweight='bold', color='blue')
ax1.axis('off')

# Right side: Division representation
ax2.text(0.5, 0.8, '1 ÷ 8', fontsize=48, ha='center', va='center', fontweight='bold', color='blue')
ax2.text(0.5, 0.6, '=', fontsize=36, ha='center', va='center')
ax2.text(0.5, 0.4, f'{1/slices_demo:.3f}', fontsize=36, ha='center', va='center', fontweight='bold', color='red')
ax2.text(0.5, 0.1, 'DIVISION', fontsize=18, ha='center', va='center', fontweight='bold', color='blue')

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')

fig1.suptitle('🤯 AMAZING DISCOVERY: Fractions ARE Division!', fontsize=20, fontweight='bold', color='purple')
st.pyplot(fig1)

st.markdown("""
### 🤯 Mind = Blown!

**The Secret:** When you see a fraction like 3/8, it's really just saying "3 ÷ 8"!

- 1/2 = 1 ÷ 2 = 0.5
- 1/4 = 1 ÷ 4 = 0.25  
- 3/8 = 3 ÷ 8 = 0.375

**Try this:** Set your pizza wheel to 4 slices. Each slice is 1/4, which equals 1 ÷ 4 = 0.25!
""")

# Section 4: Pizza Party Problem Solving!
st.markdown("---")
st.markdown("### 🎊 Section 4: Pizza Party Problem Solving!")
st.markdown("**Time to use your new superpowers to solve real pizza problems!**")

# Interactive word problems
problem_choice = st.selectbox(
    "🎮 Choose your pizza adventure:",
    [
        "The Birthday Party Challenge",
        "The Sleepover Pizza Crisis", 
        "The Class Party Planner",
        "The Family Dinner Dilemma"
    ],
    key="problem_choice"
)

if problem_choice == "The Birthday Party Challenge":
    st.markdown("""
    **🎂 The Birthday Party Challenge:**
    
    Sarah is having a birthday party! She ordered 2 large pizzas for 12 friends. 
    If they cut each pizza into 8 equal slices, how much pizza does each friend get?
    """)
    
    party_answer = st.radio(
        "What's your answer?",
        ["Each friend gets 1/8 of a pizza", "Each friend gets 2/8 of a pizza", "Each friend gets 16/12 slices", "Each friend gets 4/3 slices"],
        key="party_q1"
    )

elif problem_choice == "The Sleepover Pizza Crisis":
    st.markdown("""
    **😴 The Sleepover Pizza Crisis:**
    
    At Maya's sleepover, there are 6 kids total. They have 1 pizza cut into 12 slices.
    Each kid wants an equal share. How many slices does each kid get?
    """)
    
    sleepover_answer = st.radio(
        "What's your answer?",
        ["2 slices each (2/12 of the pizza)", "3 slices each (3/12 of the pizza)", "1 slice each (1/12 of the pizza)", "6 slices each"],
        key="sleepover_q1"
    )

elif problem_choice == "The Class Party Planner":
    st.markdown("""
    **🎓 The Class Party Planner:**
    
    Your class of 24 students is having a party. The teacher orders 3 pizzas, each cut into 8 slices.
    What fraction of ONE pizza does each student get?
    """)
    
    class_answer = st.radio(
        "What's your answer?",
        ["1/8 of a pizza", "1/24 of a pizza", "3/24 of a pizza", "8/24 of a pizza"],
        key="class_q1"
    )

elif problem_choice == "The Family Dinner Dilemma":
    st.markdown("""
    **👨‍👩‍👧‍👦 The Family Dinner Dilemma:**
    
    The Johnson family (5 people) orders 1 pizza for dinner. If they want equal shares,
    what fraction does each person get?
    """)
    
    family_answer = st.radio(
        "What's your answer?",
        ["1/5 of the pizza", "5/1 of the pizza", "1/4 of the pizza", "2/5 of the pizza"],
        key="family_q1"
    )

# Section 5: Practice Questions
st.markdown("---")
st.markdown("### 🎮 Section 5: Test Your Pizza Powers!")

practice_col1, practice_col2 = st.columns(2)

with practice_col1:
    q1 = st.selectbox("If a pizza is cut into 6 equal slices, each slice is:", 
                     ["1/6 of the pizza", "6/1 of the pizza", "1/5 of the pizza", "6 pizzas"], key="q1")
    
    q2 = st.selectbox("What does 1/8 mean as division?", 
                     ["1 ÷ 8", "8 ÷ 1", "1 + 8", "1 × 8"], key="q2")
    
    q3 = st.selectbox("If 10 people share 1 pizza equally, each gets:", 
                     ["1/10 of the pizza", "10/1 of the pizza", "1/9 of the pizza", "2/10 of the pizza"], key="q3")

with practice_col2:
    q4 = st.selectbox("Which is bigger: 1/4 or 1/8?", 
                     ["1/4 (bigger slices)", "1/8 (more slices)", "They're equal", "Can't tell"], key="q4")
    
    q5 = st.selectbox("3/8 as a division problem is:", 
                     ["3 ÷ 8", "8 ÷ 3", "3 + 8", "3 × 8"], key="q5")
    
    q6 = st.selectbox("If you eat 2 slices of a pizza cut into 12 pieces, you ate:", 
                     ["2/12 of the pizza", "12/2 of the pizza", "2/10 of the pizza", "1/6 of the pizza"], key="q6")

# Creative Problem Solving
st.markdown("---")
st.markdown("### 🎨 Section 6: Creative Pizza Math!")

creative_col1, creative_col2 = st.columns(2)

with creative_col1:
    st.markdown("#### 🎨 Design Your Own Pizza Problem!")
    custom_people = st.number_input("How many people at your party?", min_value=2, max_value=20, value=6, key="custom_people")
    custom_pizzas = st.number_input("How many pizzas do you have?", min_value=1, max_value=5, value=1, key="custom_pizzas")
    
    if custom_pizzas == 1:
        fraction_per_person = f"1/{custom_people}"
        decimal_per_person = 1/custom_people
    else:
        fraction_per_person = f"{custom_pizzas}/{custom_people}"
        decimal_per_person = custom_pizzas/custom_people
    
    st.markdown(f"""
    **Your Pizza Math:**
    - **People:** {custom_people}
    - **Pizzas:** {custom_pizzas}
    - **Each person gets:** {fraction_per_person} = {decimal_per_person:.3f} pizza
    """)

with creative_col2:
    st.markdown("#### 🧠 Think Like a Mathematician!")
    thinking_question = st.text_area(
        "If you were the pizza party planner, how would you decide how many pizzas to order for your class? Explain your thinking!",
        height=100,
        key="thinking_math",
        placeholder="Think about: How many people? How hungry are they? What size slices?"
    )

# Real-World Applications
st.markdown("---")
st.markdown("### 🌍 Section 7: Pizza Math in the Real World!")

st.markdown("""
#### 🍕 Where Do We Use Fraction & Division Math?

**At Restaurants:** 🍽️
- Chefs divide recipes to make smaller or larger portions
- Servers split bills evenly among customers
- Pizza makers cut pizzas into equal slices

**In Sports:** ⚽
- Teams are divided into equal groups for practice
- Playing time is shared equally among players  
- Statistics are calculated using fractions (shooting percentage)

**At Home:** 🏠
- Splitting chores equally among family members
- Dividing snacks fairly among siblings
- Sharing game time on devices

**In Art & Design:** 🎨
- Creating patterns with equal parts
- Mixing paint colors in specific ratios
- Designing quilts with geometric patterns
""")

# Thinking Questions
st.markdown("---")
st.markdown("### 🤔 Section 8: Deep Thinking Questions")

thinking_col1, thinking_col2 = st.columns(2)

with thinking_col1:
    deep_q1 = st.text_area(
        "🤯 Mind Bender: Why do you think 1/2 is bigger than 1/4, even though 4 is bigger than 2?",
        height=80,
        key="deep1",
        placeholder="Think about pizza slices - which would you rather have?"
    )
    
    deep_q2 = st.text_area(
        "🔍 Pattern Detective: What happens to the slice size as you add more people to the party?",
        height=80,
        key="deep2", 
        placeholder="Try the pizza wheel with 4, then 8, then 16 people..."
    )

with thinking_col2:
    deep_q3 = st.text_area(
        "🎯 Real-World Problem: How would you fairly share 3 pizzas among 7 friends?",
        height=80,
        key="deep3",
        placeholder="Think step by step - what would you do first?"
    )
    
    deep_q4 = st.text_area(
        "🚀 Challenge Question: If each pizza slice is 1/8, how many slices make a whole pizza? How do you know?",
        height=80,
        key="deep4",
        placeholder="Use what you learned about fractions and division!"
    )

st.session_state.responses.update({
    "Custom_People": custom_people,
    "Custom_Pizzas": custom_pizzas,
    "Thinking_Math": thinking_question,
    "Deep_Q1": deep_q1,
    "Deep_Q2": deep_q2,
    "Deep_Q3": deep_q3,
    "Deep_Q4": deep_q4
})

# Answer Checking
st.markdown("---")
st.markdown("### ✅ Check Your Pizza Powers!")

# Store practice responses
st.session_state.responses.update({
    "Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4, "Q5": q5, "Q6": q6,
    "Problem_Choice": problem_choice
})

# Add problem-specific answers to responses
if problem_choice == "The Birthday Party Challenge":
    st.session_state.responses["Problem_Answer"] = party_answer
elif problem_choice == "The Sleepover Pizza Crisis":
    st.session_state.responses["Problem_Answer"] = sleepover_answer
elif problem_choice == "The Class Party Planner":
    st.session_state.responses["Problem_Answer"] = class_answer
elif problem_choice == "The Family Dinner Dilemma":
    st.session_state.responses["Problem_Answer"] = family_answer

# Answer key
correct_answers = {
    "Q1": "1/6 of the pizza",
    "Q2": "1 ÷ 8", 
    "Q3": "1/10 of the pizza",
    "Q4": "1/4 (bigger slices)",
    "Q5": "3 ÷ 8",
    "Q6": "2/12 of the pizza"
}

problem_correct_answers = {
    "The Birthday Party Challenge": "Each friend gets 4/3 slices",
    "The Sleepover Pizza Crisis": "2 slices each (2/12 of the pizza)",
    "The Class Party Planner": "1/8 of a pizza", 
    "The Family Dinner Dilemma": "1/5 of the pizza"
}

score = 0
for q_num in correct_answers:
    if st.session_state.responses.get(q_num) == correct_answers[q_num]:
        score += 1

# Check problem answer
if st.session_state.responses.get("Problem_Answer") == problem_correct_answers.get(problem_choice):
    score += 1

total_questions = 7  # 6 practice + 1 word problem

if st.button("🎯 Check My Pizza Powers!", type="primary"):
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

# Fun Facts Section
st.markdown("---")
st.markdown("### 🤓 Amazing Pizza Math Facts!")

fun_facts = [
    "🍕 The world's largest pizza was 122 feet in diameter - imagine cutting that into equal slices!",
    "🧮 Ancient Egyptians used fractions to divide bread and beer fairly among workers",
    "🎯 Pizza was invented in Italy, but using math to cut it fairly is universal!",
    "📊 Americans eat about 3 billion pizzas per year - that's a LOT of fraction practice!",
    "🔢 The word 'fraction' comes from Latin meaning 'to break' - just like breaking pizza into pieces!"
]

selected_fact = st.selectbox("Choose a fun fact:", fun_facts, key="fun_fact")
st.markdown(f"**{selected_fact}**")

# Summary Section
st.markdown("---")
st.markdown("### 📝 What We Learned Today!")

st.markdown("""
**🍕 Our Pizza Math Superpowers:**

1. **Fractions are Division!** 
   - 1/4 = 1 ÷ 4 = 0.25
   - 3/8 = 3 ÷ 8 = 0.375

2. **Equal Shares Make Fair Friends!**
   - When we divide pizza equally, everyone gets the same amount
   - The more people, the smaller each piece gets

3. **Real-World Math Rocks!**
   - Fractions help us share things fairly
   - Division helps us solve everyday problems
   - Math makes life more fair and fun!

**🎯 Remember:** Every time you share pizza, you're doing advanced mathematics! 
""")

# Submit Work
st.markdown("---")
if st.button("✅ Submit My Pizza Adventure!", type="primary"):
    if name and date:
        st.session_state.all_responses.append(st.session_state.responses.copy())
        st.success(f"🎉 Fantastic work, {name}! Your pizza math score: {score}/{total_questions} ({(score/total_questions)*100:.0f}%)")
        st.markdown("### 🏆 Certificate of Pizza Math Mastery!")
        st.markdown(f"""
        <div style="border: 5px solid #ff6b6b; padding: 20px; border-radius: 15px; text-align: center; background: linear-gradient(45deg, #ffeaa7, #fab1a0);">
        <h2>🍕 PIZZA MATH CERTIFICATE 🍕</h2>
        <p><strong>This certifies that</strong></p>
        <h3 style="color: #e17055;">{name}</h3>
        <p><strong>has successfully completed</strong></p>
        <h3>Pizza Fraction & Division Adventures</h3>
        <p><strong>Score: {score}/{total_questions} ({(score/total_questions)*100:.0f}%)</strong></p>
        <p><strong>Date: {date}</strong></p>
        <p style="font-style: italic;">Keep exploring the delicious world of mathematics!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("🍕 Please enter your name and date to get your Pizza Math Certificate!")

# Teacher Dashboard
st.markdown("---")
teacher_password = st.text_input("🏫 Teacher Access Code:", type="password", key="teacher_pass")

if teacher_password == "pizzamath2025":
    st.markdown("### 📊 Teacher Dashboard")
    if st.session_state.all_responses:
        df = pd.DataFrame(st.session_state.all_responses)
        st.dataframe(df, use_container_width=True)
        
        if len(df) > 0:
            total_scores = []
            for _, row in df.iterrows():
                student_score = 0
                for q_num in correct_answers:
                    if row.get(q_num) == correct_answers[q_num]:
                        student_score += 1
                # Add problem score
                if row.get("Problem_Answer") == problem_correct_answers.get(row.get("Problem_Choice")):
                    student_score += 1
                total_scores.append(student_score)
            
            avg_score = np.mean(total_scores)
            st.metric("Class Average", f"{avg_score:.1f}/{total_questions} ({(avg_score/total_questions)*100:.0f}%)")
            
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Class Data",
            data=csv,
            file_name="pizza_math_adventure_responses.csv",
            mime="text/csv"
        )
    else:
        st.info("No student responses yet.")
elif teacher_password and teacher_password != "pizzamath2025":
    st.error("❌ Incorrect access code")

# Final Message
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(45deg, #ff9a56, #ffb347); border-radius: 15px; color: white;">
<h3>🍕 Keep Being a Math Explorer! 🚀</h3>
<p>Remember: Math is everywhere, and it's always delicious when you approach it with curiosity!</p>
<p><em>Next time you have pizza, you'll know you're also having a math lesson!</em></p>
</div>
""", unsafe_allow_html=True)
