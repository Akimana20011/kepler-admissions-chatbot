# app.py
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from chatbot import load_chatbot

# Page settings
st.set_page_config(page_title="Kepler Admissions Chatbot")
st.title("🤖 Kepler College Admissions Chatbot")

# Load the chatbot
qa = load_chatbot()

# Ask user for input
question = st.text_input("Ask a question about Kepler admissions:")

# Generate and show the answer
if question:
    with st.spinner("Thinking..."):
        response = qa.run(question)
    st.markdown(f"**Answer:** {response}")
