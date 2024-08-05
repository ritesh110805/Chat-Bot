from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

### Function to load Gemini Pro-Model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question) -> str:
    response = model.generate_content(question)
    return response.text

### Initialize our streamlit application
st.set_page_config(page_title="Chatbot")
st.header("ASK")
input = st.text_input("Input: ",key = "input")
submit = st.button("Ask the question?")

### When user submit it clicked 
if submit :
    response = get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)

# END
# END