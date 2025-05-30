import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="MathCraft | Pizza Fraction Adventures", 
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
- ➗ See how division and fractions are best friends
- 🎮 Use our amazing Pizza Wheel to explore math

**Big Secret:** Math is everywhere - especially in pizza! 🤫
""")

# Section 1: Interactive Pizza Wheel
st.markdown("---")
st.markdown("### 🎡 Section 1: The Amazing Pizza Wheel!")
st.markdown("**Get ready for some pizza magic!** This isn't just any pizza - it's a mathematical masterpiece!")

# Interactive Pizza Wheel Introduction
people_count = st.slider("🎉 How many people are coming to your pizza party?", 2, 16, 8, key="people_slider")

# Add special celebrations for key numbers - NO BALLOONS for wrong answers
if people_count == 8:
    st.success("🎯 Perfect! 8 people = 1/8 each = 0.125 = 12.5% per person!")
elif people_count == 4:
    st.success("🎉 Fantastic! 4 people = 1/4 each = 0.25 = 25% per person!")
elif people_count == 2:
    st.success("🍕 Amazing! 2 people = 1/2 each = 0.5 = 50% per person!")
    st.balloons()  # BALLOON #1 - Major fraction discovery (1/2)
elif people_count == 16:
    st.info("🤯 Wow! 16 people = 1/16 each = 0.0625 = 6.25% per person - tiny slices!")
elif people_count == 12:
    st.info("🎂 Like a birthday party! 12 people = 1/12 each = 0.083 = 8.33% per person!")

st.markdown(f"""
### 🧮 The Math Magic:

<div style="background: linear-gradient(135deg, #ff9a56 0%, #ffb347 100%); padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0; box-shadow: 0 5px 15px rgba(255, 154, 86, 0.3);">
<h2 style="color: white; margin: 0;">🍕 Pizza ÷ {people_count} people = {people_count} slices!</h2>
<h3 style="color: #fff8dc; margin: 10px 0;">Each person gets 1/{people_count} of the whole pizza</h3>
<h3 style="color: #fff8dc; margin: 10px 0;">That's {1/people_count:.3f} or {(1/people_count)*100:.1f}% each!</h3>
</div>
""", unsafe_allow_html=True)

# The Amazing Pizza Wheel - Pure HTML/JavaScript (No matplotlib!)
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
            width: 40px;
            height: 40px;
            background: radial-gradient(circle, #ff6b6b, #e74c3c);
            border: 3px solid #fff;
            border-radius: 50%;
            cursor: grab;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
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
        
        <label style="font-size: 1.4em; font-weight: bold; color: #d35400;">👥 Party Size: <span id="sliceValue">{people_count}</span> people</label>
        <div style="font-size: 1.1em; color: #7f8c8d; margin: 15px 0;">← Smaller Party &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Bigger Party →</div>
        <input type="range" min="2" max="16" value="{people_count}" class="pizza-slider" id="partySlider">
        
        <div class="fraction-display">
            <p style="margin: 0; font-size: 1.8em;"><strong><span id="sliceCount">{people_count}</span> Equal Slices!</strong></p>
            <p style="margin: 10px 0; font-size: 1.3em;">Each person gets <span style="background: rgba(255,255,255,0.3); padding: 5px 10px; border-radius: 8px;" id="fractionDisplay">1/{people_count}</span> of the pizza</p>
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

        // Generate realistic pepperoni
        function generatePepperoni(numSlices) {{
            const pepperoniData = [];
            let seed = 42069;
            function seededRandom() {{
                seed = (seed * 9301 + 49297) % 233280;
                return seed / 233280;
            }}
            
            const rings = [
                {{ radius: 0.25, count: 4 }},
                {{ radius: 0.5, count: 7 }},
                {{ radius: 0.75, count: 10 }},
                {{ radius: 0.9, count: 5 }}
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
                    pepperoniData.push({{ x: x, y: y, size: 6 + seededRandom() * 3 }});
                }}
            }});
            
            return pepperoniData;
        }}

        // Perfect pizza slicing function
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
            
            // Add pepperoni
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

            // Draw perfect slice lines
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

        slider.addEventListener('input', updatePizzaWheel);
        updatePizzaWheel();
    </script>
</body>
</html>
"""

