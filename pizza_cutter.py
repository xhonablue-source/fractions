import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Pizza Math Adventure", 
    layout="centered",
    page_icon="🍕"
)

st.title("🍕 Pizza Math Adventure!")
st.markdown("### Learn fractions with our amazing pizza wheel!")

# Interactive Pizza Wheel (No matplotlib needed!)
people_count = st.slider("🎉 How many people at your pizza party?", 2, 16, 8)

st.markdown(f"""
### 🧮 The Math Magic:
**🍕 Pizza ÷ {people_count} people = {people_count} slices!**
**Each person gets 1/{people_count} of the whole pizza**
""")

# The Amazing Pizza Wheel - Pure HTML/JavaScript
pizza_wheel_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: 'Comic Sans MS', cursive;
            background: linear-gradient(135deg, #ff9a56, #ffb347);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .pizza-container {{
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }}
        .slider {{
            width: 100%;
            height: 15px;
            border-radius: 8px;
            background: linear-gradient(90deg, #e74c3c, #f39c12);
            outline: none;
            margin: 20px 0;
        }}
        .fraction-display {{
            background: linear-gradient(135deg, #3498db, #9b59b6);
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            font-size: 1.5em;
        }}
    </style>
</head>
<body>
    <div class="pizza-container">
        <h1>🍕 The Amazing Pizza Wheel! 🎡</h1>
        
        <label>👥 Party Size: <span id="sliceValue">{people_count}</span> people</label>
        <input type="range" min="2" max="16" value="{people_count}" class="slider" id="partySlider">
        
        <div class="fraction-display">
            <p><strong><span id="sliceCount">{people_count}</span> Equal Slices!</strong></p>
            <p>Each person gets <span id="fractionDisplay">1/{people_count}</span> of the pizza</p>
        </div>

        <svg width="300" height="300" id="pizzaWheel">
            <circle cx="150" cy="150" r="140" fill="#D2691E" stroke="#8B4513" stroke-width="4"/>
            <circle cx="150" cy="150" r="135" fill="#FFD700" opacity="0.9"/>
        </svg>

        <div style="background: #2ecc71; color: white; padding: 15px; border-radius: 10px; margin-top: 15px;">
            <strong>✨ Pizza Magic:</strong> Math makes sharing fair and delicious!
        </div>
    </div>

    <script>
        const slider = document.getElementById('partySlider');
        const sliceValue = document.getElementById('sliceValue');
        const sliceCount = document.getElementById('sliceCount');
        const fractionDisplay = document.getElementById('fractionDisplay');
        const pizzaWheel = document.getElementById('pizzaWheel');

        function updatePizza() {{
            const numSlices = parseInt(slider.value);
            
            sliceValue.textContent = numSlices;
            sliceCount.textContent = numSlices;
            fractionDisplay.textContent = `1/${{numSlices}}`;

            // Clear existing lines
            const existingLines = pizzaWheel.querySelectorAll('.slice-line');
            existingLines.forEach(l => l.remove());

            // Draw perfect slice lines
            const centerX = 150, centerY = 150, radius = 135;
            const exactAngleStep = (2 * Math.PI) / numSlices;
            
            for (let i = 0; i < numSlices; i++) {{
                const exactAngle = i * exactAngleStep;
                const x2 = centerX + radius * Math.cos(exactAngle);
                const y2 = centerY + radius * Math.sin(exactAngle);
                
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', centerX);
                line.setAttribute('y1', centerY);
                line.setAttribute('x2', x2);
                line.setAttribute('y2', y2);
                line.setAttribute('stroke', '#000');
                line.setAttribute('stroke-width', '3');
                line.setAttribute('class', 'slice-line');
                pizzaWheel.appendChild(line);
            }}
        }}

        slider.addEventListener('input', updatePizza);
        updatePizza();
    </script>
</body>
</html>
"""

st.components.v1.html(pizza_wheel_html, height=600)

st.markdown("---")
st.markdown("### 🎮 Quick Math Quiz!")

q1 = st.selectbox("If a pizza is cut into 8 slices, each slice is:", 
                 ["1/8 of the pizza", "8/1 of the pizza", "1/7 of the pizza"], 
                 key="q1")

if st.button("Check Answer!"):
    if q1 == "1/8 of the pizza":
        st.success("🌟 Correct! You're a pizza math expert!")
        st.balloons()
    else:
        st.error("Not quite! Try again!")

st.markdown("---")
st.markdown("**🎯 Remember:** Every time you share pizza fairly, you're doing mathematics!")
