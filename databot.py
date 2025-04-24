import streamlit as st
import pandas as pd
from gemini_api import init_gemini
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

st.title("Data Q&A Bot")
st.write("Upload a CSV and ask questions about your data!")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    user_question = st.text_input("Ask a question about the data:")

    if user_question:
        prompt = f"""You are a data analyst. A user uploaded a CSV dataset:
{df.head(10).to_string(index=False)}

The user asked: {user_question}
Respond with a helpful, clear answer based only on the data.
"""

        with st.spinner("Thinking..."):
            try:
                # Initialize the Gemini model
                model = init_gemini()  # Removed the api_key argument
                
                # Generate response using Gemini
                response = model.generate_content(prompt)
                
                # Display the response
                st.success(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")