# Display the pizza wheel
st.components.v1.html(pizza_wheel_html, height=800)

# Section 2: The Great Discovery!
st.markdown("---")
st.markdown("### 🎉 Section 2: The Great Math Discovery!")
st.markdown("**Are you ready for the BIGGEST math secret ever?** Fractions and division are the same thing!")

# Discovery demonstration
discovery_slices = st.slider("🔍 Test this with different slice counts:", 2, 12, 8, key="discovery_slider")

# Add celebration when students discover the pattern - NO BALLOONS for discoveries
if discovery_slices == 4:
    st.info("🎯 Try 1/4 = 1 ÷ 4 = 0.25 - Perfect quarters!")
elif discovery_slices == 8:
    st.info("🍕 Classic pizza! 1/8 = 1 ÷ 8 = 0.125 per slice!")
elif discovery_slices == 2:
    st.success("🎉 Half and half! 1/2 = 1 ÷ 2 = 0.5 - You discovered halves!")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    ### 📊 Fraction
    **{discovery_slices} slices**
    
    Each slice = **1/{discovery_slices}**
    """)

with col2:
    st.markdown(f"""
    ### ➗ Division
    **1 ÷ {discovery_slices}**
    
    = **{1/discovery_slices:.3f}**
    """)

with col3:
    st.markdown(f"""
    ### 📈 Percentage
    **{(1/discovery_slices)*100:.1f}%**
    
    of the whole pizza
    """)

st.markdown("""
### 🤯 Mind = Blown!

**The Secret:** When you see a fraction like 3/8, it's really just saying "3 ÷ 8"!

- 1/2 = 1 ÷ 2 = 0.5
- 1/4 = 1 ÷ 4 = 0.25  
- 3/8 = 3 ÷ 8 = 0.375

