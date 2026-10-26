import streamlit as st

# Page Configuration
st.set_page_config(page_title="Happy Birthday Dad!", page_icon="🎉", layout="centered")

# Balloon animation on page load
st.balloons()

# Title
st.title("🎉 Happy Birthday, Dad! 🎉")
st.subheader("To the world's best dad—wishing you an amazing day!")

st.markdown("---")

# Birthday Card Message
st.markdown("""
    ### Dear Dad,
    Thank you for always being my biggest strength, my guiding light, and the person I can always count on. 
    Your hard work, kindness, and wisdom inspire me every single day.
    
    I hope this year brings you abundant health, true happiness, peace, and success in everything you do!
""")

st.markdown("---")

# Interactive Button
if st.button("Click to open your birthday wish ❤️"):
    st.success("✨ Hope your day is as wonderful and incredible as you are! Love you tons, Dad! ✨")