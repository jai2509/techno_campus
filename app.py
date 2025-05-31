import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load .env if it exists (for local development)
load_dotenv()

# Get the API key from Streamlit secrets (for deployment) or environment variables (for local development)
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

# Check if the API key is set
if not api_key:
    st.error("GROQ_API_KEY not found. Please set it in Streamlit Cloud secrets or .env for local development.")
    st.stop()

# Initialize the Groq client
client = Groq(api_key=api_key)

# Function to ask a question using Groq API
def ask_question(question):
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model="llama3-8b-8192"  # Replace with the appropriate model ID if needed
    )
    return response.choices[0].message.content

# Streamlit app UI
st.title("Groq API Question Answerer for Techno Campus")
st.write("Enter a question to get an AI-powered response, supporting TransStadia University's Techno Campus.")

question = st.text_input("Ask a question")

if st.button("Get Answer"):
    if question:
        answer = ask_question(question)
        st.write("**Answer**:")
        st.write(answer)
    else:
        st.write("Please enter a question")