**Try this:** Set your pizza wheel to 4 slices. Each slice is 1/4, which equals 1 ÷ 4 = 0.25!
""")

# Section 3: Pizza Party Problem Solving!
st.markdown("---")
st.markdown("### 🎊 Section 3: Pizza Party Problem Solving!")
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
    
    # Birthday Party Math Visualizer
    st.markdown("#### 🧮 Let's Solve This Step by Step!")
    
    # Given information
    st.markdown("""
    **📋 What We Know:**
    - **🍕 Number of pizzas:** 2
    - **👥 Number of friends:** 12  
    - **✂️ Slices per pizza:** 8
    - **❓ Question:** How much pizza does each friend get?
    """)
    
    # Show the math
    st.markdown(f"""
    ### 🎯 The Math:

    <div style="background: linear-gradient(135deg, #3498db, #2980b9); color: white; padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0;">
    <h3 style="margin: 0;">2 pizzas × 8 slices = 16 total slices</h3>
    <h3 style="margin: 10px 0;">16 ÷ 12 = 16/12 = 4/3 ≈ 1.333 slices per friend</h3>
    <p style="margin: 10px 0; font-size: 1.1em;">Each friend gets <strong>1⅓ slices</strong> (1 whole slice + ⅓ of another slice)</p>
    </div>
    """, unsafe_allow_html=True)

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
                padding: 15px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}

            .party-container {{
                background: rgba(255, 255, 255, 0.95);
                padding: 25px;
                border-radius: 20px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
                max-width: 800px;
                width: 100%;
                text-align: center;
            }}

            .party-title {{
                font-size: 2em;
                color: #e74c3c;
                margin-bottom: 15px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            }}

            .pizza-row {{
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 20px 0;
                gap: 30px;
                flex-wrap: wrap;
            }}

            .pizza-container {{
                text-align: center;
            }}

            .pizza-label {{
                font-size: 1.1em;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 10px;
            }}

            .math-explanation {{
                background: linear-gradient(135deg, #00b894, #00a085);
                color: white;
                padding: 20px;
                border-radius: 15px;
                margin: 20px 0;
                font-size: 1.1em;
            }}

            .result-box {{
                background: linear-gradient(135deg, #fdcb6e, #e17055);
                color: white;
                padding: 20px;
                border-radius: 15px;
                margin: 20px 0;
                font-size: 1.2em;
            }}

            .slice {{
                fill: #f1c40f;
                stroke: #f39c12;
                stroke-width: 2;
                opacity: 0.8;
            }}

            .slice-line {{
                stroke: #2c3e50;
                stroke-width: 2;
                stroke-linecap: round;
            }}

            .slice-number {{
                font-family: Arial, sans-serif;
                font-size: 12px;
                font-weight: bold;
                fill: #2c3e50;
            }}

            .friends-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(60px, 1fr));
                gap: 10px;
                margin: 15px 0;
                max-width: 600px;
            }}

            .friend-card {{
                background: linear-gradient(135deg, #74b9ff, #0984e3);
                color: white;
                padding: 10px 5px;
                border-radius: 8px;
                font-size: 0.8em;
                font-weight: bold;
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
                    <svg width="180" height="180" id="pizza1">
                        <circle cx="90" cy="90" r="80" fill="#D2691E" stroke="#8B4513" stroke-width="3"/>
                        <circle cx="90" cy="90" r="75" fill="#FFD700" opacity="0.3"/>
                    </svg>
                </div>
                
                <div style="font-size: 1.5em; color: #e74c3c; font-weight: bold;">+</div>
                
                <div class="pizza-container">
                    <div class="pizza-label">🍕 Pizza #2 (8 slices)</div>
                    <svg width="180" height="180" id="pizza2">
                        <circle cx="90" cy="90" r="80" fill="#D2691E" stroke="#8B4513" stroke-width="3"/>
                        <circle cx="90" cy="90" r="75" fill="#FFD700" opacity="0.3"/>
                    </svg>
                </div>
            </div>

            <div class="result-box">
                <strong>🎯 Total Available:</strong> 16 slices from 2 pizzas<br>
                <strong>👥 To Share Among:</strong> 12 friends<br>
                <strong>🧮 Answer:</strong> 16 ÷ 12 = 4/3 = 1⅓ slices each
            </div>

            <div style="background: linear-gradient(135deg, #fd79a8, #e84393); color: white; padding: 15px; border-radius: 10px; margin: 15px 0;">
                <strong>👥 How It Works Out:</strong><br>
                Each friend gets <strong>1 whole slice + ⅓ of another slice</strong><br>
                <em>(4 friends get 2 slices, 8 friends get 1 slice, but it averages to 1⅓ each)</em>
            </div>

            <div class="friends-grid" id="friendsGrid">
                <!-- Friends will be populated by JavaScript -->
            </div>

            <div style="background: linear-gradient(45deg, #6c5ce7, #a29bfe); color: white; padding: 15px; border-radius: 10px; margin-top: 15px;">
                <strong>✨ The Answer:</strong> Each friend gets <strong>4/3 slices</strong> or <strong>1⅓ slices</strong><br>
                <em>In practice: 4 friends get 2 slices each, 8 friends get 1 slice each</em>
            </div>
        </div>

        <script>
            function drawPizza(svgId, slicesPerPizza) {{
                const svg = document.getElementById(svgId);
                const centerX = 90;
                const centerY = 90;
                const radius = 75;
                
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
                    const textRadius = radius * 0.6;
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
                const friendsWithTwoSlices = totalSlices % numFriends; // 4 friends
                
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
    st.components.v1.html(party_visualizer_html, height=700)
    
    party_answer = st.radio(
        "What's your answer?",
        ["Each friend gets 1/8 of a pizza", "Each friend gets 2/8 of a pizza", "Each friend gets 16/12 slices", "Each friend gets 4/3 slices"],
        key="party_q1"
    )
    
    # Instant feedback for Birthday Party Challenge
    if party_answer == "Each friend gets 4/3 slices":
        st.success("🎉 EXCELLENT! You solved the Birthday Party Challenge perfectly!")
        st.info("💡 Great reasoning: 16 total slices ÷ 12 friends = 16/12 = 4/3 slices each!")
    elif party_answer != "Each friend gets 4/3 slices" and party_answer != "":
        st.error("❌ Not quite! Remember: 2 pizzas × 8 slices = 16 total slices, then 16 ÷ 12 friends = 4/3")
        st.info("🤔 Hint: Calculate total slices first, then divide by number of friends!")

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
    
    # Instant feedback for Sleepover Crisis
    if sleepover_answer == "2 slices each (2/12 of the pizza)":
        st.success("🌙 PERFECT! You solved the sleepover crisis!")
        st.info("💡 Excellent math: 12 slices ÷ 6 kids = 2 slices each!")
    elif sleepover_answer != "2 slices each (2/12 of the pizza)" and sleepover_answer != "":
        st.error("❌ Try again! 12 slices ÷ 6 kids = ? slices each")
        st.info("🤔 Hint: How many times does 6 go into 12?")

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
    
    # Instant feedback for Class Party
    if class_answer == "1/8 of a pizza":
        st.success("🎓 BRILLIANT! You're ready to plan any class party!")
        st.info("💡 Smart thinking: 24 slices ÷ 24 students = 1 slice each = 1/8 of a pizza!")
    elif class_answer != "1/8 of a pizza" and class_answer != "":
        st.error("❌ Think step by step! 3 pizzas × 8 slices = 24 total slices for 24 students")
        st.info("🤔 Hint: If each student gets 1 slice, and each pizza has 8 slices, what fraction is that?")

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
    
    # Instant feedback for Family Dinner
    if family_answer == "1/5 of the pizza":
        st.success("👨‍👩‍👧‍👦 WONDERFUL! The Johnson family will be so happy!")
        st.info("💡 Perfect logic: 1 pizza ÷ 5 people = 1/5 each!")
    elif family_answer != "1/5 of the pizza" and family_answer != "":
        st.error("❌ Remember the basic rule: 1 pizza ÷ number of people = fraction each")
        st.info("🤔 Hint: 1 pizza shared among 5 people means each gets 1/? of the pizza")

# Section 4: Practice Questions
st.markdown("---")
st.markdown("### 🎮 Section 4: Test Your Pizza Powers!")

practice_col1, practice_col2 = st.columns(2)

with practice_col1:
    q1 = st.selectbox("If a pizza is cut into 6 equal slices, each slice is:", 
                     ["1/6 of the pizza", "6/1 of the pizza", "1/5 of the pizza", "6 pizzas"], key="q1")
    
    # Instant feedback for Q1
    if q1 == "1/6 of the pizza":
        st.success("🌟 Correct! Perfect understanding of fractions!")
    elif q1 != "1/6 of the pizza" and q1 != "":
        st.error("❌ Not quite! Remember: 1 pizza ÷ 6 slices = 1/6 per slice")
    
    q2 = st.selectbox("What does 1/8 mean as division?", 
                     ["1 ÷ 8", "8 ÷ 1", "1 + 8", "1 × 8"], key="q2")
    
    # Instant feedback for Q2
    if q2 == "1 ÷ 8":
        st.success("🎯 Excellent! Fractions ARE division!")
    elif q2 != "1 ÷ 8" and q2 != "":
        st.error("❌ Try again! Fractions mean division: 1/8 = 1 ÷ 8")
    
    q3 = st.selectbox("If 10 people share 1 pizza equally, each gets:", 
                     ["1/10 of the pizza", "10/1 of the pizza", "1/9 of the pizza", "2/10 of the pizza"], key="q3")
    
    # Instant feedback for Q3
    if q3 == "1/10 of the pizza":
        st.success("🍕 Amazing! You've mastered pizza sharing!")
    elif q3 != "1/10 of the pizza" and q3 != "":
        st.error("❌ Think again! 1 pizza ÷ 10 people = 1/10 each")

with practice_col2:
    q4 = st.selectbox("Which is bigger: 1/4 or 1/8?", 
                     ["1/4 (bigger slices)", "1/8 (more slices)", "They're equal", "Can't tell"], key="q4")
    
    # Instant feedback for Q4
    if q4 == "1/4 (bigger slices)":
        st.success("🧠 Brilliant! Fewer pieces = bigger slices!")
    elif q4 != "1/4 (bigger slices)" and q4 != "":
        st.error("❌ Think about pizza: Would you rather have 1/4 or 1/8 of a pizza?")
    
    q5 = st.selectbox("3/8 as a division problem is:", 
                     ["3 ÷ 8", "8 ÷ 3", "3 + 8", "3 × 8"], key="q5")
    
    # Instant feedback for Q5
    if q5 == "3 ÷ 8":
        st.success("🚀 Outstanding! You understand fractions perfectly!")
    elif q5 != "3 ÷ 8" and q5 != "":
        st.error("❌ Remember: 3/8 means 3 ÷ 8")
    
    q6 = st.selectbox("If you eat 2 slices of a pizza cut into 12 pieces, you ate:", 
                     ["2/12 of the pizza", "12/2 of the pizza", "2/10 of the pizza", "1/6 of the pizza"], key="q6")
    
    # Instant feedback for Q6
    if q6 == "2/12 of the pizza":
        st.success("🎉 Perfect! 2 slices out of 12 = 2/12!")
    elif q6 != "2/12 of the pizza" and q6 != "":
        st.error("❌ Count carefully: 2 slices out of 12 total = 2/12")

# Add celebration for getting all answers right - BALLOON #2
correct_count = 0
answers = [q1, q2, q3, q4, q5, q6]
correct_answers_list = ["1/6 of the pizza", "1 ÷ 8", "1/10 of the pizza", "1/4 (bigger slices)", "3 ÷ 8", "2/12 of the pizza"]

for i, answer in enumerate(answers):
    if answer == correct_answers_list[i]:
        correct_count += 1

if correct_count == 6 and all(answer != "" for answer in answers):
    st.markdown("### 🏆 PIZZA MASTER ACHIEVEMENT UNLOCKED! 🏆")
    st.success("🌟 INCREDIBLE! You got ALL 6 questions correct! You're officially a Pizza Math Expert!")
    st.balloons()  # BALLOON #2 - Perfect score achievement
    st.markdown("🎊 **Congratulations!** 🎊")
elif correct_count >= 4 and all(answer != "" for answer in answers):
    st.markdown("### 🎯 Excellent Work!")
    st.success(f"Great job! You got {correct_count} out of 6 correct!")

# Section 5: Creative Pizza Math
st.markdown("---")
st.markdown("### 🎨 Section 5: Creative Pizza Math!")

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

# Store responses
st.session_state.responses.update({
    "Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4, "Q5": q5, "Q6": q6,
    "Problem_Choice": problem_choice,
    "Custom_People": custom_people,
    "Custom_Pizzas": custom_pizzas,
    "Thinking_Math": thinking_question
})

# Add problem-specific answers
if problem_choice == "The Birthday Party Challenge":
    st.session_state.responses["Problem_Answer"] = party_answer
elif problem_choice == "The Sleepover Pizza Crisis":
    st.session_state.responses["Problem_Answer"] = sleepover_answer
elif problem_choice == "The Class Party Planner":
    st.session_state.responses["Problem_Answer"] = class_answer
elif problem_choice == "The Family Dinner Dilemma":
    st.session_state.responses["Problem_Answer"] = family_answer

# Answer Checking
st.markdown("---")
st.markdown("### ✅ Check Your Pizza Powers!")

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
        
        # BALLOON #3 + CONFETTI - Final program completion celebration!
        st.balloons()
        
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
        
        # Add confetti-style celebration text
        st.markdown("""
        ### 🎊 CONGRATULATIONS! 🎊
        **You are now officially a Pizza Math Expert!**
        
        🌟 **What you've mastered:**
        - Fractions and division are the same thing!
        - Pizza sharing = mathematical fairness
        - Visual math makes everything clearer
        - Math is everywhere and delicious!
        
        **Keep using your pizza powers in real life!** 🍕✨
        """)
        
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
            
            if total_scores:  # Check if we have scores
                import statistics
                avg_score = statistics.mean(total_scores)
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

# Real-World Applications
st.markdown("---")
st.markdown("### 🌍 Pizza Math in the Real World!")

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
st.markdown("### 🤔 Deep Thinking Questions")

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

# Store thinking responses
st.session_state.responses.update({
    "Deep_Q1": deep_q1,
    "Deep_Q2": deep_q2,
    "Deep_Q3": deep_q3,
    "Deep_Q4": deep_q4
})

# Pizza Calculator Tool
st.markdown("---")
st.markdown("### 🧮 Pizza Calculator Tool!")
st.markdown("**Use this tool to solve any pizza sharing problem!**")

calc_col1, calc_col2, calc_col3 = st.columns(3)

with calc_col1:
    calc_pizzas = st.number_input("Number of Pizzas:", min_value=1, max_value=10, value=2, key="calc_pizzas")
    calc_slices_per_pizza = st.number_input("Slices per Pizza:", min_value=4, max_value=16, value=8, key="calc_slices")

with calc_col2:
    calc_people = st.number_input("Number of People:", min_value=1, max_value=50, value=12, key="calc_people")
    
with calc_col3:
    if calc_people > 0:
        total_slices = calc_pizzas * calc_slices_per_pizza
        slices_per_person = total_slices / calc_people
        pizza_per_person = slices_per_person / calc_slices_per_pizza
        
        st.markdown(f"""
        **Results:**
        - **Total slices:** {total_slices}
        - **Per person:** {slices_per_person:.2f} slices
        - **Fraction of pizza:** {pizza_per_person:.3f}
        - **Percentage:** {pizza_per_person*100:.1f}%
        """)

# Pizza Memory Game
st.markdown("---")
st.markdown("### 🎮 Pizza Memory Challenge!")
st.markdown("**Test your fraction memory!**")

if st.button("🎲 Generate Random Pizza Challenge!", key="memory_game"):
    import random
    random_slices = random.randint(3, 12)
    random_people = random.randint(2, random_slices)
    
    st.markdown(f"""
    ### 🍕 Challenge:
    **A pizza is cut into {random_slices} slices and shared among {random_people} people.**
    
    **Quick! What fraction does each person get?**
    """)
    
    challenge_answer = st.selectbox(
        "Your answer:",
        [f"1/{random_people}", f"1/{random_slices}", f"{random_people}/{random_slices}", f"{random_slices}/{random_people}"],
        key="challenge_answer"
    )
    
    correct_challenge = f"{random_slices//random_people if random_slices % random_people == 0 else random_slices}/{random_people}"
    
    if st.button("Check Challenge Answer!", key="check_challenge"):
        # Simplified check - each person gets equal slices
        if random_slices % random_people == 0:
            slices_each = random_slices // random_people
            if challenge_answer == f"1/{random_people}" and slices_each == 1:
                st.success(f"🌟 Correct! Each person gets {slices_each} slice, which is 1/{random_people} of the pizza!")
            elif str(slices_each) in challenge_answer:
                st.success(f"🌟 Correct! Each person gets {slices_each} slices!")
            else:
                st.error(f"Not quite! Each person gets {slices_each} slices = {slices_each}/{random_slices} of the pizza")
        else:
            correct_fraction = f"{random_slices}/{random_people}"
            if challenge_answer == correct_fraction:
                st.success(f"🌟 Correct! Each person gets {random_slices}/{random_people} slices!")
            else:
                st.error(f"Not quite! Each person gets {random_slices}/{random_people} slices")

# Final Message
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(45deg, #ff9a56, #ffb347); border-radius: 15px; color: white;">
<h3>🍕 Keep Being a Math Explorer! 🚀</h3>
<p>Remember: Math is everywhere, and it's always delicious when you approach it with curiosity!</p>
<p><em>Next time you have pizza, you'll know you're also having a math lesson!</em></p>
<h4>🎯 Key Takeaways:</h4>
<p>✅ Fractions = Division<br>
✅ Equal shares = Fair shares<br>
✅ Math makes life better!<br>
✅ Pizza makes math delicious! 🍕</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 10px; color: #666; font-size: 0.9em;">
<p>Built with ❤️ for young mathematicians everywhere</p>
<p>Questions? Contact your teacher or visit our help section!</p>
</div>
""", unsafe_allow_html=True)
